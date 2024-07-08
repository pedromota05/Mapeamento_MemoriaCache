<h1 align="center">
  💾 Um Simulador que não é bem um Simulador! 💾
</h1>
<p align="center">Emulação da memória cache com mapeamento associativo por conjunto e algoritmo de substituição LFU</p>
<p align="center">
  <a href="#-projeto">Resumo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Execução</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;  
  <a href="#-layout">Contato</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<br>

## 💻 Resumo

O programa em Python consiste em emular os o tipo de mapeamento de memória cache com Mapeamento associativo por conjunto.

Mapeamento Associativo por Conjunto<br>
👨‍💻 Implementado por meio do endereço da MP. Cada endereço da MP pode ser visto como consistindo em três campos:

&nbsp;&nbsp;• Os w bits menos significativos identificam uma palavra ou um byte dentro de um bloco da MP.

&nbsp;&nbsp;• Os s bits restantes especificam um dos 2s blocos da MP.

&nbsp;&nbsp;• A lógica de cache interpreta esses s bits como uma tag de s - d bits (parte mais significativa) e um campo de conjunto de d bits. 

&nbsp;&nbsp;• O segundo campo identifica um dos v = 2d conjuntos da cache.

📄 Arquivos de Entrada (modo texto)<br>
&nbsp;&nbsp;• Tamanho da MP (no máximo 256KB).

&nbsp;&nbsp;• Qtde de palavras por bloco na MP (2, 4 ou 8).

&nbsp;&nbsp;• Tamanho da cache (no máximo 32KB).

&nbsp;&nbsp;• Número de linhas por conjunto da cache (mínimo de 2 linhas/máximo é  número de linhas/2).

## ⚙️: Execução do Projeto

### 
Baixe os arquivos e execute pelo Pycharm ou pelo CMD.

### Como utilizar o programa:
```bash
Quando executar o programa, irá aparecer esse menu:
Menu: 
1. Ler o nome de um arquivo de entrada que contenha as informações necessárias
2. Informar um endereço de MP binário válido para acesso à MP
-- OU --
3. Ler o nome de um arquivo que contenha uma sequência de endereços de MP
4. Exibir estatísticas, Memória Principal ou Memória Cache
5. Encerrar o programa
Escolha uma opção: 
```

### Passo a passo de cada opção:
```bash
Para executar a opção 1, utilize o arquivo .txt chamado entrada, contendo os seguintes dados:
128 //Tamanho memória principal
4 //Número de blocos de palavras
16 //Tamanho da cache
4 //Número de linhas por conjunto

Para executar a opção 2, informe um endereço da memória principal em formato binário.

Para executar a opção 3, utilize o arquivo .txt chamado enderecos, contendo uma sequência de endereços da memória principal:
000000000000
000000000001
000000000010
000000000011
000000000100
000000000101
000000000110
000000000111
000000001000
000000001001

Executando a opção 4, exibe um menu para o usuário escolher a informação desejada:
Selecione a opção desejada:
--- 1. Exibir memória principal ---
--- 2. Exibir cache ---
--- 3. Exibir estatísticas ---
--- 4. Voltar ao menu principal ---

A opção 5 encerra o programa!
```

## :telephone: Contato

Meu e-mail: pedro.hmota.goncalves@gmail.com
