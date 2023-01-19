import argparse,sys,os,signal,time,re, math, struct
from multiprocessing import Process, Array, Value, Semaphore, Queue

from datetime import datetime


#Leitura do ficheiro, contém linhas vazias e ignora os '\n'
def lerFicheiro(fileName): 
    with open(fileName, 'r', encoding='utf-8') as fileRead:
        return list(map(lambda x: x.strip(), fileRead.readlines()))

#obtem o dicionário de palavra com valor, em que cada key[palavra], inicia com um valor 0
def get_dict(palavras):
    dictPalavras = dict()
    for word in palavras:
        dictPalavras[word] = 0
    return dictPalavras

#Construção da opção A
def optionA(fileRead,palavras,enable=False):

    searchResult = list()

    for linha_ficheiro in fileRead:
        containTrue = list()
        for palavra in palavras:
            if bool(re.findall(rf'\b{palavra}\b',linha_ficheiro)) == True: #caso a palavra exista na linha
                containTrue.append(True)
        if enable == False and len(containTrue) == 1: #caso apenas contenha uma unica palavra na linha, opção A inativa
            searchResult.append(linha_ficheiro)
        
        elif enable == True and len(containTrue) == len(palavras): #caso acontenha todas as palavra na linha, opção A ativa
            searchResult.append(linha_ficheiro)
    return searchResult


#Construção da opção C
def optionC(fileRead,palavras):

    dictPalavras = get_dict(palavras)

    for linha_ficheiro in fileRead:
        for word in palavras:
            if bool(re.findall(rf'\b{word}\b',linha_ficheiro)) == True: #caso a palavra exita na linha
                dictPalavras[word] += len(re.findall(rf'\b{word}\b',linha_ficheiro)) #key palavra recebe a soma de quantas vezes aparece na linha

    return dictPalavras

#Construção da opção L
def optionL(searchResult,palavras, aOptionEnable = False):

    if aOptionEnable == True:
        return len(searchResult) #caso a opção A esteja ativa retorna o tamanho da lista de resultado
    else:
        dictPalavras = get_dict(palavras)
        for linha in searchResult:
            for word in palavras:
                palavra = word.lower()
                if bool(re.findall(rf'\b{palavra}\b',linha.lower())) == True: #Conta a linha em que aparece a palavra
                    dictPalavras[word] += 1

    return dictPalavras


#Execução do comando
def pgrepwc(a,c,l,p,palavras,ficheiro,inicio,fim):

    searchResult = optionA(ficheiro,palavras,a) 
        
    if c == True:
        dictPalavrasC = optionC(ficheiro,palavras)
        imprime(ficheiro,dictPalavrasC,c,l,inicio,fim)
        atualiza(dictPalavrasC,palavras)
            

    if l == True:
        dictPalavrasL = optionL(searchResult,palavras, a) # pode ser um inteiro caso a opção a esteja ativa
        imprime(ficheiro,dictPalavrasL,c,l,inicio,fim)
        atualiza(dictPalavrasL,palavras)
    print()
        

