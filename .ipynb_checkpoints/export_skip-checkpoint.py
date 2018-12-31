import numpy as np
from tqdm import trange
import pickle

with open("skip_s100.txt") as f:

    lin, col = tuple(map(int, f.readline().split()))

    data = np.memmap("skip_np.npy", mode="w+",
                     type=np.float, shape=(lin, col))

    id2word, word2id = [], {}

    for i in trange(lin):
        line = f.readline().split()
        w = "".join(line[:-col])
        id2word.append(w)
        word2id[w] = i
        data[i, :] = line[-col:]

    with open("skip_id2word.pickle", "wb") as id2w_file:
        pickle.dump(id2word, id2w_file)
        id2w_file.close()

    with open("skip_word2id.pickle", "wb") as w2id_file:
        pickle.dump(word2id, w2id_file)
        w2id_file.close()
