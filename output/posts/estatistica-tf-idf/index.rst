.. title: Estatística: TF-IDF
.. slug: estatistica-tf-idf
.. date: 2018-12-07 01:47:59 UTC-03:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Antes da popularidade de métodos baseados em IA, muito também devido à capacidade dos computadores da época, o que restava para análises de texto era quantificar as palavras e buscar extrair estatísticas, o mais básico e fundamental talvez seja o TF-IDF e por isso este post.

Este método se resume a contar a frequência de uso de palavras e realizar um cálculo que gere uma estimativa de uso/importância da palavra no texto, ele se inpira na Lei de Zipf.

..

   Lei de Zipf:


Logicamente há inconsistências, afinal apenas a frequência não alcança o uso das palavras, não indica necessariamente as mais significativas se uma pessoa em vez de fazer referências a uma palavra ficar repetindo a mesma coisa o tempo todo. ex.:

"há filmes bons, ruins e medianos, mas o filme em questão é o pior de todos, o filme é tão chato e cansativo que todos dormem assistindo os primeiros minutos do filme"

"há filmes bons, ruins e medianos, mas este em questão é o pior de todos, tão chato e cansativo que todos dormem aos primeiros minutos"

É bem claro que apesar do sentido do texto ser o mesmo, a importância dada à palavra "filme" seria diferente. E de fato, o TF-IDF funciona melhor para textos que seguem as regras de coesão e coerência, então vamos usar publicações da wikipédia.

primeiro vamos fazer uma parte do processo mais manualmente e depois usando o sklearn

