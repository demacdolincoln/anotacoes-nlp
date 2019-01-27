.. title: Seq2Seq - Introdução
.. slug: seq2seq-introducao
.. date: 2018-12-24 02:13:03 UTC-03:00
.. tags: modelagem
.. category: seq2seq
.. link: 
.. description: 
.. type: text

Tenho certeza que todos ao menos uma vez se perguntaram, pelo menos nas primeiras vezes que usaram o google translate, "como é que isso funciona? é magica?", até mesmo pelo que escrevi aqui até agora, todos os conteúdos estão bastante distantes de algo que trate tão intensamente com linguagem do que o desta anotação. O seq2seq nos permite criar redes que aprendam a sequência em que as palavras estão dispostas num texto de modo que fique fácil gerar textos, por hora, para simplificar esse assunto bastante extendo, traterei aqui apenas de explicar cada passo praticamente sem o código e na próxima anotação terá uma implementação completa.

encoder - decoder
-----------------

O grande "truque" está no mecanismo de codificação-decodificação, na prática são 2 redes neurais recorrentes bem simples que compartilham uma mesma camada oculta e não tem camada de ativação, só uma célula `GRU ou LSTM <link://filename/posts/gru-e-lstm.rst>`_ que realiza o processamento.

A informação que dá sentido à ambas as redes é a camada oculta, é sobre ela que incide o treinamento, portanto essa é a camada responsável por fazer a relação entre as saídas de cada rede neural.

Então o que temos até o momento é:

* encoder:

    - hidden layer
    - gru

* decoder:

    - hidden layer
    - gru

Treinamento
-----------

Como já disse que tudo está em torno da camada oculta compartilhada, é criando este array que se inicia o treinamento, que incide mais sobre a camada de decodificação que sobre a de encodificação, é feito desse modo pela camada de decodificação ser a usada para calcular a perda já que é ela que nos fornecerá a saída final do algoritmo.

Procedimento:

* hidden layer
* encoder_output, hidden_layer = encoder(input, hidden_layer)
* decoder_output, hidden_layer = decoder(encoder_output, hidden_layer)
* loss(decoder_output, target)
* backward
* step

Na próxima anotação sobre o seq2seq, diante do código, tudo ficará mais claro.

Resolvi não colocar imagens ilustrativas aqui pois no 1º link das leituras recomendadas há um monte de animações explicando bem detalhadamente todo o processo, das 2 leituras recomendadas, essa é a que mais recomendo.

---

leituras recomendadas
---------------------

* http://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/
* https://google.github.io/seq2seq/

