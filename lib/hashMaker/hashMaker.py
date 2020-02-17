import hashlib # usado para hash de file


##==========constantes
global BUF_SIZE
BUF_SIZE = 65536 #64Kb
##==========hashs
def retornarHashMd5(file):#devolve hash md5 de file informado
    """
        retorna o hash md5 do file informado.
    """
    hashFile = hashlib.md5()
    while True:
        data = file.read(BUF_SIZE)
        if not data:
            break
        hashFile.update(data)
    return hashFile.hexdigest()

def retornarHashSha256(file):#devolve hash sha256 de file informado
    """
        retorna o hash 256 do file informado.
    """
    hashFile = hashlib.sha256()
    while True:
        data = file.read(BUF_SIZE)
        if not data:
            break
        hashFile.update(data)
    return hashFile.hexdigest()

def retornarHashSha512(file):#devolve hash sha512 de file informado
    """
        retorna o hash 512 do file informado.
    """
    hashFile = hashlib.sha512()
    while True:
        data = file.read(BUF_SIZE)
        if not data:
            break
        hashFile.update(data)
    return hashFile.hexdigest()
