from memoria_cache import MemoriaCache  # Importa a classe MemoriaCache do módulo memoria_cache
from funcoes_auxiliares import carregar_arquivo, menu  # Importa as funções carregar_arquivo e menu do módulo funcoes_auxiliares

def main():
    simularMapeamento = None  # Inicializa a variável simularMapeamento como None

    while True:
        menu()  # Exibe o menu de opções
        choice = input("Escolha uma opção: ")
        if choice == "1":  # Se a escolha for 1, configurar a memória e cache
            nome_arquivo = input("Digite o nome do arquivo de entrada: ")  # Solicita o nome do arquivo de entrada
            configurar = carregar_arquivo(nome_arquivo)  # Carrega o arquivo e configura a memória e cache
            if configurar:  # Se a configuração for bem-sucedida
                simularMapeamento = MemoriaCache(*configurar)  # Cria uma instância da classe MemoriaCache passando os parâmetros carregados
                print("Arquivo de entrada lido com sucesso!")  # Informa que o arquivo foi lido com sucesso

                print("Informações sobre a memória principal: ")  # Exibe informações da memória principal
                print("Tamanho:", simularMapeamento.mpTamanho, "bytes")  # Exibe o tamanho da memória principal
                print("Tamanho do bloco:", simularMapeamento.blocosPalavras)  # Exibe o tamanho do bloco na memória principal
                print()
                print("Informações sobre a memória cache: ")  # Exibe informações da memória cache
                print("Tamanho:", simularMapeamento.cacheTamanho, "bytes")  # Exibe o tamanho da memória cache
                print("Linhas por conjunto:", simularMapeamento.conjuntoLinhas)  # Exibe o número de linhas por conjunto na cache
                print()
            else:
                print("Erro ao ler arquivo de entrada\n")  # Informa que houve um erro ao ler o arquivo
        elif choice == "2":  # Se a escolha for 2, acessar a memória principal
            if simularMapeamento is None:  # Verifica se a memória principal e cache foram configuradas
                print("Memória principal e cache ainda não foram configuradas. Selecione a opção 1 primeiro.")  # Informa que é necessário configurar primeiro
                continue  # Volta ao início do loop principal
            enderecoMP = input("Informe um endereço da MP em formato binário: ")  # Solicita um endereço da memória principal em formato binário
            simularMapeamento.acessos_memoria(enderecoMP)  # Acessa a memória principal com o endereço fornecido
            simularMapeamento.contador_acessos += 1  # Incrementa o contador de acessos à memória
            print()
        elif choice == "3":  # Se a escolha for 3, realizar simulação de acessos
            nome_arquivo = input("Digite o nome do arquivo com a sequência de endereços da MP: ")  # Solicita o nome do arquivo com a sequência de endereços
            try:
                with open(nome_arquivo, 'r') as arquivo:  # Abre o arquivo em modo de leitura
                    enderecosArquivo = [linha.strip() for linha in arquivo]  # Lê e limpa cada linha do arquivo, armazenando os endereços
                    for enderecoMP in enderecosArquivo:  # Itera sobre cada endereço no arquivo
                        if 0 <= int(enderecoMP, 2) < simularMapeamento.mpTamanho:  # Verifica se o endereço é válido
                            simularMapeamento.contador_acessos += 1  # Incrementa o contador de acessos
                            simularMapeamento.acessos_memoria(enderecoMP)  # Acessa a memória com o endereço fornecido
                        else:
                            print("Endereço informado inválido!")  # Informa que o endereço é inválido
                    simularMapeamento.exibirEstatisticas()  # Exibe as estatísticas da simulação
                    print()
            except FileNotFoundError:  # Se o arquivo não for encontrado
                print("O arquivo informado não foi encontrado.\n")  # Informa que o arquivo não foi encontrado
            except ValueError:  # Se houver valores inválidos no arquivo
                print("O arquivo está com endereços inválidos.\n")  # Informa que o arquivo contém endereços inválidos
        elif choice == "4":  # Se a escolha for 4, exibir informações
            if simularMapeamento is None:  # Verifica se a memória principal e cache foram configuradas
                print("Memória principal e cache ainda não foram configuradas. Selecione a opção 1 primeiro.")  # Informa que é necessário configurar primeiro
                continue  # Volta ao início do loop principal
            while True:
                sub_menu = input(
                    "Selecione a opção desejada:\n--- 1. Exibir memória principal ---\n--- 2. Exibir cache ---\n--- 3. Exibir estatísticas ---\n--- 4. Voltar ao menu principal ---\nOpção: ")  # Exibe o submenu e solicita uma opção

                if sub_menu == "1":  # Se a escolha for 1, exibir memória principal
                    simularMapeamento.exibirMP()  # Exibe a memória principal
                    print()
                elif sub_menu == "2":  # Se a escolha for 2, exibir cache
                    simularMapeamento.exibirCache()  # Exibe a cache
                    print()
                elif sub_menu == "3":  # Se a escolha for 3, exibir estatísticas
                    simularMapeamento.exibirEstatisticas()  # Exibe as estatísticas
                    print()
                elif sub_menu == "4":  # Se a escolha for 4, voltar ao menu principal
                    break  # Sai do loop do submenu
                else:
                    print("Opção inválida! Tente novamente.")  # Informa que a opção é inválida

        elif choice == "5":  # Se a escolha for 5, encerrar o programa
            print("Programa encerrado com sucesso.")  # Informa que o programa foi encerrado com sucesso
            break  # Sai do loop principal e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")  # Informa que a opção é inválida

if __name__ == "__main__":
    main()  # Chama a função main para iniciar o programa