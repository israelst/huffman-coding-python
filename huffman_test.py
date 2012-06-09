import unittest
import fixture
from huffman import *

class TestDescompactar(unittest.TestCase):
    def test_descompactar_texto_grande(self):
        compactado = u"""\x04\x94\xfb\xe2\xae\xbd\xf7$e7Mh\xbf\xd2\xfdin\xfd\xab\xe9\xd3G\n\x8fM\x8b,\xde&\x97\xee\xff7\'y~\xdey\xab\xee\xa9LZ\xc7\x87\x8e\xd5\x9e\xb0\xc0iO\xdf[\x922\x9f\xaf\x0b\x1a4\t\t\xe0\x0c\x0b[\xd8\xdfG5\xcb\x1b\xe5\xbe\xc6.\xbf\x04\xe7\xb9\xa7\xb4\x8f\xcd\xeb\xbd,j(\xcbg\x11\x8b\xdap\xc0iC\xdc\xc7\xa7=h\x12\x13\x95o]\xbe5\xa6\xf7\x9eN\xb4\xb7|\'\x8a\x03\x03\x9c\xf7C\xd7\xe2\x8e\x9f\xb9#)\x8bd\xf5\'\x83{s\xd0\xd6-\x96\xc8\xba\xaa+\xf2\xdf\x13[\xfb\xdf\xd6"/}\xc9\x19O\xde\xf8;\xac1Y\x9cF2\xa1\x0cS\xa0\x18\x1e\xba\xde\xaa\xf7M\xd2\xd5\xa6\xd6\x8f\xb4V\xb3\xa8\xf2*+4\xb6RI\xe7\xb5/\xddv\xac[Y\xc5Q\x82s\xa48sc\x1b\x9f\xdfGj\xd7\x91\x13Z\x18\xdf\x1eo\xeda\x80\xd2\x8fp\x00"""
        self.assertEqual(descompactar(compactado, fixture.arvore), fixture.texto)

    def test_descompactar_abacabi(self):
        self.assertEqual(descompactar('h\x1d', fixture.arvore_abacabi), 'abacabi')


class TestCompactar(unittest.TestCase):
    def test_compactar_abacabi(self):
        codigo_abacabi = '0110100011101'
        self.assertEqual(compactar(codigo_abacabi), 'h\x1d')


class TestDicionario(unittest.TestCase):
    def test_palavra_com_1_letra(self):
        arvore = (1, 'a')
        self.assertEqual(dicionario(arvore), {'a': '0'})
        arvore = (1, 'b')
        self.assertEqual(dicionario(arvore), {'b': '0'})

    def test_tabela_com_elementos_diferentes_ab(self):
        arvore = (2, None, (1, 'a'), (1, 'b'))
        self.assertEqual(dicionario(arvore), {'a': '0',
                                              'b': '1'})

    def test_tabela_abacabi(self):
        self.assertEqual(dicionario(fixture.arvore_abacabi),
                {'a': '0',
                 'b': '11',
                 'c': '100',
                 'i': '101'})

class TestCodificar(unittest.TestCase):
    def test_palavra_com_1_letra(self):
        palavra = 'a'
        self.assertEqual(codificar(palavra), '0')

    def test_palavra_com_2_letras_b(self):
        palavra = 'bb'
        self.assertEqual(codificar(palavra), '00')

    def test_palavra_com_letras_diferentes(self):
        palavra = 'ab'
        self.assertEqual(codificar(palavra), '01')
        palavra = 'abacabi'
        self.assertEqual(codificar(palavra), '0110100011101')

class TestDecodificar(unittest.TestCase):
    def test_palavra_com_1_letra(self):
        arvore = (1, 'a')
        codigos = '0'
        self.assertEqual(decodificar(codigos, arvore), 'a')

    def test_palavra_com_2_letras_b(self):
        arvore = (1, 'b')
        codigos = '00'
        self.assertEqual(decodificar(codigos, arvore), 'bb')

    def test_palavra_com_2_letras_diferentes(self):
        arvore = (7, None,
                    (3, 'a'),
                    (4, 'b'))
        codigos = '01'
        self.assertEqual(decodificar(codigos, arvore), 'ab')

    def test_palavra_com_letras_diferentes(self):
        codigos = '0110100011101'
        self.assertEqual(decodificar(codigos, fixture.arvore_abacabi), 'abacabi')

class TestTabelaFrequencia(unittest.TestCase):
    def test_palavra_vazia(self):
        palavra = ''
        self.assertEqual(frequencia(palavra), {})

    def test_palavra_com_1_letra(self):
        palavra = 'a'
        self.assertEqual(frequencia(palavra), {'a': 1})

    def test_palavra_com_2_letras_b(self):
        palavra = 'bb'
        self.assertEqual(frequencia(palavra), {'b': 2})

    def test_palavra_com_letras_diferentes(self):
        palavra = 'ab'
        self.assertEqual(frequencia(palavra), {'a': 1, 'b':1})

    def test_abacabi(self):
        palavra = 'abacabi'
        self.assertEqual(frequencia(palavra), {'a': 3, 'b': 2, 'c': 1, 'i': 1})


class TestArvoreDePrefixos(unittest.TestCase):
    def test_tabela_com_um_elemento_a(self):
        tabela = {'a': 1}
        self.assertEqual(prefixos(tabela), (1, 'a'))

    def test_tabela_com_um_elemento_b(self):
        tabela = {'b': 1}
        self.assertEqual(prefixos(tabela), (1, 'b'))

    def test_tabela_com_elementos_diferentes_ab(self):
        tabela = {'a': 1, 'b':1}
        arvore = (2, None, (1, 'a'), (1, 'b'))
        self.assertEqual(prefixos(tabela), arvore)

    def test_tabela_com_elementos_diferentes_ac(self):
        tabela = {'a': 1, 'c': 1}
        arvore = (2, None, (1, 'a'), (1, 'c'))
        self.assertEqual(prefixos(tabela), arvore)

    def test_tabela_abacabi(self):
        tabela = {'i': 1, 'a': 3, 'b': 2, 'c':1}
        self.assertEqual(prefixos(tabela), fixture.arvore_abacabi)

unittest.main()
