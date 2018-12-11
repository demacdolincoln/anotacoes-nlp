.. title: Pré-processamento de textos
.. slug: pre-processamento-de-textos
.. date: 2018-12-06 03:03:53 UTC-03:00
.. tags: utils 
.. category: 
.. link: 
.. description: 
.. type: text

Este é o processo padrão usado em praticamente todas as anotações relacionadas à NLP:

1. limpar o texto:

   * remover pontuação, acentos, e stop-words [1]_
   * colocar tudo em minúsculas

2. converter numa lista de termos usados.

A única excessão é com o TF-IDF e LSA e comparo quando o processamento é feito dividindo em parágrafos e com o texto inteiro de uma vez.

Sempre usarei textos da wikipédia, pelo simples motivo de ser muito prático e inteiramente legal.

bibliotecas usadas
------------------

.. code-block:: python

   %pylab inline
   import nltk
   import gensim
   import wikipedia

No Jupyter notebook o comando **%pylab** importa o matplotlib e numpy e configura o modo como os gráficos serão apresentados, ocasionalmente também usarei o Altair junto com o Pandas para visualizar os dados.

Pré-processamento
-----------------

.. code-block:: python
   :number-lines:
   
   wikipedia.set_lang("pt")
   text = wikipedia.page("Alan_Turing").content

   sentences = []

   stop_words = nltk.corpus.stopwords.words("portuguese") +\
                nltk.corpus.stopwords.words("english")

   for i in text.splitlines():
       clean_text = gensim.utils.simple_preprocess(i)
       clean_text = [i for i in clean_text if i not in stop_words]
       sentences.append(clean_text)

Explicando as etapas do código acima:

:linhas 6 e 7:
   lista de stop-words, como no texto há termos em inglês, juntei as duas listas (termos em português e em inglês) numa só.

:for:
   **splitlines** vai dividir o texto em parágrafod e a função **simple_preprocess()** do Gensim remove pontuação e converte tudo para minúsculas, em seguida removo as stop words e por último adiciono o parágrafo à lista de sentenças usadas no texto.


Facilitando as coisas
---------------------

Para dar maior foco ao que importa, salvei a lista de termos usando o pickle:

.. code-block:: python

   import pickle

   # salvando em arquivo
   with open("sentences.pickle", "wb") as f:
      pickle.dump(sentences, f)
      f.close()

   # lendo do arquivo
   sentences = pickle.load(
      open("sentences.pickle", "rb")
   )

footnotes
---------

.. [1] stop words são as palavras sem valor semântico ao que pretendemos fazer, são palavras como "eu", "está", "era", "têm", etc. São palavras de uso tão comum e frequente que acabaria por ofuscar a presença de palavras mais relevantes no processo de classificação de textos por exemplo, afinal para saber o sentido de frases como "Alan Turing é o pai da ciência da computação" basta apenas as palavras \["Alan", "Turing", "pai", "ciência", "computação"\], isso é o que basta para uma máquina.

`teste <link://filename/listings/preprocessing.py>`_

.. raw:: html

    <div class="notebook">
        <a class="notebook-link" href="http://nbviewer.jupyter.org/github/demacdolincoln/anotacoes-nlp/blob/src/files/preprocessing.py">code</a>
    </div>