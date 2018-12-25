from nltk.corpus import stopwords
from gensim.utils import simple_preprocess
import re

def preprocessing(texts=[], lang=["portuguese", "english"]):
    original_text, corpus_text = [], []

    stop_words = []
    for l in lang:
        stop_words += stopwords.words(l)
    
    for text in texts:
        for i in text.splitlines():
            original_text.append(i)
            
            clean_text = re.sub("\d", "", i) # remove numbers
            clean_text = simple_preprocess(i)
            clean_text = [i for i in clean_text if i not in stop_words]
            corpus_text.append(clean_text)
    
    # remove empty corpus
    empty_lines = reversed([i for i, j in enumerate(corpus_text) if len(j) == 0])
#     import ipdb; ipdb.set_trace()
    for i in empty_lines:
        original_text.pop(i)
        corpus_text.pop(i)
    
    return original_text, corpus_text

if __name__ == '__main__':
    import wikipedia
    import pickle # save using pickle
    
    page_title = "Alan_Turing"
    wikipedia.set_lang("pt")
    text = wikipedia.page(page_title).content
    
    original_text, corpus_text = preprocessing(texts=[text])

    with open("corpus_text.pickle", "wb") as f:
       pickle.dump(corpus_text, f)
       f.close()
    
    with open(f"original_text-{page_title}.pickle", "wb") as f:
        pickle.dump(original_text, f)
        f.close()