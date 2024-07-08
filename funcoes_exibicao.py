def exibirMP(self): # Função que exibe o conteúdo da memória principal (MP) em blocos
    print("\nMemória Principal: ")
    # Itera sobre cada bloco de memória principal
    for i in range(self.numeroBlocosMP):
        enderecoInicial = i * self.blocosPalavras  # Calcula o endereço inicial do bloco
        dadosBloco = self.memoriaPrincipal[enderecoInicial:enderecoInicial + self.blocosPalavras]  # Obtém os dados do bloco
        # Imprime o bloco em formato binário
        print(f"Bloco {i}: {' '.join(format(palavra, '08b') for palavra in dadosBloco)}")

def exibirCache(self): # Função que exibe o conteúdo da memória cache.
    print("Memória Cache: ")
    # Itera sobre cada conjunto na cache
    for i, definir_cache in enumerate(self.cache):
        print(f"Conjunto {i}: ")
        # Itera sobre cada linha no conjunto
        for j, linha in enumerate(definir_cache):
            if linha is not None:
                # Imprime a tag e os dados se a linha não estiver vazia
                print(f"Linha {j}: Tag = {linha[0]}, Dados = {linha[1]}")
            else:
                # Imprime 'Vazio' se a linha estiver vazia
                print(f"Linha {j}: Vazio")

# Função que exibe as estatísticas de desempenho da cache, incluindo contadores de acessos, hit, miss, taxa de acertos e substituições LFU. Imprimi tambem os valores de w, d, s e tag
def exibirEstatisticas(self):
    print()
    # Imprime os contadores de acessos, hit e miss
    print(f"Acessos: {self.contador_acessos} \nQuatidade de Hit: {self.contadorHit}\nQuantidade de Miss: {self.contadorMiss}")
    # Calcula a taxa de acertos se houver acessos
    taxaAcertos = (self.contadorHit / self.contador_acessos) * 100 if self.contador_acessos > 0 else 0
    # Imprime a taxa de acertos formatada para duas casas decimais
    print(f"Taxa de Acerto: {taxaAcertos: .2f}%")
    # Imprime o número de substituições realizadas
    print(f"Quantidade de Substituições LFU: {self.substituicoes}")

    # Imprime informações sobre w, s, d e tag
    print(f"\nConfiguração da Cache:")
    print(f"  Bits de deslocamento (w): {self.deslocamento}")
    print(f"  Bits para o endereço (d): {self.enderecoBits}")
    print(f"  Bits para o índice (s): {self.indiceBits}")
    print(f"  Bits para a tag: {self.tagBits}")
