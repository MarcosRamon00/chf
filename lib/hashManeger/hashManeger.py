import lib.hashMaker.hashMaker as hashMaker
import lib.messages.messages as message


##=========funcoes

#gera hash do arquivo de acordo com o nome do hash informado  
def retornarHashArquivo(hashFile,file) -> str:
    """
        retorna hash do  file informado deacordo com o tipo de hash informado.
    """
    if hashFile == "sha256":
        return hashMaker.retornarHashSha256(file)
    elif hashFile == "sha512":
        return hashMaker.retornarHashSha512(file)
    else: #md5
        return hashMaker.retornarHashMd5(file)

#compara hashs do arquivo original e o hash informado
def comparar_hashs(originalHash,hashFile,isVerbose=False) -> None:
    """
        verifica se hashs informados sao iguais ou diferentes.
    """
    if isVerbose == False:
        if hashFile == originalHash:
            print("---hashs iguais [OK]")
        else:
            print("--hashs diferentes [!!!]")
    else:
        if hashFile == originalHash:
            print("com verbose")
        else:
            print("com verbose")