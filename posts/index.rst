.. title: README
.. slug: index
.. date: 2018-12-06 02:46:15 UTC-03:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Pretendo fazer uma longa série de posts sobre NLP, não sou especialista nisso e podemos considerar os posts mais como anotações de estudo do que tutoriais ou manuais. O Índice abaixo será atualizado à medida que eu for publicando novos conteúdos, a idéia é seguir o andamento histórico de cada parte, na 1ª parte começaremos com o tf-idf para depois seguirmos para o word2vec e glove:


* parte 1: vetorização
    * `estatística: tf-idf <link://filename/posts/estatistica-tf-idf-e-lsa.rst>`_
    * `word2vec 1: introdução <link://filename/posts/word2vec-1-introducao.rst>`_
    * `word2vec 2: cbow <link://filename/posts/word2vec-2-cbow.rst>`_
    * `word2vec 3: skip-gram <link://filename/posts/word2vec-3-skip-gram.rst>`_
    * *glove*
    * `seq2seq: introdução <link://filename/posts/seq2seq-introducao.rst>`_
    * *notas finais e comparações entre métodos*

* parte 2: classificação
    * `Classificação 1: introdução <link://filename/posts/classificacao-1.rst>`_
    * `Classificacao 2: CNN <link//filename/posts/classificacao-2-cnn.rst>`_
    * `Classificação 3: RNN parte 1 <link//filename/posts/classificacao-3-rnn-parte-1.rst>`_
    * `Classificação 4: RNN parte 2 (+ convolução) <link//filename/posts/classificacao-4-rnn-parte-2-+-convolucao.rst>`_

* parte 3: modelagem
    * `resumos 0: pagerank <link://filename/posts/resumos-0-pagerank.rst>`_
    * `seq2seq: introdução <link://filename/posts/seq2seq-introducao.rst>`_
    * *seq2seq: implementação*

* utils
    * `Pré-processamento de textos <link://filename/posts/pre-processamento-de-textos.rst>`_. (*muito importante*)
    * `SVD vs PCA <link://filename/posts/svd-vs-pca.rst>`_
    * `distância euclidiana vs similaridade de cossenos <link://filename/posts/distancia-euclidiama-vs-similaridade-de-cossenos.rst>`_
    * `GRU e LSTM <link://filename/posts/gru-e-lstm.rst>`_

Obs1.: O pré-processamento é a etapa inicial de praticamente todos os conteúdos aqui escritos, é realmente muito importante, por isso antes de partir para qualquer outro conteúdo, leia ele primeiro.

Obs2.: O que estiver em itálico é que ainda não escrevi mas devo fazer ao longo dessas semanas.

obs3.: Com excessão da parte 1, usarei o cbow, skip-gram e glove já computados, fontes recomendadas:

* http://www.nilc.icmc.usp.br/nilc/index.php/repositorio-de-word-embeddings-do-nilc
* https://github.com/facebookresearch/fastText/blob/master/docs/crawl-vectors.md
* https://sites.google.com/site/rmyeid/projects/polyglot