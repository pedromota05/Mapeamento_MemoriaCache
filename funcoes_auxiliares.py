def carregar_arquivo(nome_arquivo): # Função para ler o arquivo txt de entrada
    try:
        with open(nome_arquivo, 'r') as arquivo:  # Abre o arquivo em modo de leitura
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            tamanhoMP = int(linhas[0].strip())  # Converte a primeira linha para inteiro, representando o tamanho da memória principal
            blocosPalavras = int(linhas[1].strip())  # Converte a segunda linha para inteiro, representando o número de blocos de palavras
            tamanhoCache = int(linhas[2].strip())  # Converte a terceira linha para inteiro, representando o tamanho da cache
            conjuntoLinhas = int(linhas[3].strip())  # Converte a quarta linha para inteiro, representando o número de linhas por conjunto
            return tamanhoMP, blocosPalavras, tamanhoCache, conjuntoLinhas  # Retorna os valores lidos e convertidos
    except Exception as e:  # Captura exceção caso ocorra erro de conversão dos valores
        print(f"Erro ao ler o arquivo de configuração! Motivo do erro: {e}")  # Imprime mensagem de erro
        return None  # Retorna None indicando falha na leitura do arquivo

def menu():
    # Imprime o menu de opções para o usuário
    print("Menu: ")
    print("1. Ler o nome de um arquivo de entrada que contenha as informações necessárias")
    print("2. Informar um endereço de MP binário válido para acesso à MP")
    print("-- OU --")
    print("3. Ler o nome de um arquivo que contenha uma sequência de endereços de MP")
    print("4. Exibir estatísticas, Memória Principal ou Memória Cache")
    print("5. Encerrar o programa")
