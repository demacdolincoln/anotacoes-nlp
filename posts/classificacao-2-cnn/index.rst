.. title: Classificação 2: CNN
.. slug: classificacao-2-cnn
.. date: 2018-12-25 05:17:55 UTC-03:00
.. tags: classificação
.. category: cnn
.. link: 
.. description: 
.. type: text


Como falado `anteriormente <link://filename/posts/classificacao-1.rst>_`, classificar um texto é algo que vai além do vocabulário ainda que a gente utilize o word2vec ou o glove, e como a ordem das palavras importa muito, vamos dar aqui o 1º passo neste sentido, vamos ver como funciona uma rede neural convolucional (CNN) aplicada à classificação de textos.

Habitualmente elas são usadas essencialmente em processamento de imagens, a idéia é bastante simples: ter uma matriz maior e calcular uma matriz menor equivalente, neste processo há perda de dados e portanto é irreversível, porém tem se demonstrado muito útil em muitos casos.

Implementação:
--------------

O primeiro passo é transformar um texto numa matriz, para isso vamos recordar o que temos:

* texto ~> sequência de ids de palavras
* skip-gram, cbow, glove, etc. ~> representação cartesiana de palavras segundo o sentido compreendido pelo seu uso
 
Diante disso se torna meio lógico fazer uma matriz no formato `words x embedding dims`.

Um dos problemas dessa abordagem é que frases tem tamanhos variáveis enquanto a matriz de entrada na camada convolucional da CNN precisa ter tamanho fixo, então temos de lidar sempre com o pior caso, frases grandes, e preencher o espaço restante das frases menores com zeros, isso acaba nos obrigando ter um custo computacional extra já que teremos muitos espaços em branco só para que sempre tenhamos matrizes do mesmo tamanho.



---

Leituras recomendadas:
----------------------

https://arxiv.org/abs/1408.5882