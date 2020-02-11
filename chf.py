# pacotes/modulos de terceiros
from argparse import ArgumentParser

# pacotes criados para o programa
import lib.hashManeger.hashManeger as hashManeger
import lib.messages.messages as message
import lib.checkFile.checkFile as checkFile


#funcao principal
def main():
    """
        funcao principal do programa, checa o hash informado com o hash do file informado.
    """
    #parametros gerais do programa
    parser = ArgumentParser(
        prog='checkHashFile',
        description='software para verificar hash de file.',
        usage="python checkHashFile.py -ht <hash type> -f <file> -oh <orginal hash>"
    )

    #parametros essenciais para o programa
    parser.add_argument(
        '-ht','--hashType',
        action='store',
        type=str,
        help='tipo de hash',
        choices=['md5','sha256','sha512'],
        required=True,
        dest='hashType'
    )

    parser.add_argument(
        '-f','--file',
        action='store',
        type=str,
        help='localizacao do arquivo',
        required=True,
        dest='file'
    )

    parser.add_argument(
        '-oh','--originalHash',
        type=str,
        action='store',
        help='hash original para ser comparada',
        required=True,
        dest='originalHash'
    )
   
    args = parser.parse_args()
    if args.hashType != None:
        hashType = args.hashType
    if args.file != None:
        file = args.file 
    if args.originalHash != None:
        originalHash = args.originalHash
    
#verifica hash de arquivo
    dataFile = checkFile.verificaArquivo(file)#verifica file
    while dataFile == False:#pede file ate que seja valido
        file = str(input("arquivo para ser verificado: "))
        dataFile = checkFile.verificaArquivo(file)

    print("aguarde, verificando...")
    hashFile = hashManeger.retornarHashArquivo(hashType,dataFile)
    dataFile.close()
    hashManeger.comparar_hashs(originalHash,hashFile)
    
#execucao main
if (__name__ == "__main__"):
    message.showBanner()
    main()