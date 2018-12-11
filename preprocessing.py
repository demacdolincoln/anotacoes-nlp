import nltk
import gensim
import wikipedia
import re

wikipedia.set_lang("pt")
text = wikipedia.page("Alan_Turing").content

corpus_text = []

stop_words = nltk.corpus.stopwords.words("portuguese") +\
             nltk.corpus.stopwords.words("english")

for i in text.splitlines():
    clean_text = re.sub("\d", "", i) # remove numbers
    clean_text = gensim.utils.simple_preprocess(i)
    clean_text = [i for i in clean_text if i not in stop_words]
    corpus_text.append(clean_text)
        
# save using pickle
import pickle

with open("corpus_text.pickle", "wb") as f:
   pickle.dump(corpus_text, f)
   f.close()