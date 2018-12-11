.. title: Estatística: TF-IDF e LSA
.. slug: estatistica-tf-idf-e-lsa
.. date: 2018-12-07 01:47:59 UTC-03:00
.. tags: utils
.. category: vetorização
.. link: 
.. description: 
.. type: text

Antes da popularidade de métodos baseados em IA, muito também devido à capacidade dos computadores da época, o que restava para análises de texto era quantificar as palavras e buscar extrair estatísticas, o mais básico e fundamental talvez seja o TF-IDF e por isso este post.

:tf-idf: *frequency-inverse document frequency*

Este método se resume a contar a frequência de uso de palavras e realizar um cálculo que gere uma estimativa de uso/importância da palavra no texto, de certa forma ele se conecta à `Lei de Zipf <https://en.wikipedia.org/wiki/Zipf%27s_law>`_ que trata justamente de uma análise da frequência de palavras.

.. math::

    TF(t) = \frac{nº\ de\ vezes\ que\ t\ aparece\ no\ texto}{total\ de\ termos\ no\ texto}
    
    IDF(t) = log_e(\frac{quantidade\ total\ de\ textos}{numero\ de\ textos\ em\ que\ t\ aparece})

Recomendo bastante a wikipédia em inglês, há bastante exemplos de cálculos variantes: https://en.wikipedia.org/wiki/Tf%E2%80%93idf

Logicamente há inconsistências, afinal apenas a frequência não alcança o uso das palavras, não indica necessariamente as mais significativas se uma pessoa em vez de fazer referências a uma palavra ficar repetindo a mesma coisa o tempo todo. ex.:

.. 

    "há filmes bons, ruins e medianos, mas o filme em questão é o pior de todos, o filme é tão chato e cansativo que todos dormem assistindo os primeiros minutos do filme"

    "há filmes bons, ruins e medianos, mas este em questão é o pior de todos, tão chato e cansativo que todos dormem aos primeiros minutos"

É bem claro que apesar do sentido do texto ser o mesmo, a importância dada à palavra "filme" seria diferente. E de fato, o TF-IDF funciona melhor para textos que seguem as regras de coesão e coerência, então vamos usar publicações da wikipédia.

Apesar do cálculo ser bastante simples, vou preferir usar o sklearn pois neste caso o mais importante é ter uma ideia geral sobre um recurso básico e servir como uma introdução básica sobre NLP, especialmente sobre vertorização de textos

TF-IDF
------

Como quase tudo no sklearn...

.. code-block:: python
    :number-lines:
    
    import wikipedia
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    stopw = stopwords.words("portuguese") +\
            stopwords.words("english")
    
    wikipedia.set_lang("pt")
    text = wikipedia.page("Alan_Turing").content

    tfidf = TfidfVectorizer(stop_words=stopw)

    X = tfidf.fit_transform(text.splitlines())
    X.shape
    
Na penúltima linha usei o `splitlines` para dividir o texto em parágrafos, assim podemos posteriormente coletar informações sobre os termos relevantes para cada parágrafo, mas admito esta forma ser demasiadamente simplista pois neste caso acabo considerando subtítulos como parágrafos.

Internamente, o objeto que criamos, durante o treinamento, armazena um dicionário com as palavras e um "id", vamos usar isso para converter os termos:

.. code-block:: python
    
    >>> X
    <61x664 sparse matrix of type '<class 'numpy.float64'>'
	with 862 stored elements in Compressed Sparse Row format>
    
A matriz esparsa tem diversas vantagens quando tratamos com longos arrays rechados de zeros, talvez o produto principal nessa implementação seja exatamente essa matriz que indica em cada parágrafo quais os termos presentes e a sua frequência, que é o ponto principal do TF-IDF.

.. image:: /images/lsa.png
    :alt: visualização da matriz resultante

E é exatamente sobre essa matriz que chegamos no LSA (Latent Semantic Analysis), mas antes vamos ver quais as palavras mais relevantes do primeiro parágrafo:

.. code-block:: python
    
    >>> ft_name = tfidf.get_feature_names()
    >>> top_tfidf = X[0].transpose().toarray().argsort(axis=0)[::-1]
    >>> for i in top_tfidf[:10]:
            print(ft_name[i[0]])
            
    computação
    cheshire
    junho
    ciência
    influente
    algoritmo
    east
    lógico
    desenvolvimento
    desempenhando

O ft_name é a lista de termos que irá converter para string a posição do termo indicada quando ordenamos o array comtendo o valor calculado para cada termo devolvendo as respectivas posições.

LSA
---

O LSA é nada mais que usar o `SVD <link://filename/posts/svd-vs-pca.rst>`_ mas em vez de diminuir as dimensões vamos manter o tamanho da matriz:

.. code-block:: python

    >>> X.shape
    (61, 664)
    
    >>> lsa = TruncatedSVD(n_components=61, n_iter=1000)
    >>> lsa.fit(X)
    TruncatedSVD(algorithm='randomized', n_components=61, n_iter=1000,
       random_state=None, tol=0.0)

O real poder do LSA vem desse tratamento dado à matriz formada a partir do TF-IDF, o código abaixo indica as palavras mais relevantes para cada parágrafo:

.. code-block:: python

    for i, comp in enumerate(lsa.components_):
        terms_in_comp = zip(ft_name, comp)
        sorted_terms = sorted(terms_in_comp,
                              key=lambda x: x[1], reverse=True)[:10]

        print(f"paragrafo: {i}")
        for t in sorted_terms:
            print(t[0])
        print("-"*20)
        
Pegando apenas o parágrafo 0, o resultado que temos é:

:paragrafo 0:
    * turing
    * máquina
    * alan
    * prêmio
    * memorial
    * guerra
    * enigma
    * bletchley
    * park
    * computação
    
off-topic
---------

1. E para gerar estatísticas de relevância de um texto inteiro, basta não dividir em parágrafos

2. E para gerarmos aquele bag of words que está na moda temos algumas opções, dependendo do caso aplicamos só o **TF** para gerar um ranking, para outros casos o **TF-IDF** funciona melhor, especialmente quando juntamos vários textos como uma análise geral de várias páginas de blogs, o LSA tende a ser melhor em usos mais específicos porém nada impede de usa-lo para gerar o ranking de termos para um livro, por exemplo.

.. raw:: html

    <div class="notebook">
        <a class="notebook-link" href="http://nbviewer.jupyter.org/github/demacdolincoln/anotacoes-nlp/blob/src/files/estatistica-tf-idf-e-lsa.ipynb">code</a>
    </div>
