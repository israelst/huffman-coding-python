import unittest
from huffman import *

class TestDescompactar(unittest.TestCase):
    def test_descompactar_texto_grande(self):
        import fixture
        compactado = "\xb0\x1e0\xdf#O\x86j\xd4\xd0\x8b\x85\x96\xf8@[\x8a\x9f`\xfb\xb8gG\xcd<\xd3~I^\xe1D\xd1\xeei\xbf4\xad\xf5\xde\x12\xbd`<a\xbeF\x9f\x0c4\xadd\x99\xdc3\x9aV\xfa\xef\n\xea\xad\\\x92\xb4\xf2\xf2\xdf\x08\x0bqS\xecn\x1fji\xb4\xee\x19\xcaW]\xdd\xdd*\xdf\x86g$\xe7\xcf\xf9\x0f\xd3\xa3\xe6\x9e>\xdc\x01\xff&\xbd\x1c\xe2,\x1fw\n'$\xafU\xbeHYq^n\xdc\x1a\t\xfc\xe4\xdc(\x9dQ6\xb4\x0c\xeb \x1f\xd5\xef\x9d\x86\x95\xa9\xfe\xb8\xd7\n\xf4\x87`\x97\x0b}k\x87Zg\x9f\xe64\xabY\x7fdu\x06\xe1\x9c\xe2\x91\xcd<\x18\xb8\xdb\xde\tkw\n&\x8fsM\xea\xb7\x8c\x11\xa5\xa6\xfcj\x8c\xf3#\x9c,\xf9\xb4i7\x95\xab\xdf;~J\xd1\x08\xbd\xc9\xe6\xa2\xbc\xd3\xb8g)(T\x17u\xbf7\x0fp\xce\xf1qJ8>\xeb\x07\xbc\x94{P\xc9\xea\xd6\x84\xf24\xb4\xdf\xac\x07\x8c7\xc8\xd3\xe1\xa2\x95Iy\xa5Y%z\x01\xe3\xbcm3\xce\x16\xfc\xdc<\xb3_\xf8#\xa2\xfb.j\x1bM\xfa\x83\xef~O\x1c\xe6\xfer\x89\xcb}k\xa2^Ti\xfc\xfb4\xda\xe7\xad\xa6\xfdp\xfa\x98&\xb0}\xd6\x03\xc6\x1b\xe4i\xf0+"
        self.assertEqual(descompactar(compactado, fixture.arvore), fixture.texto)

    def test_descompactar_abacabi(self):
        arvore = (7, None, 
                (3, 'a'),
                (4, None, 
                    (2, None, 
                        (1, 'c'), 
                        (1, 'i')),
                    (2, 'b'))
                )
        self.assertEqual(descompactar('h\x1d', arvore), 'abacabi')


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
        arvore = (7, None,
                (3, 'a'),
                (4, None,
                    (2, None,
                        (1, 'c'),
                        (1, 'i')),
                    (2, 'b'))
                )
        self.assertEqual(dicionario(arvore), {'a': '0',
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
        arvore = (7, None,
                (3, 'a'),
                (4, None,
                    (2, None,
                        (1, 'c'),
                        (1, 'i')),
                    (2, 'b'))
                )
        codigos = '0110100011101'
        self.assertEqual(decodificar(codigos, arvore), 'abacabi')

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
        arvore = (7, None, 
                (3, 'a'),
                (4, None, 
                    (2, None, 
                        (1, 'c'), 
                        (1, 'i')),
                    (2, 'b'))
                )
        self.assertEqual(prefixos(tabela), arvore)

unittest.main()