def imprime(ficheiro,contentOption,c,l,inicio,fim):

    #pt = time.gmtime()

    global dia,mes,ano,horas,minutos,segundos,microsegundos,tamanho_ficheiros,one_file,lista_ultima_linha,flag
    
    # caso seja o processo pai
    if argument.p < 1:

        global historico

    #caso seja processos filho
    else:
    
        historico = q.get() #recebe historico do pai

    #obter a hora atual
    now = datetime.now()
    phoras = int(now.strftime("%H")) - horas
    pminutos = int(now.strftime("%M")) - minutos
    psegundos = int(now.strftime("%S")) - segundos
    pmicrosegundos = (float(now.strftime("%S.%f")) - int(now.strftime("%S")))

    #Caso lemos a primeira vez
    if leu.value == 0:
        print()
        
        historico.append("Início da execução da pesquisa: <"+str(dia)+"/"+str(mes)+"/"+str(ano)+","+str(horas)+":"+str(minutos)+":"+str(segundos)+":"+str(microsegundos)+">")
        print("Início da execução da pesquisa: <"+str(dia)+"/"+str(mes)+"/"+str(ano)+","+str(horas)+":"+str(minutos)+":"+str(segundos)+":"+str(microsegundos)+">")

        historico.append("\n")
        print()

        historico.append("Número de processos filhos: <" + str(argument.p) + ">")
        print("Número de processos filhos: <" + str(argument.p) + ">")

        historico.append("\n")
        print()

        #caso a opção esteja ativa ou inativa
        if argument.a == True:

            historico.append("Opção -a ativada: Sim ")
            print("Opção -a ativada: Sim ")

            historico.append("\n")
            print()
        else:
            historico.append("Opção -a ativada: Não ")
            print("Opção -a ativada: Não ")

            historico.append("\n")
            print()

        historico.append("Emissão de alarmes no intervalo de <" + str(argument.w) + "> segundos.")
        print("Emissão de alarmes no intervalo de <" + str(argument.w) + "> segundos.")

        historico.append("\n")
        
        print()

    #caso processo filho
    if argument.p > 0:

        if leu.value == 0:
            leu.value +=1 #garantir que apenas um filho le uma vez

            print("Uso de processos filho: Sim")

            print()
            
            
            print("Tamanho de cada ficheiro --> " + str(tamanho_ficheiros) + ", origina um unico ficheiro de tamanho --> " + str(len(one_file)))
                
            print()

            print("Ultima linha de cada ficheiro (linha 0 também conta) --> " + str(lista_ultima_linha[:]))

            print()

            print("Cada processo lê aproximadamente--> " + str(math.ceil(len(one_file)/argument.p)) + " linhas, sendo que o ultimo process lê o resto.")

            print()
    else:
        #garante que o pai le uma unica vez
        leu.value +=1

    #apresenta o processo uma unica vez
    if leu_buffer.value == 0:
        leu_buffer.value +=1
        
        historico.append("Processo: " + str(os.getpid()))
        print("Processo: " + str(os.getpid())) #obtem o processo corrente

        historico.append("\n")
        print()
        
        print("processo ->", process.value, ", intervalo ->", [inicio,fim])

        print()

    historico.append(" "*2 +"-> ficheiro: <" + argument.f[contador.value] + ">")
    print(" "*5 +"-> ficheiro: <" + argument.f[contador.value] + ">")

    historico.append("\n")
    print()
    
    historico.append(" "*5 +"-> tempo de pesquisa: <"+str(phoras)+":"+str(pminutos)+":"+str(psegundos)+":"+str(pmicrosegundos)+">")
    print(" "*5 +"-> tempo de pesquisa: <"+str(phoras)+":"+str(pminutos)+":"+str(psegundos)+":"+str(pmicrosegundos)+">")

    historico.append("\n")
    print()
    
    historico.append(" "*5 +"-> dimensão do ficheiro: <" + str(tamanho_ficheiros[contador.value]) + ">")
    print(" "*5 +"-> dimensão do ficheiro: <" + str(tamanho_ficheiros[contador.value]) + ">")

    historico.append("\n")
    print()
    print(" "*5 +"-> Leu " + str(len(ficheiro)) + " do ficheiro " + argument.f[contador.value])
    print()

    #caso a opção a inativa
    if type(contentOption) != int:     
        for chave in contentOption:
            if type(contentOption) == dict:
                if c == True: #caso opção c ativa
                    historico.append(" "*5 +"-> número de ocorrências da palavra " + str(chave) + ': ' + "<" + str(contentOption[chave]) + ">")
                    print(" "*5 +"-> número de ocorrências da palavra " + str(chave) + ': ' + "<" + str(contentOption[chave]) + ">")
                    historico.append("\n")
                    print()
                else: #caso a opção l ativa
                    historico.append(" "*5 +"-> número de linhas da palavra " + str(chave) + ': ' + "<"+ str(contentOption[chave]) + ">")
                    print(" "*5 +"-> número de linhas da palavra " + str(chave) + ': ' + "<"+ str(contentOption[chave]) + ">")
                    historico.append("\n")
                    print()
                

    else: #caso a opção ativa e opção ativa -l
        for palavra in argument.palavras:
            historico.append(" "*5 +"-> número de linhas da palavra " + str(palavra) + ': ' + "<"+ str(contentOption) + ">")
            print(" "*5 +"-> número de linhas da palavra " + str(palavra) + ': ' + "<"+ str(contentOption) + ">")

    historico.append("\n")
    print()

    #caso control+C ativa
    if flag == True:
        contador.value = len(argument.f)-1 #contador atinge o maximo

        if argument.p > 0:
            process.value = argument.p - 1 #processo corrente atinge o maximo

    #caso atingimos o limite, estamos no ultimo processo e ultimo ficheiro
    if (contador.value == len(argument.f)-1)  and (process.value == argument.p-1 or process.value == 0):

        fdate = datetime.now()
        fphoras = int(fdate.strftime("%H")) - horas
        fpminutos = int(fdate.strftime("%M")) - minutos
        fpsegundos = int(fdate.strftime("%S")) - segundos
        fpmicrosegundos = (float(fdate.strftime("%S.%f")) - int(fdate.strftime("%S")))

        #obtem a duração da execução
        historico.insert(2,"Duração da execução: <"+str(fphoras)+":"+str(fpminutos)+":"+str(fpsegundos)+":"+str(fpmicrosegundos)+">") #insere na segunda posição
        print("Duração da execução: <"+str(fphoras)+":"+str(fpminutos)+":"+str(fpsegundos)+":"+str(fpmicrosegundos)+">")

        ativador.value +=1 #indica que impressão terminou

        historico.insert(3,"\n") #insere uma tab 
        print()
        
    #caso processo pai
    if argument.p < 1:

        contador.value +=1 #conta ficheiro
        leu_buffer.value = 0 #indica que podemos ler o proximo processo
    #caso processo filho
    else:
        q.put(historico) #comunicação entre processos, partilha do historial
        
