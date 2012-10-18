Codificação Huffman implementada em python
==========================================

_R A S C U N H O_

O fim da pré-história foi marcado pelo surgimento da escrita, pelo uso de símbolos para representar ideias.

Determinadas representações de uma informação podem ser mais convenientes que outras para um dado objetivo. O conjunto de símbolos que formam o nosso alfabeto, por exemplo, apesar de ser largamente usado para representar palavras do nosso idioma, precisam ser codificados de uma outra maneira para ser transmitido ou armazenado através de computadores.

Se desejarmos armazenar a palavra "BANANA" em nosso computador, é necessário representá-la através da linguagem da máquina, números binários. Existem várias formas de se fazer isso, uma delas é através de uma variação da codificação ASCII, que atribui um número de 0 a 255 para cada letra:

Letra Decimal Binário
  B     66    01000001
  A     65    01000010
  N     78    01001110

Assim, "BANANA" poderia ser escrito como "01000010 01000001 01001110 01000001 01001110 01000001", o que ocuparia 48 bits de espaço de armazenamento.
Essa codificação é capaz de lidar com um alfabeto de 256 símbolos, abrangendo letras, acentos, sinais de pontuação, etc.. Mas o nosso alfabeto só possui 3, "B", "A" e "N". Então ao invés de usar 8 bit para representar cada símbolo, podemos usar somente 2:

Letra Decimal Binário
  B      0       00
  A      1       01
  N      2       10

Assim, "BANANA" poderia ser escrito como "00 01 10 01 10 01", o que ocuparia 12 bits de espaço de armazenamento. Já foi uma grande melhora, mas ainda podemos fazer melhor.

## Huffman

Nas codificações que vimos até agora, sempre usamos a mesma quantidade de bits para cada símbolo, por isso, bastou percorrer o texto olhando o dicionário a cada N bits (nos exemplos, N foi 8 e depois 2) e fazer a devida substituição para ter nossa palavra escrita novamente na forma original.

Mas, para otimizar espaço, podemos usar quantidades diferentes de bits por símbolo, e mais, podemos escolher os menores números para os símbolos mais frequentes, o que diminui ainda mais o resultado:

Letra Decimal Binário
  A      0       0
  N      1       1
  B      2      10

Assim, "BANANA" poderia ser escrito como "10 0 1 0 1 0", o que ocuparia 7 bits de espaço de armazenamento.

Como não temos mais um número fixo de bits por símbolo, para ter a palavra de volta na forma original, precisamos nos perguntar a cada bit que lemos se encontramos o símbolo correspondente. O que nos mostra um problema no nosso processo, ambiguidade: Como saberemos se o primeiro bit "1" é um "N" ou o início de um "B"?

Para resolver esse problema, devemos escolher nossos números de modo que os bits que representam um símbolo nunca seja prefixo da representação de outro símbolo. A solução proposta por David A. Huffman, foi gerar uma árvore binária que informasse quando um símbolo foi alcançado durante a leitura dos bits. Ao ler o bit "0", seguimos para o nó à esquerda, ao ler o bit "1", seguimos para o nó à direita.

A árvore é gerada da seguinte maneira:

1. Para cada símbolo, cria-se um nó folha e o insere numa fila priorizada pela menor frequência.
Fila: (1, B), (2, N), (3, A)
2. Enquanto há mais de um nó na fila:
    1. Uni-se os dois nós de maior prioridade (os de símbolo de menor frequência) criando um terceiro cuja frequência seja a soma das frequências dos dois primeiros.

    Fila: (3, (1, B), (2, N)), (3, A)

         (3)         (3, A)
        /   \
       /     \
   (1, B)   (2, N)



    Fila: (6, (3, (1, B), (2, N)), (3, A))

             (6)
            /   \
           /     \
         (3)    (3, A)
        /   \
       /     \
   (1, B)   (2, N)

3. O nó que resta é o nó raiz e a árvore está completa.
