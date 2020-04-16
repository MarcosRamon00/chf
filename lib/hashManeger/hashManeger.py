import lib.hashMaker.hashMaker as hashMaker
import lib.messages.messages as message


# #=========funcoes

# gera hash do arquivo de acordo com o nome do hash informado


def retornarHashArquivo(hashName, file, buffersize) -> str:
    """
        retorna hash do  file informado deacordo com o tipo de hash informado.
    """
    if hashName == "sha256":
        return hashMaker.retornarHashSha256(file, buffersize)
    elif hashName == "sha512":
        return hashMaker.retornarHashSha512(file, buffersize)
    elif hashName == "md5":
        return hashMaker.retornarHashMd5(file, buffersize)
    else:
        return None

# compara hashs do arquivo original e o hash informado


def comparar_hashs(originalHash, hashFile, isVerbose=False) -> None:
    """
        verifica se hashs informados sao iguais ou diferentes.
    """
    if originalHash == hashFile:
        hashsSaoIguais = True
    else:
        hashsSaoIguais = False

    message.infoComparacaohashs(hashsSaoIguais, originalHash, hashFile, isVerbose)

