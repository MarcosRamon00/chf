#!/usr/bin/env python
# pacotes/modulos de terceiros
from argparse import ArgumentParser

# pacotes criados para o programa
import lib.hashManeger.hashManeger as hashManeger
import lib.messages.messages as message
import lib.checkFile.checkFile as checkFile


# funcao principal


def main():
    """
        funcao principal do programa, checa o hash informado com o hash do file informado.
    """
# parametros gerais do programa
    parser = ArgumentParser(
        prog='chf',
        description='software para comparar hash de arquivo.',
        usage="""
            python3 chf.py <hash type> <file> <original hash>
        """
    )

# parametros essenciais para o programa
    parser.add_argument(
        'hashType',
        metavar='HT',
        type=str,
        help='tipo de hash',
        choices=['md5', 'sha256', 'sha512']
    )

    parser.add_argument(
        'file',
        metavar='F',
        type=str,
        help='localizacao do arquivo'
    )

    parser.add_argument(
        'originalHash',
        metavar='OH',
        type=str,
        help='hash original para ser comparada'
    )
   
# parametros opcionais
    parser.add_argument(
        '-v', '--verbose',
        required=False,
        help='mostra mais informacoes sobre a comparacao dos hashs',
        dest='isVerbose',
        action="store_true"
   )

    parser.add_argument(
        '-bs', '--buffersize',
        required=False,
        type=int,
        help='customizar tamanho do buffer de hash',
        dest='buffersize',
        action="store"
    )


# verificar se argumentos obrigatorios estao vazios
    args = parser.parse_args()
    
    if args.hashType:
        hashType = args.hashType
    
    if args.file:
        file = args.file
    
    if args.originalHash:
        originalHash = args.originalHash
    
    if args.buffersize:
        bufferSize = args.buffersize
    else:
        bufferSize = 65444

    if args.isVerbose:
        isVerbose = args.isVerbose
    else:
        isVerbose = False

# verifica hash de arquivo
    dataFile = checkFile.verificaArquivo(file) # verifica file
    while dataFile == False: # pede file ate que seja valido
        file = str(input("arquivo para ser verificado: "))
        dataFile = checkFile.verificaArquivo(file)

    message.verificando()
    hashFile = hashManeger.retornarHashArquivo(hashType, dataFile, bufferSize)
    dataFile.close()
    hashManeger.comparar_hashs(originalHash, hashFile, isVerbose)
  
# execucao main


if (__name__ == "__main__"):
    try:
        import colorama
        try:
            message.showBanner()
            main()
        except RuntimeError:
            print("nao foi possivel iniciar o programa")
    except ModuleNotFoundError as err:
        print("faltam pacotes:")
        print("pacotes: {0}".format(err))
        print("use: pip install -r requirements.txt")
        