#atualiza array
def atualiza(contentOption,palavras):

    if type(contentOption) == dict: # caso seja do tipo dicionario

        for i in range(len(palavras)):

            myArray[i] += contentOption[palavras[i]] #cada posicao do array recebe total linhas ou ocorrencias obtidas
    #caso do tipo int
    else:
        myArray[0] += contentOption #linhas igual para todas as palavras

#obtem processo corrente
def get_process():

    process.value +=1  

#divisao de ficheiros
def divisonTask():

    global one_file,flag

    if flag != True: #caso control c inativo

        #divisao do ficheiro unico em partes iguais aproximadamente
        inicio = math.ceil(( process.value * len(one_file)) / argument.p)

        fim = math.ceil(((process.value + 1) * len(one_file)) / argument.p)
                    
        conjunto = one_file[inicio:fim] #particao de uma parte do unico ficheiro pelo processo corrente
        
        conteudo = [] #lista de linhas que o processo ira ler do ficheiro unico

        linha_final = lista_ultima_linha[contador.value] #linha final do ficheiro corrente

        ficheiro_atual = argument.f[contador.value] #ficheiro atual correspondente a particao
        
        for l in conjunto:
                
            conteudo.append(l)

            if conta_linha.value == linha_final: # caso chegamos a ultima linha do ficheiro corrente
                
                pgrepwc(argument.a,argument.c,argument.l,argument.p,argument.palavras,conteudo,inicio,fim) #executa

                conteudo = [] #limpa lisa de linhas

                if linha_final == lista_ultima_linha[len(lista_ultima_linha)-1]: #evitar erro de index out of range
                    break

                if flag != True: #caso a opção control c  esteja ativa, de modo evitar a contabilização e dar erro
                    contador.value +=1

                linha_final = lista_ultima_linha[contador.value] #linha final corrente
                ficheiro_atual = argument.f[contador.value] #ficheiro corrente

            elif conta_linha.value == fim-1: #caso fim das linhas destinadas ao processo
                pgrepwc(argument.a,argument.c,argument.l,argument.p,argument.palavras,conteudo,inicio,fim) #executa

            conta_linha.value +=1 #conta numero de linhas lidas
        get_process() #obtem o processo corrente
        leu_buffer.value = 0 #indica que pode ler o proximo processo
    ocupado.release() #passa a estar livre para o proximo processo
    

#caso control c ativa
def controlC(sig,NULL):

    print()
    signal.setitimer(signal.ITIMER_REAL, 0.5,0)
    global flag

    flag = True #flag ativa
    
    sig = None #impedi sinal de dar exit

