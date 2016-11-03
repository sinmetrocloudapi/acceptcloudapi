#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy

'''
Table of Control Chart Constants
'''
class TableSPC:
    colN = 0
    colA = 1
    colA2 = 2
    colA3 = 3
    colC4 = 4
    colB3 = 5
    colB4 = 6
    colB5 = 7
    colB6 = 8
    colD2Pequeno = 9
    colD2 = 10
    colD3 = 11
    colD4 = 12
    colD1 = 13

    def getConstantTableSPC(self, parametro, n):

        tabelaSPC = self.criarTabelaSPC()
        valor = self.obterValor(tabelaSPC, parametro, n)

        return valor

    """
    Cria a Tabela SPC com os respetivos dados preenchidos
    """
    def criarTabelaSPC(self):
        
        colunaN = self.preencherColunaN()

        colunaA = self.preencherColunaA()
        colunaA2 = self.preencherColunaA2()
        colunaA3 = self.preencherColunaA3()

        colunaC4 = self.preencherColunaC4()

        colunaB3 = self.preencherColunaB3()
        colunaB4 = self.preencherColunaB4()
        colunaB5 = self.preencherColunaB5()
        colunaB6 = self.preencherColunaB6()

        colunaD2Pequeno = self.preencherColunaD2Pequeno()
        colunaD2 = self.preencherColunaD2()
        colunaD3 = self.preencherColunaD3()
        colunaD4 = self.preencherColunaD4()
        colunaD1 = self.preencherColunaD1()

        tabelaSPC = numpy.array([colunaN, colunaA, colunaA2, colunaA3, colunaC4, colunaB3, colunaB4, colunaB5, colunaB6, colunaD2Pequeno, colunaD2, colunaD3, colunaD4, colunaD1], dtype=float)

        return tabelaSPC

  
    '''
    Preenche coluna 0 : Sample size = n
    :param coluna: index da coluna
    :return coluna: retorna coluna 0 preenchida
    '''
    def preencherColunaN(self):
        coluna = [] 
        coluna.insert(0, 2)
        coluna.insert(1, 3)
        coluna.insert(2, 4)
        coluna.insert(3, 5)
        coluna.insert(4, 6)
        coluna.insert(5, 7)
        coluna.insert(6, 8)
        coluna.insert(7, 9)
        coluna.insert(8, 10)
        coluna.insert(9, 11)
        coluna.insert(10, 12)
        coluna.insert(11, 13)
        coluna.insert(12, 14)
        coluna.insert(13, 15)
        coluna.insert(14, 16)
        coluna.insert(15, 17)
        coluna.insert(16, 18)
        coluna.insert(17, 19)
        coluna.insert(18, 20)
        coluna.insert(19, 21)
        coluna.insert(20, 22)
        coluna.insert(21, 23)
        coluna.insert(22, 24)
        coluna.insert(23, 25)

        return coluna

    '''
    Preenche coluna A : Coluna A
    :param coluna: index da coluna
    :return coluna: retorna coluna A preenchida
    '''
    def preencherColunaA(self):
        coluna = []
    
        coluna.insert(0, 2.121)
        coluna.insert(1, 1.732)
        coluna.insert(2, 1.500)
        coluna.insert(3, 1.342)
        coluna.insert(4, 1.225)
        coluna.insert(5, 1.134)
        coluna.insert(6, 1.061)
        coluna.insert(7, 1.000)
        coluna.insert(8, 0.949)
        coluna.insert(9, 0.905)
        coluna.insert(10, 0.866)
        coluna.insert(11, 0.832)
        coluna.insert(12, 0.802)
        coluna.insert(13, 0.775)
        coluna.insert(14, 0.750)
        coluna.insert(15, 0.728)
        coluna.insert(16, 0.707)
        coluna.insert(17, 0.688)
        coluna.insert(18, 0.671)
        coluna.insert(19, 0.655)
        coluna.insert(20, 0.640)
        coluna.insert(21, 0.626)
        coluna.insert(22, 0.612)
        coluna.insert(23, 0.600)
        
        return coluna

    '''
    Preenche coluna A2 : Coluna A2
    :param coluna: index da coluna
    :return coluna: retorna coluna A2 preenchida
    ''' 
    def preencherColunaA2(self):
        coluna = []

        coluna.insert(0, 1.880)
        coluna.insert(1, 1.023)
        coluna.insert(2, 0.729)
        coluna.insert(3, 0.577)
        coluna.insert(4, 0.483)
        coluna.insert(5, 0.419)
        coluna.insert(6, 0.373)
        coluna.insert(7, 0.337)
        coluna.insert(8, 0.308)
        coluna.insert(9, 0.285)
        coluna.insert(10, 0.266)
        coluna.insert(11, 0.249)
        coluna.insert(12, 0.235)
        coluna.insert(13, 0.223)
        coluna.insert(14, 0.212)
        coluna.insert(15, 0.203)
        coluna.insert(16, 0.194)
        coluna.insert(17, 0.187)
        coluna.insert(18, 0.180)
        coluna.insert(19, 0.173)
        coluna.insert(20, 0.167)
        coluna.insert(21, 0.162)
        coluna.insert(22, 0.157)
        coluna.insert(23, 0.153)

        return coluna

    '''
    Preenche coluna A3 : Coluna A3
    :param coluna: index da coluna
    :return coluna: retorna coluna A3 preenchida
    ''' 
    def preencherColunaA3(self):
        coluna = []

        coluna.insert(0, 02.659)
        coluna.insert(1, 01.954)
        coluna.insert(2, 01.628)
        coluna.insert(3, 01.427)
        coluna.insert(4, 01.287)
        coluna.insert(5, 01.182)
        coluna.insert(6, 01.099)
        coluna.insert(7, 01.032)
        coluna.insert(8, 00.975)
        coluna.insert(9, 00.927)
        coluna.insert(10, 00.886)
        coluna.insert(11, 00.850)
        coluna.insert(12, 00.817)
        coluna.insert(13, 00.789)
        coluna.insert(14, 00.763)
        coluna.insert(15, 00.739)
        coluna.insert(16, 00.718)
        coluna.insert(17, 00.698)
        coluna.insert(18, 00.680)
        coluna.insert(19, 00.663)
        coluna.insert(20, 00.647)
        coluna.insert(21, 00.633)
        coluna.insert(22, 00.619)
        coluna.insert(23, 00.606)

        return coluna

    '''
    Preenche coluna C4 : C4
    :param coluna: index da coluna
    :return coluna: retorna coluna C4 preenchida
    '''
    def preencherColunaC4(self):
        coluna = []

        coluna.insert(0, 0.798)
        coluna.insert(1, 0.886)
        coluna.insert(2, 0.921)
        coluna.insert(3, 0.940)
        coluna.insert(4, 0.951)
        coluna.insert(5, 0.959)
        coluna.insert(6, 0.965)
        coluna.insert(7, 0.969)
        coluna.insert(8, 0.973)
        coluna.insert(9, 0.975)
        coluna.insert(10, 0.978)
        coluna.insert(11, 0.979)
        coluna.insert(12, 0.981)
        coluna.insert(13, 0.982)
        coluna.insert(14, 0.984)
        coluna.insert(15, 0.984)
        coluna.insert(16, 0.985)
        coluna.insert(17, 0.986)
        coluna.insert(18, 0.987)
        coluna.insert(19, 0.988)
        coluna.insert(20, 0.988)
        coluna.insert(21, 0.989)
        coluna.insert(22, 0.989)
        coluna.insert(23, 0.990)

        return coluna

    '''
    Preenche coluna B3 : B3
    :param coluna: index da coluna
    :return coluna: retorna coluna B3 preenchida
    '''
    def preencherColunaB3(self):
        coluna = []

        coluna.insert(0, 0.000)
        coluna.insert(1, 0.000)
        coluna.insert(2, 0.000)
        coluna.insert(3, 0.000)
        coluna.insert(4, 0.030)
        coluna.insert(5, 0.118)
        coluna.insert(6, 0.185)
        coluna.insert(7, 0.239)
        coluna.insert(8, 0.284)
        coluna.insert(9, 0.321)
        coluna.insert(10, 0.354)
        coluna.insert(11, 0.382)
        coluna.insert(12, 0.406)
        coluna.insert(13, 0.428)
        coluna.insert(14, 0.448)
        coluna.insert(15, 0.466)
        coluna.insert(16, 0.482)
        coluna.insert(17, 0.497)
        coluna.insert(18, 0.510)
        coluna.insert(19, 0.523)
        coluna.insert(20, 0.534)
        coluna.insert(21, 0.545)
        coluna.insert(22, 0.555)
        coluna.insert(23, 0.565)

        return coluna

    '''
    Preenche coluna B4 : B4
    :param coluna: index da coluna
    :return coluna: retorna coluna B4 preenchida
    '''
    def preencherColunaB4(self):
        coluna = []
 
        coluna.insert(0, 3.267)
        coluna.insert(1, 2.568)
        coluna.insert(2, 2.266)
        coluna.insert(3, 2.089)
        coluna.insert(4, 1.970)
        coluna.insert(5, 1.882)
        coluna.insert(6, 1.815)
        coluna.insert(7, 1.761)
        coluna.insert(8, 1.716)
        coluna.insert(9, 1.679)
        coluna.insert(10, 1.646)
        coluna.insert(11, 1.618)
        coluna.insert(12, 1.594)
        coluna.insert(13, 1.572)
        coluna.insert(14, 1.552)
        coluna.insert(15, 1.534)
        coluna.insert(16, 1.518)
        coluna.insert(17, 1.503)
        coluna.insert(18, 1.490)
        coluna.insert(19, 1.477)
        coluna.insert(20, 1.466)
        coluna.insert(21, 1.455)
        coluna.insert(22, 1.445)
        coluna.insert(23, 1.435)

        return coluna

    '''
    Preenche coluna B5 : B5
    :param coluna: index da coluna
    :return coluna: retorna coluna B5 preenchida
    '''
    def preencherColunaB5(self):
        coluna = []

        ### Coluna colb5 : B5
        coluna.insert(0, 0.000)
        coluna.insert(1, 0.000)
        coluna.insert(2, 0.000)
        coluna.insert(3, 0.000)
        coluna.insert(4, 0.029)
        coluna.insert(5, 0.113)
        coluna.insert(6, 0.179)
        coluna.insert(7, 0.232)
        coluna.insert(8, 0.276)
        coluna.insert(9, 0.313)
        coluna.insert(10, 0.346)
        coluna.insert(11, 0.374)
        coluna.insert(12, 0.399)
        coluna.insert(13, 0.421)
        coluna.insert(14, 0.440)
        coluna.insert(15, 0.458)
        coluna.insert(16, 0.475)
        coluna.insert(17, 0.490)
        coluna.insert(18, 0.504)
        coluna.insert(19, 0.516)
        coluna.insert(20, 0.528)
        coluna.insert(21, 0.539)
        coluna.insert(22, 0.549)
        coluna.insert(23, 0.559)

        return coluna

    '''
    Preenche coluna B6 : B6
    :param coluna: index da coluna
    :return coluna: retorna coluna B6 preenchida
    '''
    def preencherColunaB6(self):
        coluna = []

        coluna.insert(0, 2.606)
        coluna.insert(1, 2.276)
        coluna.insert(2, 2.088)
        coluna.insert(3, 1.964)
        coluna.insert(4, 1.874)
        coluna.insert(5, 1.806)
        coluna.insert(6, 1.751)
        coluna.insert(7, 1.707)
        coluna.insert(8, 1.669)
        coluna.insert(9, 1.637)
        coluna.insert(10, 1.610)
        coluna.insert(11, 1.585)
        coluna.insert(12, 1.563)
        coluna.insert(13, 1.544)
        coluna.insert(14, 1.526)
        coluna.insert(15, 1.511)
        coluna.insert(16, 1.496)
        coluna.insert(17, 1.483)
        coluna.insert(18, 1.470)
        coluna.insert(19, 1.459)
        coluna.insert(20, 1.448)
        coluna.insert(21, 1.438)
        coluna.insert(22, 1.429)
        coluna.insert(23, 1.420)

        return coluna

    '''
    Preenche coluna d2 : d2
    :param coluna: index da coluna
    :return coluna: retorna coluna d2 preenchida
    '''
    def preencherColunaD2Pequeno(self):
        coluna = []
        ### Coluna colD2Pequeno : d2
        coluna.insert(0, 1.128)
        coluna.insert(1, 1.693)
        coluna.insert(2, 2.059)
        coluna.insert(3, 2.326)
        coluna.insert(4, 2.534)
        coluna.insert(5, 2.704)
        coluna.insert(6, 2.847)
        coluna.insert(7, 2.970)
        coluna.insert(8, 3.078)
        coluna.insert(9, 3.173)
        coluna.insert(10, 3.258)
        coluna.insert(11, 3.336)
        coluna.insert(12, 3.407)
        coluna.insert(13, 3.472)
        coluna.insert(14, 3.532)
        coluna.insert(15, 3.588)
        coluna.insert(16, 3.640)
        coluna.insert(17, 3.689)
        coluna.insert(18, 3.735)
        coluna.insert(19, 3.778)
        coluna.insert(20, 3.819)
        coluna.insert(21, 3.858)
        coluna.insert(22, 3.895)
        coluna.insert(23, 3.931)

        return coluna
 
    '''
    Preenche coluna D2 : D2
    :param coluna: index da coluna
    :return coluna: retorna coluna D2 preenchida
    '''
    def preencherColunaD2(self):
        coluna = []

        coluna.insert(0, 3.686)
        coluna.insert(1, 4.358)
        coluna.insert(2, 4.698)
        coluna.insert(3, 4.918)
        coluna.insert(4, 5.078)
        coluna.insert(5, 5.204)
        coluna.insert(6, 5.306)
        coluna.insert(7, 5.393)
        coluna.insert(8, 5.469)
        coluna.insert(9, 5.535)
        coluna.insert(10, 5.594)
        coluna.insert(11, 5.647)
        coluna.insert(12, 5.696)
        coluna.insert(13, 5.741)
        coluna.insert(14, 5.782)
        coluna.insert(15, 5.820)
        coluna.insert(16, 5.856)
        coluna.insert(17, 5.891)
        coluna.insert(18, 5.921)
        coluna.insert(19, 5.951)
        coluna.insert(20, 5.979)
        coluna.insert(21, 6.006)
        coluna.insert(22, 6.031)
        coluna.insert(23, 6.056)

        return coluna

    '''
    Preenche coluna D3 : D3
    :param coluna: index da coluna
    :return coluna: retorna coluna D3 preenchida
    '''
    def preencherColunaD3(self):
        coluna = []

        coluna.insert(0, 0.000)
        coluna.insert(1, 0.000)
        coluna.insert(2, 0.000)
        coluna.insert(3, 0.000)
        coluna.insert(4, 0.000)
        coluna.insert(5, 0.076)
        coluna.insert(6, 0.136)
        coluna.insert(7, 0.184)
        coluna.insert(8, 0.223)
        coluna.insert(9, 0.256)
        coluna.insert(10, 0.283)
        coluna.insert(11, 0.307)
        coluna.insert(12, 0.328)
        coluna.insert(13, 0.347)
        coluna.insert(14, 0.363)
        coluna.insert(15, 0.378)
        coluna.insert(16, 0.391)
        coluna.insert(17, 0.403)
        coluna.insert(18, 0.415)
        coluna.insert(19, 0.425)
        coluna.insert(20, 0.434)
        coluna.insert(21, 0.443)
        coluna.insert(22, 0.451)
        coluna.insert(23, 0.459)

        return coluna

    '''
    Preenche coluna D4 : D4
    :param coluna: index da coluna
    :return coluna: retorna coluna D4 preenchida
    '''
    def preencherColunaD4(self):
        coluna = []

        coluna.insert(0, 3.267)
        coluna.insert(1, 2.575)
        coluna.insert(2, 2.282)
        coluna.insert(3, 2.115)
        coluna.insert(4, 2.004)
        coluna.insert(5, 1.924)
        coluna.insert(6, 1.864)
        coluna.insert(7, 1.816)
        coluna.insert(8, 1.777)
        coluna.insert(9, 1.744)
        coluna.insert(10, 1.717)
        coluna.insert(11, 1.693)
        coluna.insert(12, 1.672)
        coluna.insert(13, 1.653)
        coluna.insert(14, 1.637)
        coluna.insert(15, 1.622)
        coluna.insert(16, 1.608)
        coluna.insert(17, 1.597)
        coluna.insert(18, 1.585)
        coluna.insert(19, 1.575)
        coluna.insert(20, 1.566)
        coluna.insert(21, 1.557)
        coluna.insert(22, 1.548)
        coluna.insert(23, 1.541)

        return coluna

    '''
    Preenche coluna D1 : D1
    :param coluna: index da coluna
    :return coluna: retorna coluna D1 preenchida
    '''
    def preencherColunaD1(self):
        coluna = []

        coluna.insert(0, 0.000)
        coluna.insert(1, 0.000)
        coluna.insert(2, 0.000)
        coluna.insert(3, 0.000)
        coluna.insert(4, 0.000)
        coluna.insert(5, 0.204)
        coluna.insert(6, 0.388)
        coluna.insert(7, 0.547)
        coluna.insert(8, 0.687)
        coluna.insert(9, 0.811)
        coluna.insert(10, 0.922)
        coluna.insert(11, 1.025)
        coluna.insert(12, 1.118)
        coluna.insert(13, 1.203)
        coluna.insert(14, 1.282)
        coluna.insert(15, 1.356)
        coluna.insert(16, 1.424)
        coluna.insert(17, 1.487)
        coluna.insert(18, 1.549)
        coluna.insert(19, 1.605)
        coluna.insert(20, 1.659)
        coluna.insert(21, 1.710)
        coluna.insert(22, 1.759)
        coluna.insert(23, 1.806)

        return coluna
    
    '''
    Obtem o valor da constante com base no fator e tamanho da amostra
    :param tabelaSPC: tabela SPC
    :param fator: nome do fator
    :param n: tamanho da amostra
    :return valo: retorna o valor da constante
    '''
    def obterValor(self, tableSPC, factor, n):

        coluna = 0
        num = n - 2

        if factor.upper() == 'A':
            coluna = self.colA
            pass
        elif factor.upper() == 'A2':
            coluna = self.colA2
            pass
        elif factor.upper() == 'A3':
            coluna = self.colA3
            pass
        elif factor.upper() == 'C4':
            coluna = self.colC4 
            pass
        elif factor.upper() == 'B3':
            coluna = self.colB3
            pass
        elif factor.upper() == 'B4':
            coluna = self.colB4
            pass
        elif factor.upper() == 'B5':
            coluna = self.colB5
            pass
        elif factor.upper() == 'B6':
            coluna = self.colB6
            pass
        elif factor.upper() == 'D2PEQUENO':
            coluna = self.colD2Pequeno
            pass
        elif factor.upper() == 'D2':
            coluna = self.colD2
            pass
        elif factor.upper() == 'D3':
            coluna = self.colD3
            pass
        elif factor.upper() == 'D4':
            coluna = self.colD4
            pass
        elif factor.upper() == 'D1':
            coluna = self.colD1
            pass

        return tableSPC.item(coluna, num)

    pass



    
    