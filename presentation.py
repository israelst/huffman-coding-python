# coding: utf-8
from huffman import *


texto = "BANANA"
texto = u"texto de teste para ser compactado"

arvore = prefixos(frequencia(texto))


compactado = compactar(codificar(texto, dicionario(arvore)))
descompactar(compactado, arvore)
