#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy
from stats import table_spc

'''
Carta de Controlo X S 
'''
class CartaControloXS:

    TABLE_SPC = table_spc.TableSPC()

    def main(self, n, media, std, casasdecimais):
   
        dictCartaXS = {}

        dictCartaXS["dados_cartasxs"] = {
            
            'lscx' : round(self.calcularLSCx(n, media, std), casasdecimais),
            'lcx' : round(self.calcularLCx(media), casasdecimais), 
            'licx' : round(self.calcularLICx(n, media, std), casasdecimais),

            'lscs' : round(self.calcularLSCs(n, std), casasdecimais),
            'lcs' : round(self.calcularLCs(std), casasdecimais),
            'lics' : round(self.calcularLICs(n, std), casasdecimais)
            }

        return dictCartaXS

    """
    Cálculo da Linha Central para as médias (LCx)
    :param media - media
    :return lcx - retorno da linha central das médias 
    """
    def calcularLCx(self, media):
        lcx = media 
        return lcx

    """
    Cálculo do Limite Inferior de Controlo para as médias (LICx)
    :param n - tamanho da amostra
    :param media - média
    :param stdmedio - desvio-padrão
    :return licx = retorna o limite inferior de controlo para as médias 
    """
    def calcularLICx(self, n, media, stdMedio):
        a3 = self.TABLE_SPC.getConstantTableSPC("a3", n)
        licx = media - (a3 * stdMedio)
        return licx 

    """
    Cálculo do Limite Superior de Controlo para as médias (LSCx)
    :param n - tamanho da amostra
    :param media - média
    :param stdmedio - se n = 1 então rmedia é a amplitude móvel média. se n > 1 então rmedia é a amplitude média
    :return lscx = retorna o limite superior de controlo para as médias 
    """
    def calcularLSCx(self, n, media, stdmedio):
        a3 = self.TABLE_SPC.getConstantTableSPC("a3", n)
        lscx = media + (a3 * stdmedio)
        
        return lscx

    """
    Cálculo da Linha Central para o desvio-padrão (LCs)
    :param stdMedio - desvio-padrao médio
    :return lcs - retorno da linha central dos desvios-padrão 
    """
    def calcularLCs(self, stdMedio):
        lcs = stdMedio 
        return lcs

    """
    Cálculo do Limite Inferior de Controlo para o desvio-padrão(LICs)
    :param n - tamanho da amostra
    :param stdmedio - desvio-padrão médio
    :return licr = retorna o limite inferior de controlo para o desvio-padrão
    """
    def calcularLICs(self, n, stdmedio):
        #rmedia = amplitude média
        b3 = self.TABLE_SPC.getConstantTableSPC("b3", n)
        lics = b3 * stdmedio
            
        return lics

    """
    Cálculo do Limite Superior de Controlo para o desvio-padrão (LSCs)
    :param n - tamanho da amostra
    :param stdMedio - desvio-padrão médio
    :return lscs = retorna o limite superior de controlo para o desvio-padrão 
    """
    def calcularLSCs(self, n, stdMedio):
        b4 = self.TABLE_SPC.getConstantTableSPC("b4", n)
        lscs = b4 * stdMedio

        return lscs

    pass
