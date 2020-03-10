import hashlib # usado para hash de file


#codigos usado para gerar hash do arquivo
#https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

##==========buffer 
def escolheBuffer(buffersize):
    if buffersize > 0:
        return buffersize
    else:
        BUFFERSIZE_DEFAULT =  65536 #64 kB
        return BUFFERSIZE_DEFAULT

##==========hashs
def retornarHashMd5(file,buffersize):#devolve hash md5 de file informado
    """
        retorna o hash md5 do file informado.
    """
    hashFile = hashlib.md5()
    while True:
        data = file.read(escolheBuffer(buffersize))
        if not data:
            break
        hashFile.update(data)
    return hashFile.hexdigest()

def retornarHashSha256(file,buffersize):#devolve hash sha256 de file informado
    """
        retorna o hash 256 do file informado.
    """
    hashFile = hashlib.sha256()
    while True:
        data = file.read(escolheBuffer(buffersize))
        if not data:
            break
        hashFile.update(data)
    return hashFile.hexdigest()

def retornarHashSha512(file,buffersize):#devolve hash sha512 de file informado
    """
        retorna o hash 512 do file informado.
    """
    hashFile = hashlib.sha512()
    while True:
        data = file.read(escolheBuffer(buffersize))
        if not data:
            break
        hashFile.update(data)
    return hashFile.hexdigest()
