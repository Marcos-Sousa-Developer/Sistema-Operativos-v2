<p align="center">
    <img src="https://e7.pngegg.com/pngimages/986/627/png-clipart-computer-icons-system-integration-others-miscellaneous-business-process.png" alt="Logo" width="80" height="80">
</p>

# <h1 align="center">Pesquisa as linhas dos ficheiros</h3>
<h4 align="center">Projeto para a cadeira de Sistemas Operativos (Parte1) (2021/2022)</h5>

<hr>

# Objetivo
Continuação da realização do trabalho de programação em Python envolvendo a sincronização de processos, a manipulação de ficheiros e o tratamento de sinais, tempo e alarmes.

<hr>

# Instruções  

Este trabalho pretende estender o comando pgrepwc (versão desenvolvida com processos, na 1ª Fase trabalho de projeto de avaliação) com algumas funcionalidades adicionais. 
Para aceder a 1ªFase, <a href="https://github.com/Marcos-Sousa-Developer/Sistema_Operativos_v1"> clique aqui!</a>

A pesquisa das palavras nesta fase do projeto é case-sensitive, ou seja, o resultado da pesquisa deve ser o mais
restrito e preciso de acordo com as palavras a pesquisar. Por exemplo, se queremos pesquisar a palavra “sistemas”,
as linhas devolvidas e ocorrências contabilizadas são todas as que contêm a palavra “sistemas”, e não “Sistemas”
ou qualquer outra variante case-insensitive da palavra (ex., SisTemaS). No entanto, mantem-se os resultados com
caracteres especiais que antecedem ou precedem a palavra (ex., sistemas!). 

Caso o número de processos definidos por n, pela opção -p, seja maior do que o número de ficheiros a
processar, o programa terá de dividir o conteúdo dos ficheiros pelos processos e sincronizar os processos ao acesso
aos ficheiros, quando, por exemplo, dois processos estão a processar um mesmo ficheiro. Por exemplo, se o n for
igual a 3 e o número de ficheiros for igual a 5 (f1 a f5), uma possível distribuição dos ficheiros pelos processos
será a seguinte: o 1º processo processa 2 ficheiros (f1 e f2); o 2º processo processa o ficheiro f3 e metade do
ficheiro f4; o 3º processo processa a outra metade do ficheiro f4 e o ficheiro f5. O algoritmo de distribuição dos
ficheiros pelos processos é da responsabilidade do grupo de trabalho. A distribuição dos ficheiros (ou conteúdo 
destes) pelos processos deverá ser a mais equitativa possível. 

Caso o processo pai receba o sinal SIGINT (i.e., CTRL+C), o processamento dos ficheiros deve terminar
corretamente, isto é, os processos devem concluir o processamento nos ficheiros correntes e terminar de seguida.
Por seu turno, o processo pai escreve para stdout o número de ocorrências encontradas de cada a palavra a pesquisar
ou o número de linhas onde cada palavra foi encontrada até ao momento, considerando apenas os ficheiros que
foram processados pelos processos. 


* **-w**: a opção é opcional e permite definir o intervalo de tempo (dado pelo argumento s) em que o processo pai
escreve para stdout o estado da contagem até ao momento, com a seguinte informação: (1) número de ocorrências
de cada palavra ou número de linhas resultantes da pesquisa (independentemente se a opção -a está ativa ou não);
(2) número de ficheiros completamente processados; (3) número de ficheiros em processamento; (4) tempo
decorrido desde o início da execução do programa (em micro-segundos).

* **-o**: a opção o é opcional e permite definir o ficheiro usado para guardar o histórico da execução do programa. O
conteúdo do ficheiro file deve ser armazenado em binário. A informação guardada neste ficheiro deve ser a que é
necessária para a execução do comando hpgrepwc.

Todas os acessos a zonas de memória partilhada, tanto para escrita como para leitura, terão de ser devidamente
sincronizados para evitar erros e outputs inesperados. Assim, os acessos por vários processos ao mesmo ficheiro,
bem como os acessos a buffers partilhados entre o processo pai e os processos filhos terão de ser sincronizados.


#### *Run it on terminal** 
```bash
python3 pgrepwc.py [-a] [-c|-l] [-p n] [-w s] [-o file] {palavras} [-f ficheiros]
```

##### Adicionalmente

* **hpgrepwc**: Lê o histórico de uma execução do programa pgrepwc guardada em file

###### *Run it on terminal** 
```bash
python3 hpgrepwc.py file
```

