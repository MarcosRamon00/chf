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
    from colorama import init,Fore,Back,Style

    init()
    if hashsSaoIguais:
        print(Fore.GREEN + '---> hashs iguais')
    else:
        print(Fore.RED + '---> hashs diferentes')

    if isVerbose:
        print(Fore.WHITE + "hash original  : {0}".format(originalHash))
        print(Fore.WHITE + "hash do arquivo: {0}".format(hashFile))

    print(Style.RESET_ALL)

def verificando() -> None:
    print("verificando ...")

