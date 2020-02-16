def verificaArquivo(arquivo):#verifica erro na abertura de arquivo
    """
        verifica se eh possivel utilizar o arquivo informado.
    """
    try:
        arq = open(arquivo,'rb')
        return arq
    except FileNotFoundError as erro:
        print("[ERRO]: ARQUIVO NÃO ENCONTRADO")
        print("ERRO:", erro)
        return False
    except Exception as erro:
        print("[ERRO]:  ARQUIVO NÃO PODE SER ABERTO ")
        print("ERRO:", erro)
        return False

