import math  # Importa o módulo math do python para operações matemáticas
import random  # Importa o módulo random do python para gerar números aleatórios
from funcoes_exibicao import exibirEstatisticas, exibirMP, exibirCache  # Importa funções de exibição

class MemoriaCache:
    def __init__(self, tamanhoMP, blocosPalavras, tamanhoCache, conjuntoLinhas):
        # Validações de parâmetros de inicialização
        if not (0 < tamanhoMP <= 256):
            raise ValueError("Tamanho da MP deve ser entre 1 e 256 KB")
        if blocosPalavras not in [2, 4, 8]:
            raise ValueError("Quantidade de palavras por bloco deve ser 2, 4 ou 8")
        if not (0 < tamanhoCache <= 32):
            raise ValueError("Tamanho da cache deve ser entre 1 e 32 KB")
        max_linhas = (tamanhoCache * 1024 // (blocosPalavras * 4)) // 2
        if not (2 <= conjuntoLinhas <= max_linhas):
            raise ValueError(f"Número de linhas por conjunto deve ser entre 2 e {max_linhas}")

        # Inicialização dos atributos da classe
        self.mpTamanho = tamanhoMP * 1024  # Converte o tamanho da MP de KB para bytes
        self.blocosPalavras = blocosPalavras  # Define a quantidade de palavras por bloco
        self.cacheTamanho = tamanhoCache * 1024  # Converte o tamanho da cache de KB para bytes
        self.conjuntoLinhas = conjuntoLinhas  # Define o número de linhas por conjunto na cache
        self.tamanhoPalavra = 4  # Tamanho de cada palavra em bytes
        self.contador_acessos = 0  # Inicializa o contador de acessos à memória
        self.contadorHit = 0  # Inicializa o contador de hits na cache
        self.contadorMiss = 0  # Inicializa o contador de misses na cache
        self.substituicoes = 0  # Inicializa o contador de substituições na cache

        # Cálculo de diversos parâmetros
        self.tamanhoBloco = self.blocosPalavras * self.tamanhoPalavra  # Tamanho de cada bloco em bytes
        self.numeroBlocosMP = self.mpTamanho // self.tamanhoBloco  # Número total de blocos na memória principal
        self.numeroConjuntosCache = (self.cacheTamanho // self.tamanhoBloco) // self.conjuntoLinhas  # Número de conjuntos na cache
        self.deslocamento = int(math.log(self.blocosPalavras, 2))  # Bits de deslocamento
        self.indiceBits = int(math.log(self.numeroConjuntosCache, 2))  # Bits para o índice
        self.enderecoBits = int(math.log(self.mpTamanho // self.tamanhoPalavra, 2))  # Bits para o endereço
        self.tagBits = self.enderecoBits - self.indiceBits - self.deslocamento  # Bits para a tag

        # Inicialização da memória principal e cache
        self.memoriaPrincipal = [random.randint(0, 999) for _ in range(self.mpTamanho // self.tamanhoPalavra)]  # Memória principal com valores aleatórios
        self.cache = [[None for _ in range(self.conjuntoLinhas)] for _ in range(self.numeroConjuntosCache)]  # Estrutura da cache
        self.contadorUsos = [[0 for _ in range(self.conjuntoLinhas)] for _ in range(self.numeroConjuntosCache)]  # Contador de usos das linhas da cache

    def indices_cache(self, enderecoMP):
        enderecoMP = enderecoMP.zfill(self.enderecoBits)  # Preenche o endereço com zeros à esquerda até o tamanho total de bits do endereço
        indice = enderecoMP[-(self.deslocamento + self.indiceBits):-self.deslocamento]  # Extrai o índice do endereço
        tag = enderecoMP[:-(self.deslocamento + self.indiceBits)]  # Extrai a tag do endereço
        return int(indice, 2), int(tag, 2)  # Retorna o índice e a tag como inteiros

    def acessos_memoria(self, enderecoMP):
        enderecoMP = enderecoMP.zfill(self.enderecoBits)  # Preenche o endereço com zeros à esquerda até o tamanho total de bits do endereço
        definir_indice, tag = self.indices_cache(enderecoMP)  # Obtém o índice e a tag do endereço
        definir_cache = self.cache[definir_indice]  # Obtém o conjunto da cache correspondente ao índice

        for i in range(self.conjuntoLinhas):
            if definir_cache[i] is not None and definir_cache[i][0] == tag:  # Verifica se há um hit na cache
                self.contadorUsos[definir_indice][i] += 1  # Incrementa o contador de uso da linha
                self.contadorHit += 1  # Incrementa o contador de hits
                print(f"Hit: Endereço {enderecoMP} encontrado no conjunto de cache {definir_indice}, linha {i}.")
                return definir_cache[i][1]  # Retorna o dado encontrado na cache

        self.contadorMiss += 1  # Incrementa o contador de misses
        self.carregarCache(enderecoMP, definir_indice, tag)  # Carrega o dado da memória principal para a cache
        return self.memoriaPrincipal[int(enderecoMP, 2) // self.tamanhoPalavra]  # Retorna o dado da memória principal

    def carregarCache(self, enderecoMP, definir_indice, tag):
        definir_cache = self.cache[definir_indice]  # Obtém o conjunto da cache correspondente ao índice
        indice_minimo_uso = self.contadorUsos[definir_indice].index(min(self.contadorUsos[definir_indice]))  # Encontra a linha menos usada no conjunto

        if definir_cache[indice_minimo_uso] is None or definir_cache[indice_minimo_uso][0] != tag:  # Verifica se precisa substituir a linha na cache
            linhaSubstituida = definir_cache[indice_minimo_uso][0] if definir_cache[indice_minimo_uso] else None  # Guarda a tag da linha substituída, se houver
            definir_cache[indice_minimo_uso] = (tag, self.memoriaPrincipal[int(enderecoMP, 2) // self.tamanhoPalavra])  # Carrega o dado da memória principal para a cache
            self.contadorUsos[definir_indice][indice_minimo_uso] = 1  # Reseta o contador de uso da linha
            print(f"Miss: Carregou o endereço {enderecoMP} para a cache no conjunto {definir_indice}, linha {indice_minimo_uso}.")
            if linhaSubstituida is not None:
                self.substituicoes += 1  # Incrementa o contador de substituições
                print(f"Substituída a linha com tag {linhaSubstituida} no conjunto {definir_indice}, linha {indice_minimo_uso}.")
        else:
            self.contadorUsos[definir_indice][indice_minimo_uso] += 1  # Incrementa o contador de uso da linha
            print(f"Hit: Endereço {enderecoMP} encontrado na cache conjunto {definir_indice}, linha {indice_minimo_uso}.")

    # Métodos de exibição que chamam as funções importadas
    def exibirMP(self):
        exibirMP(self)

    def exibirCache(self):
        exibirCache(self)

    def exibirEstatisticas(self):
        exibirEstatisticas(self)
