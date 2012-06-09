import heapq

ESQUERDA = 2
DIREITA = 3

def frequencia(texto):
    tabela = {}
    for caractere in texto:
        tabela[caractere] = tabela.get(caractere, 0) + 1
    return tabela

def unir_nos(a, b):
    frequencia = a[0] + b[0]
    no_pai = (frequencia, None, a, b)
    return no_pai

def prefixos(frequencias):
    arvore = [(f, c) for c, f in frequencias.items()]
    heapq.heapify(arvore)

    while len(arvore) > 1:
        esquerda = heapq.heappop(arvore);
        direita = heapq.heappop(arvore);
        pai = unir_nos(esquerda, direita)
        heapq.heappush(arvore, pai)
    raiz = arvore[0]
    return raiz

def dicionario(arvore, simbolo=''):
    no = arvore[1]

    if no is not None:
        return {no: simbolo or '0'}
    else:
        a = dicionario(arvore[ESQUERDA], simbolo + '0')
        b = dicionario(arvore[DIREITA], simbolo + '1')
        a.update(b)
        return a

def codificar(texto):
    d = dicionario(prefixos(frequencia(texto)))
    return "".join([d[letra] for letra in texto])

def decodificar(codigos, arvore):
    texto = []
    no = arvore
    for codigo in codigos:
        if no[1] is None:
            if codigo == '0':
                no = no[ESQUERDA]
            elif codigo == '1':
                no = no[DIREITA]
        if no[1] is not None:
            texto.append(no[1])
            no = arvore

    return "".join(texto)

def compactar(codigos):
    bytes = [chr(int(codigos[i:i+8], 2)) for i in range(0,len(codigos),8)]
    return "".join(bytes)

def descompactar(texto_compactado, prefixos):
    bytes = [bin(ord(byte))[2:] for byte in texto_compactado]
    for i in range(0, len(bytes) - 1):
        bytes[i] = bytes[i].zfill(8)
    texto_codificado = "".join(bytes)
    texto_descompactado = decodificar(texto_codificado, prefixos)
    return texto_descompactado
