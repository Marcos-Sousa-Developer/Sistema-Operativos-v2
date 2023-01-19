import struct,argparse

def save(ficheiro):

    #le o ficheiro e transforma em iso-8859-1 para leitura do usuario

    with open (ficheiro,"rb") as fileRead:

        for linha in fileRead.readlines():

            l = struct.unpack('{}s'.format(len(linha)),linha)[0]

            print()

            print(l.decode('iso-8859-1','replace'))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('ficheiro', default=None, nargs='?', type=str, help='opção que ppermite definir o ficheiro usado para guardar o histórico da execução do programa')

    argument = parser.parse_args()
    
    if argument.ficheiro == None:

        print('Não indicou o nome de um ficheiro')

        exit()

    else:

        save(argument.ficheiro)
