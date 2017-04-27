#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from poker import *

# 23456789 D JQK A
# Ouro (D), Copas (H), Espadas (S), Paus (C)

# 0 CartaAlta       : A carta de maior valor.
# 1 Par             : Duas cartas do mesmo valor.
# 2 DoisPares       : Dois pares diferentes.
# 3 Trinca          : Três cartas do mesmo valor e duas de valores diferentes.
# 4 Straight        : Todas as carta com valores consecutivos.
# 5 # Flush         : Todas as cartas do MESMO NAIPE.
# 6 FullHouse       : Um trinca e um par.
# 7 Quadra          : Quatro cartas do mesmo valor.
# 8 # StraightFlush : Todas as cartas são consecutivas e do MESMO NAIPE.
# 9 # RoyalFlush    : A seqüência 10, Valete, Dama, Rei, Ás, do MESMO NAIPE.


class TestIdentificaACombinacao(unittest.TestCase):
    def test_CartaAlta(self):
        self.assertEqual((0, 7, 7), combinacao('2C 3C 4C 5C 7O'))  # CartaAlta
    def test_Flush(self):
        self.assertEqual((5, 7, 7), combinacao('2C 3C 4C 5C 7C'))  # Flush
    def test_Straight(self):
        self.assertEqual((4, 6, 6), combinacao('2C 3C 4C 5C 6O'))  # Straight
    def test_StraightFlush(self):
        self.assertEqual((8, 6, 6), combinacao('2C 3C 4C 5C 6C'))  # StraightFlush
        
    def test_Par(self):
        self.assertEqual((1, 2, 5), combinacao('2C 2P 3C 4C 5O'))  # Par
    def test_Par_Flush(self):
        self.assertEqual((5, 2, 5), combinacao('2C 2C 3C 4C 5C'))  # Flush
        
        
    def test_DoisPares(self):
        self.assertEqual((2, 3, 4), combinacao('2C 2O 3C 3O 4O'))  # DoisPares
    def test_DoisPares_Flush(self):
        self.assertEqual((5, 3, 4), combinacao('2C 2C 3C 3C 4C'))  # Flush
        
    def test_Trinca(self):
        self.assertEqual((3, 2, 4), combinacao('2C 2O 2P 3O 4O'))  # Trinca
    def test_Trinca_Flush(self):
        self.assertEqual((5, 2, 4), combinacao('2C 2C 2C 3C 4C'))  # Flush
        
    def test_FullHouse(self):
        self.assertEqual((6, 3, 2), combinacao('2C 2O 3C 3O 3P'))  # FullHouse
    def test_FullHouse_mesmo_naipe(self):
        self.assertEqual((6, 3, 2), combinacao('2C 2C 3C 3C 3C'))  # FullHouse
        
    def test_Quadra(self):
        self.assertEqual((7, 2, 3), combinacao('2C 2O 2P 2E 3O'))  # Quadra
    def test_Quadra_mesmo_naipe(self):
        self.assertEqual((7, 2, 3), combinacao('2C 2C 2C 2C 3C'))  # Quadra
        
    def test_RoyalFlush(self):
        self.assertEqual((8, 14, 14), combinacao('DC JC QC KC AC'))  # StraightFlush -> RoyalFlush
    


class TestPoker(unittest.TestCase):
    def test_carta_mais_alta(self):
        self.assertEqual(1, poker('4C 6P 7P 9P KP', '6C 7O 8O 9O JO'))
        self.assertEqual(2, poker('6C 7O 8O 9O JO', '4C 6P 7P 9P KP'))
        
        self.assertEqual(1, poker('5D 8P 9E JE AP', '2P 5P 7O 8E QC'))

    def test_um_par(self):
        self.assertEqual(1, poker('5C 5P 2C 3C 4C', '6C 7O 8C 9C AC'))
        self.assertEqual(2, poker('6C 7O 8C 9C AC', '5C 5P 2C 3C 4C'))

    def test_maior_par(self):
        self.assertEqual(2, poker('5C 5P 2C 3C 4C', '6C 6P 7C 8C 9C'))
        self.assertEqual(1, poker('7C 7P 2C 3C 4C', '6C 6P 7C 8C 9C'))
        
        self.assertEqual(2, poker('5C 5P 6E 7E KO', '2P 3E 8E 8O DO'))
        
    def test_pares_iguais(self):
        self.assertEqual(1, poker('4O 6E 9C QC QP', '3O 6O 7C QO QE'))
        
    def test_Flush_ganha_de_Trinca(self):
        self.assertEqual(2, poker('2O 9P AE AC AP', '3O 6O 7O DO QO'))
        
    def test_FullHouse_com_Trinca_de_4_ganha_FullHouse_com_Trinca_de_3(self):
        self.assertEqual(1, poker('2C 2O 4P 4O 4E', '3P 3O 3E 9E 9O'))

    def test_royal_straigth_flush_ganha_de_todos(self):
        self.assertEqual(2, poker('9C DC JC QC KC', 'DC JC QC KC AC'))
        
        self.assertEqual(2, poker('DC JP QC KC AC', 'DC JC QC KC AC'))
        self.assertEqual(1, poker('DC JC QC KC AC', 'DC JP QC KC AC'))


if __name__ == "__main__":
    unittest.main()
