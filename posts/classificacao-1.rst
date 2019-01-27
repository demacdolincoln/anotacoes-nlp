.. title: Classificação 1
.. slug: classificacao-1
.. date: 2018-12-24 02:12:26 UTC-03:00
.. tags: 
.. category: classificação
.. link: 
.. description: 
.. type: text

O problema fundamental da classificação de textos reside no fato da dificuldade de representar o texto a nível numérico, ainda que o word2vec, o glove, o seq2seq sejam realmente úteis assim como vários outros algoritmos que não incluí aqui mas que são facilmente encontrados em buscas no google, eles por si só não conseguem ir além da representação semântica ou de alguma outra lógica sobre as palavras, tanto para gerar textos quanto para classificá-los precisamos do auxílio de outros algoritmos. O objetivo desta anotação é identificar os desafions inerentes a esta tarefa.

Apenas vocabulário
------------------

Esse seria o caminho mais óbvio, tendo em vista que temos uma representação espacial da disposição das palavras num hiperplano, então faz sentido imaginar que textos sobre diferentes assuntos necessariamente tem diferentes vocabulários. Façamos um teste:

1. peguei 2 textos da wikipedia: 

     a) `Lutefisk <https://pt.wikipedia.org/wiki/Lutefisk>`_ - um prato da culinária norueguesa
     b) `Erhu <https://pt.wikipedia.org/wiki/Erhu>`_ - um instrumento tradicional chinês

2. fiz o pré-processamento das palavras como já descrito em outro post, ficando apenas com o vocabulário
3. peguei as posições correspondentes a cada palavra no skip-gram já treinado
4. reduzi as dimensões e plotei o gráfico

.. image:: /images/classificacao_1_scatter_vec.png

**explicando as cores:**

.. vermelho: vocabulário do texto 1
.. ciano: vocabulário do texto 2
.. branco: vocabulário em comum a ambos

Como é possível perceber acima, não identificamos um nível de separação consistente entre os vocabulários, olhando a densidade de concentração do vocabulário nos dois textos, descartando as palavras em comum, temos a imagem abaixo:

.. image:: /images/classificacao_1_kde_vec.png

Os centros estão muito próximos, ou seja, mesmo identificando as regiões mais densas nos vocabulários, ao tentar usar esta região como métrica, a similaridade de sentido entre os termos para o texto 1 e para o texto 2 continuam muito próximas tornando essa estratégia bem ineficaz.

A solução está na compreensão que um texto não são apenas palavras soltas, mas o sentifo extrapola a simples junção de palavras, então a ordem do que está escrito importa, a disposição das palavras no texto importa muito.

Nas próximas anotações abordarei sobre o uso de redes convolucionais e redes neurais recorrentes, diferentes formas de tentar burlar as dificuldades aqui apresentadas.