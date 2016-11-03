#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy
from stats import table_spc

'''
Carta de Controlo X R 
'''
class CartaControloXR:

    TABLE_SPC = table_spc.TableSPC()

    def main(self, n, media, rmedia, casasdecimais):
    
        dictCartaXR = {}

        dictCartaXR["dados_cartasxr"] = {
            
            'lscx' : round(self.calcularLSCx(n, media, rmedia), casasdecimais),
            'lcx' : round(self.calcularLCx(media), casasdecimais), 
            'licx' : round(self.calcularLICx(n, media, rmedia), casasdecimais),

            'lscr' : round(self.calcularLSCr(n, media, rmedia), casasdecimais),
            'lcr' : round(self.calcularLCr(rmedia), casasdecimais), 
            'licr' : round(self.calcularLICr(n, media, rmedia), casasdecimais)
            }

        return dictCartaXR
    
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
    :param rmedia - se n = 1 então rmedia é a amplitude móvel. se n > 1 então rmedia é a amplitude média
    :return licx = retorna o limite inferior de controlo para as médias 
    """
    def calcularLICx(self, n, media, rmedia):
        licx = 0
        if n == 1:
            #rmedia = amplitude móvel
            licx = media - (2.66 * rmedia)
            pass

        else:
            #rmedia = amplitude média
            a2 = self.TABLE_SPC.getConstantTableSPC("a2", n)
            licx = media - (a2 * rmedia)
            pass

        return licx 

    """
    Cálculo do Limite Superior de Controlo para as médias (LSCx)
    :param n - tamanho da amostra
    :param media - média
    :param rmedia - se n = 1 então rmedia é a amplitude móvel média. se n > 1 então rmedia é a amplitude média
    :return lscx = retorna o limite superior de controlo para as médias 
    """
    def calcularLSCx(self, n, media, rmedia):
        lscx = 0
        if n == 1:
            lscx = media + (2.66 * rmedia)
            pass
        else:
            a2 = self.TABLE_SPC.getConstantTableSPC("a2", n)
            lscx = media + (a2 * rmedia)
            pass
        
        return lscx

    """
    Cálculo da Linha Central para as amplitudes (LCr)
    :param rmedia - amplitude média
    :return lcr - retorno da linha central das amplitudes 
    """
    def calcularLCr(self, rmedia):
        lcr = rmedia 
        return lcr

    """
    Cálculo do Limite Inferior de Controlo para as amplitudes (LICr)
    :param n - tamanho da amostra
    :param media - média
    :param rmedia - se n = 1 então rmedia é a amplitude móvel. se n > 1 então rmedia é a amplitude média
    :return licr = retorna o limite inferior de controlo para as amplitudes 
    """
    def calcularLICr(self, n, media, rmedia):
        licr = 0
        if n == 1:
            licr = 0
            #rmedia = amplitude móvel
            pass

        else:
            #rmedia = amplitude média
            d3 = self.TABLE_SPC.getConstantTableSPC("d3", n)
            licr = d3 * rmedia
            pass

        return licr

    """
    Cálculo do Limite Superior de Controlo para as amplitudes (LSCr)
    :param n - tamanho da amostra
    :param media - média
    :param rmedia - se n = 1 então rmedia é a amplitude móvel. se n > 1 então rmedia é a amplitude média
    :return lscr = retorna o limite superior de controlo para as amplitudes 
    """
    def calcularLSCr(self, n, media, rmedia):
        lscr = 0
        if n == 1:
            lscr = 3.267 * rmedia
            pass
        else:
            d4 = self.TABLE_SPC.getConstantTableSPC("d4", n)
            lscr = d4 * rmedia
            pass
        
        return lscr

    pass
