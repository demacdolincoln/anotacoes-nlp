from preprocessing import preprocessing
from glob import glob
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from ignite.engine import create_supervised_trainer, create_supervised_evaluator
from ignite.engine import Events
from ignite.metrics import Accuracy

files = glob("../../../datasets/sentiment labelled sentences/*labelled.txt")

_, corpus_text = preprocessing([open(i).read() for i in files], lang=["english"])

word2id, id2word = {}, {}

uniques = set()
for words in corpus_text:
    for w in words:
        uniques.add(w)

count_id = 0
for word in uniques:
    word2id[word] = count_id
    id2word[count_id] = word
    count_id += 1
    
window = 2
pair_ids = []

text_size = len(corpus_text)

corpus_text = np.array(corpus_text)
mask = np.array([i for i in range(-window, window+1) if i is not 0])

for paragraph in corpus_text:
    paragraph = np.array(paragraph)
    text_size = len(paragraph)

    for center_word in range(window, text_size-window):
        center_word_id = word2id[paragraph[center_word]]
        for i in paragraph[mask + center_word]:
            context_word_id = word2id[i]
            pair_ids.append([center_word_id, context_word_id])

pair_ids = np.array(pair_ids)

##########################################
# define classes

class SkipGram(torch.nn.Module):
    def __init__(self, vocab_size, emb_size):
        super(SkipGram, self).__init__()
        
        self.embeddings = torch.nn.Embedding(vocab_size, emb_size)
        
        self.dropout = torch.nn.Dropout()
        
        self.linear0 =  torch.nn.Sequential(
            torch.nn.Linear(emb_size, emb_size*2),
            torch.nn.ReLU()
        )
        self.linear1 = torch.nn.Linear(emb_size*2, vocab_size)

        self.log_softmax = torch.nn.LogSoftmax(dim=1)
        
    def forward(self, x):
        out = self.embeddings(x)
        out = self.linear0(out)
        out = torch.nn.functional.dropout(out)
        out = torch.relu(self.linear1(out))
        
        out = self.log_softmax(out)
        return out
    
    def get_word_emb(self, word_id):
        word = torch.LongTensor([word_id])
        return self.embeddings(word).view(1, -1)
    
class Dataset(Dataset):
    def __init__(self, obj):
        self.len = len(obj)
        self.x = torch.LongTensor(obj[:, 0])
        self.y = torch.LongTensor(obj[:, 1])
    def __getitem__(self, index):
        return (self.x[index], self.y[index])
    def __len__(self):
        return self.len

###############################################
# train

dataset = Dataset(pair_ids)
data = DataLoader(dataset=dataset,
                  batch_size=int(dataset.len/3),
                  shuffle=True)

model = SkipGram(len(uniques), 10)
# import ipdb; ipdb.set_trace()
criterion = torch.nn.NLLLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

trainer = create_supervised_trainer(
    model, optimizer, criterion
)
evaluator = create_supervised_evaluator(
    model,
    metrics={"accuracy": Accuracy()}
)

@trainer.on(Events.EPOCH_COMPLETED)
def validate(trainer):
    if trainer.state.epoch % 100 == 0:
        evaluator.run(dataset)
        metrics = evaluator.state.metrics
        print(f"epoch: {trainer.state.epoch:<4} | " + \
              f"accuracy: {metrics['accuracy']:.2f} | " + \
              f"loss: {trainer.state.output:.2f}")
              
state = trainer.run(dataset, max_epochs=1500)