#ativao do alarm
def alarm(sig,NULL):
    estado() #executa o estado atual

#estado atual do programa
def estado():

    print()

    print("-" * 30 + " ATUALIZAÇÃO " + "-"*30)

    print()

    global start

    list_processados = []
    total_linhas = 0

    if argument.a == True and argument.l == True:
        print('--> O número total de linhas da pesquisa até ao momento: ' + str(myArray[0]))

    else:
        for i in range(len(argument.palavras)):

            if argument.c == True:
                print('--> A palavra ' + argument.palavras[i] + ' teve um número total de ocorrências até agora igual a: ' + str(myArray[i])) #total de ocorrencias ate ao momento
            else:
                total_linhas += myArray[i] #total linhas ate ao momento
            
    if argument.l == True:

        print('--> O número de linhas resultantes da pesquisa até agora: ' + str(total_linhas))

    for i in range(argument.p):

        if i < contador.value:

            list_processados.append(argument.f[i]) #verifica os ficheiros completamente processados ate agora

    if len(list_processados) == 0:
        
        print('--> Nenhum ficheiro completamente processado ainda') #caso nenhum processado
    else:
        #caso final do programa ativado pelo control c
        if ativador.value != 1:
            print('--> Ficheiro completamente processado: ' + str(list_processados + [argument.f[contador.value]]))
            print('--> Ficheiro em processamento: Nenhum'  )
        else:
            print('--> Ficheiro completamente processado: ' + str(list_processados))
            print('--> Ficheiro em processamento: ' + str(argument.f[contador.value]))
        

    print('--> Tempo decorrido: ' + str((time.time() - start)*1000000) + " em microssegundos.") #obtem tempo decorrido

    print()

    print("-" * 30 + "-"*15 + "-"*30)

    print()
        
#guarda historico no ficheiro binario
def save():

    global historico

    with open (argument.o,"wb") as outFile:

        for linha in historico:
            
            outFile.write(struct.pack('{}s'.format(len(linha)),linha.encode('iso-8859-1'))) #escreve em binario 'iso-8859-1'

    
#imprime o resultado final       
def final():

    print('Resultado Final: ')
    print()

    if argument.a == True and argument.l == True:
        print('O número de linhas da pesquisa no total é: ' + str(myArray[0]))
    else:
        
        for i in range(len(argument.palavras)):

            if argument.c == True:
                    print('A palavra ' + argument.palavras[i] + ' teve um número total de ocorrências igual a: ' + str(myArray[i]))

            else:
                    print('A palavra ' + argument.palavras[i] + ' teve um número total de linhas encontradas de acordo com a opção -a ' \
                          + str(argument.a) + ' igual a: ' + str(myArray[i]))
    print()


