.. title: GRU e LSTM
.. slug: gru-e-lstm
.. date: 2018-12-24 02:13:54 UTC-03:00
.. tags: 
.. category: utils
.. link: 
.. description: 
.. type: text


obs: Não vou me demorar tratando de questões teóricas sobre as RNN em si, já que o foco dessas anotações é NLP, futuramente, ao concluir essas anotações talvez eu inicie uma série mais abrangente sobre machine learning, mas por enquanto apenas traterei de assuntos teóricos relativos a NLP e ao resto apenas uma abordagem prática.

Parece meio óbvio dizer mas o que define uma rede neural recorrente é exatamente a recorrência, isto é, informações que são armazenadas e depois reutilizadas, a forma mais simples de implementação consiste em criar uma camada (um array) que armazena os resultados e é utilizado normalmente no processamento dos dados que passam por uma rede neural, só que com 1 caracérística distinta: haver uma condição ou não para atualizar esses dados aprendidos ao longo do treinamento e uma condição que a informação armazenada seja utilizada.

Devido a esse mecanismo ser claramente um gerenciamento de memória e estarmos tratando de redes neurais, não demora muito para começarmos a associar ao modo como nosso cérebro gerencia a memória, desta forma vem ao mundo em 1997 o LSTM (Long Short-Term Memory) [1]_ [2]_, e como o nome bem indica, se trata de gerenciamento de memória de curto e longo prazo, mas como ele faz isso?

Portões
-------

.. image:: https://upload.wikimedia.org/wikipedia/commons/3/3b/The_LSTM_cell.png

.. image:: https://upload.wikimedia.org/wikipedia/commons/3/37/Gated_Recurrent_Unit%2C_base_type.svg



Traduzindo as funções expostas na imagem acima disponível na wikipedia representando uma célula de memória LTSM:

.. math::

	\sigma = \frac{1}{1 + exp(-x)}

	tanh = \frac{e^x - e^-x}{e^x + e^{-x}}


.. image:: /images/lstm_gru-tanh-sigmoid.png

Vemos que a diferença entre os gráficos dessas funções é essencialmente o limite quando tende a menos infinito, e isso faz toda a diferença, pois um limite que tende a 0 significa que posteriormente qualquer número multiplicado por 0 será 0, neste caso a função sigmoide indica a relevância de cada dimensão de entrada, se a dimensão for próxima a zero, ela vai perdendo relevância até desaparecer ou ser substituída por outra informação mais relevante (decidida pela função tanh).

Todo o mecanismo de preservação e esquecimento desses métodos se baseia nesses "portões" que é como são chamadas as camadas com a função sigmoide, enquanto a função tanh tem o dever de fazer as escolhas finais, repare nas somas e multiplicações que unem o fluxo da saída com a camada oculta que armazena a memória, como a última estapa das operações com o estado da célula é sempre uma soma e os anteriores são multiplicações, isso revela a alteração dos pesos para definir a importância de cada dimensão e posteriormente a atualização mantendo assim para a época atual do treinamento da rede neural, a memória de curto prazo (os espaços próximos a zero que após a soma se mantém próximos aos resultados mais recentes) e a memória de longo prazo (o conteúdo mais relevante deixado mais próximo de 1)



---

artigos e links recomendados
----------------------------

.. [1] `Learning to Forget: Continual Prediction with LSTM ( Felix A. Gers , Jürgen Schmidhuber , Fred Cummins ) <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.55.5709>`

.. [2] `Long short-term memory (Sepp Hochreiter; Jürgen Schmidhuber) <https://www.researchgate.net/profile/Sepp_Hochreiter/publication/13853244_Long_Short-term_Memory/links/5700e75608aea6b7746a0624/Long-Short-term-Memory.pdf?origin=publication_detail>`

.. [3] `Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation ( Cho, Kyunghyun; van Merrienboer, Bart; Gulcehre, Caglar; Bahdanau, Dzmitry; Bougares, Fethi; Schwenk, Holger; Bengio, Yoshua) <https://arxiv.org/pdf/1406.1078v3.pdf>`