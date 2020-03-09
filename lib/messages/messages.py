def showBanner() -> None:
    """
        mostra um banner com o nome do programa.
    """
    print('''
       _               _    _   _           _    _____ _ _      
   ___| |__   ___  ___| | _| | | | __ _ ___| | _|  ___(_) | ___ 
  / __| '_ \\ / _ \\/ __| |/ / |_| |/ _` / __| |/ / |_  | | |/ _ \\
 | (__| | | |  __/ (__|   <|  _  | (_| \\__ \\   <|  _| | | |  __/
  \\___|_| |_|\\___|\\___|_|\\_\\_| |_|\\__,_|___/_|\\_\\_|   |_|_|\\___|
 ''')

def infoComparacaohashs(hashsSaoIguais,originalHash,hashFile,isVerbose=False) -> None:
    if hashsSaoIguais:
        print("---> hashs iguais")
    else:
        print("---> hashs diferentes")

    if isVerbose:
        print("hash original:",originalHash)
        print("hash do arquivo: ",hashFile)


def verificando() -> None:
    print("verificando ...")