if __name__ == '__main__':

    start = time.time()

    date = datetime.now()

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', required=False, action='store_true', help='Define se o resultado da pesquisa, caso ativo: são as linhas de texto que \
                                                                         contêm unicamente uma das palavras, caso inativo: todas as palavras ')

    parser.add_argument('-c', required=False, action='store_true', help='Opção que permite obter o número de ocorrências \
                                                                         encontradas das palavras a pesquisar')
                                                    
    parser.add_argument('-l', required=False, action='store_true', help= 'Opção que permite obter o número de linhas devolvidas da pesquisa,a. \
                                                                          Caso a opção -a não esteja ativa, o número de linhas devolvido é por palavra')
    
    parser.add_argument('-p', required=False, default=0, type=int, help='opção que permite definir o nível de paralelização, número de processos \
                                                                         (filhos)/threads que são utilizados para efetuar as pesquisas e contagens')

    parser.add_argument('-w', required=False, default=0, nargs='?', type=float, help='opção que permite definir o intervalo de tempo (dado pelo argumento s) em que o processo pai \
                                                                                      escreve para stdout o estado da contagem até ao momento.')

    parser.add_argument('-o', required=False, default=None, nargs='?', type=str, help='opção que ppermite definir o ficheiro usado para guardar o histórico da execução do programa')
    
    parser.add_argument('palavras', nargs='+',help='Palavras a procurar' )

    parser.add_argument('-f',required=False, nargs='*', default = [], help='Ficheiros a serem lidos')

    argument = parser.parse_args()

    lista = sys.argv

    myArray =  Array('i',len(argument.palavras))

    if len(argument.palavras) > 3:

        print('Não pode ser mais de 3 palavras') 

    if len(argument.f) == 0:
        filesList = list()
        while len(filesList) == 0:
            print('Não colocou os ficheiros a vereficar. Quais os ficheiros que quer ler? ')
            filesList += input().split()
        argument.f = filesList

    if argument.w < 0:
        print('Não existe intervalos negativos')
        exit()
        
    if argument.c == True and argument.l == True: 
        print('Não é possivel usar a opção -c em conjunto com -l')
        exit()

    elif argument.c == False and argument.l == False:
        print('Opção -c ou -l tem de estar ativa')
        exit()
    
    else:
        historico = list()

        q = Queue() #comunicação entre processos

        ativador = Value("i",1) #verifcador do control c ativado no imprime
        
        leu = Value("i",0) #verificador de leitura uma unica vez no imprime
    
        leu_buffer = Value("i",0) #verificador de ler uma unica vez o processo corrente no imprime

        contador = Value('i',0) #contador de ficheiro e linha final atual

        tamanho_ficheiros = [] #lista do tamanho de cada ficheiro

        process = Value("i",0) #process atual
        
        dia = int(date.strftime("%d"))
        mes = int(date.strftime("%m"))
        ano = int(date.strftime("%Y"))
        horas = int(date.strftime("%H"))
        minutos = int(date.strftime("%M"))
        segundos = int(date.strftime("%S"))
        microsegundos = (float(date.strftime("%S.%f")) - int(date.strftime("%S")))

        signal.signal(signal.SIGINT, controlC) #siganl de control c

        flag = False #flag caso ativado pelo control c

        #temporizador ativado caso -w diferente de 0        
        if argument.w != 0:
            signal.signal(signal.SIGALRM, alarm)
            signal.setitimer(signal.ITIMER_REAL, 0.5,argument.w)
        
        if argument.p > 0:

            one_file, lista_ultima_linha , count = [], Array('i',len(argument.f)), 0

            #ujunção de todos os ficheiros num unico
            for fileName in argument.f:
                ficheiro = lerFicheiro(fileName)

                tamanho_ficheiros.append(len(ficheiro))
                
                one_file += ficheiro
                
                lista_ultima_linha[count] = len(one_file)-1

                count +=1

            #conta linha
            conta_linha = Value('i',0)

            #lista de jobs
            jobs = list()

            #lista de processados
            processados = Array("i",argument.p)

            #semaforo
            ocupado = Semaphore(1)
               
            for i in range(argument.p):

                newJ = Process(target=divisonTask)
                jobs.append(newJ)

            for job in jobs:
                #enquanto control c nãoa tivado
                if flag == False:
                    ocupado.acquire()
                    job.start()

                    q.put(historico) #comunicao entre processos enviar historico

                    time.sleep(0.5) #garante que há comunicação entre o processo filho e pai

                    historico = q.get() #comunicao entre processos enviar historico
                else:
                    signal.setitimer(signal.ITIMER_REAL, 0.5,0) #termina o alarm() com o control c
                    break

            for job in jobs:
                #enquanto control c nãoa tivado
                if flag == False:
                    job.join()
                else:
                    signal.setitimer(signal.ITIMER_REAL, 0.5,0) #termina o alarm() com o control c
                    break
                                             
                        
        else:
            #caso processo pai
            for ficheiro in argument.f:
                fileRead = lerFicheiro(ficheiro)
                tamanho_ficheiros.append(len(fileRead))
                if flag == False:
                    #pai le todos os ficheiros um a um sem junção num unico
                    pgrepwc(argument.a,argument.c,argument.l,argument.p,argument.palavras,fileRead,0,len(fileRead))
                else:
                    signal.setitimer(signal.ITIMER_REAL, 0.7,0)
                    break

                    
        #impressão final
        final()

        #caso argument.o ativo
        if argument.o != None:
            save()
            print("Histórico guardado no ficheiro " + argument.o)
             