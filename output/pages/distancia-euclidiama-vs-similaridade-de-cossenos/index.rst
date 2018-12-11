.. title: Distância Euclidiama vs Similaridade de Cossenos
.. slug: distancia-euclidiama-vs-similaridade-de-cossenos
.. date: 2018-12-07 04:04:17 UTC-03:00
.. tags: utils
.. category:
.. link: 
.. description: 
.. type: text

Indo direto ao ponto a principal diferença entre os cálculos é que enquanto na distância euclidiana é como se fizéssemos uma medição com uma régua entre 2 pontos, na similaridade de cossenos analisamos a distância angular entre 2 pontos a partir da origem, isso ficará mais claro no gráfico perto do final desta anotação.

.. math::

    dist\_eucl = \sqrt{\sum{(a-b)^2}}
    
    cosine\_sim = \frac{\sqrt{\sum{a * b}}}{\sqrt{\sum{a^2}} * \sqrt{\sum{b^2}}}

Comparando resultados
---------------------

Primeiro vamos implementar cada cálculo e depois uma função que receba uma matriz, normalize os dados, e indike os "k" pontos mais próximos a alguma coordenada que a gente escolher. Como usaremos em outras anotações, escrevi mais linhas do que um código simples e didático deveria ter:

.. code-block:: python
    :number-lines:
    
    import numpy as np
    from scipy.spatial.distance import euclidean, cosine

    def norm(x):
        return x/np.sqrt(np.sum(np.square(x)))

    def knn(matrix, n=5, func="cos", **kw):
        data_norm, coord_norm = None, None

        if "coord" in kw.keys():
            data = np.concatenate((matrix, np.array([kw["coord"]])))
            ata_norm = norm(matrix)
            coord_norm = data_norm[-1, :]
        else:
            data_norm = norm(matrix)
            coord_norm = data_norm[kw["pos"]]

        res = []
        for i in data_norm:
            if func=="cos":
                res.append(cosine(coord_norm, i))
            else:
                res.append(euclidean(coord_norm, i))

        if func=="cos":
            return np.array(res).argsort()[1:n+1], sorted(res)[1:n+1]
        else:
            return np.array(res).argsort()[1:n+1], sorted(res)[1:n+1]


Visualizando a diferença de resultados entre as medições, gerei esse gráfico abaixo:

.. thumbnail:: /images/eucl_vs_cos.png
    :width: 500
    
explicando: os pontos vermelhos representam os pontos mais próximos desse ponto amarelo cortado por uma seta são os pontos mais próximos considerando a distância euclidiana, os pontos azuis é pela similaridade de cossenos e os roxos são os que as duas métricas coincidem ao listar os mais próximos, a seta indica a inclinação do ponto amarelo em relação a origem, e é isso que a similaridade de cossenos leva em consideração, perceba que um dos pontos azuis ficou bem distante mas projetando a seta vemos que se mantém mais próximo ao ângulo do ponto amarelo que o ponto vemelho.

O motivo de preferirmos usar a similaridade de cossenos a usar distância euclidiana ou outras métricas para medir distâncias é que quando trabalhamos com NLP e ainda mais quando fazemos uma redução de dimensionalidade (onde ficou claro que há rotação e distorção) os ângulos ficam mais bem preservados que as distâncias.

obs: no Gensim, a similaridade é calculada com 1 passo a mais do que o demonstrado aqui, a distância angular é dada por:


.. math::

    dist\_angular = \frac{cos^-1(cos\_similarity)}{\pi}

    angular\_similarity = 1-dist\_angular