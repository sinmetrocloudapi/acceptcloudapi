#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import statistics
import numpy
import math
import scipy
from scipy.stats import norm

import plotly
import plotly.graph_objs as go

import matplotlib.pyplot as plt

from stats import models, table_spc
from django import views
from django.http.request import HttpRequest
from statistics import mean, pstdev

""" 
    Classe destinada aos cálculos estatísticos
"""
class Estatistica:
    
    TABLE_SPC = table_spc.TableSPC()
    global PRECISAO_CALCULO
    
    def main(self, precisaoCalculo):
        self.PRECISAO_CALCULO = precisaoCalculo
        pass
        
    #####
    #Nível 1
    #####
    """
    Cálculo do tamanho da amostra
    
    :param lista: lista com os valores das amostras
    :return tamanhoAmostra: retorna o tamanho da amostra
    """
    def calcularTamanhoAmostra(self, lista):
        nPesagens = self.calcularN(lista)
        nAmostras = self.calcularNAmostras(lista)
        
        tamanhoAmostra = nPesagens / nAmostras 
        return tamanhoAmostra

    """
    Cálculo do número de amostras realizadas

    :param nPesagens: número de pesagens
    :param tamanhoAmostra: tamanho da amostra
    :return nAmostras: retorna o número de amostras realizadas
    """
    def calcularNAmostras(self, nPesagens, tamanhoAmostra):
        nAmostras = nPesagens / tamanhoAmostra
        return nAmostras

    """
    Cálculo do número de pesagens realizadas
    
    :param lista: lista com os valores das pesagens
    :return n: retorna o número total de pesagens
    """
    def calcularN(self, lista):
        n = len(lista)
        return n
    
    """
    Cálculo da média

    :param lista: lista com os valores das pesagens/amostras
    :return media: retorna a média 
    """
    def calcularMedia(self, lista):
        media = mean(lista)
        return self.precisaoCalculo(media)

    """
    Cálculo do máximo 

    :param lista: lista com os valores das pesagens/amostras
    :return maximo: retorna o máximo
    """
    def calcularMaximo(self, lista):
        maximo = max(lista)
        return maximo

    """
    Cálculo do mínimo

    :param lista: lista com os valores das pesagens/amostras
    :return minimo: retorna o minimo
    """
    def calcularMinimo(self, lista):
        minimo = min(lista)
        return minimo
    
    """
    Cálculo da Amplitude

    :param min: mínimo
    :param max: max
    :return amplitude: retorna a amplitude
    """
    def calcularAmplitude(self, min, max):
        amplitude = float(max - min)
        return self.precisaoCalculo(amplitude)

    """
    Cálculo da amplitude média
    Obtém os valores da amplitude de cada amostra e calcula a média desses valores. 
    
    :param lista: lista com os valores de cada amostra
    :return amplitudeMedia: retorna a amplitude média 
    """
    def calcularAmpMedia(self, lista):

        listaValoresAmplitudePorAmostra = []

        nAmostras = len(lista)

        for j in range(0, nAmostras):
            valor = lista[j]['amplitude']
            if valor == None:
                pass
            else:
                listaValoresAmplitudePorAmostra.append(valor)
                pass
            pass

        amplitudeMedia = self.calcularMedia(listaValoresAmplitudePorAmostra)

        return self.precisaoCalculo(amplitudeMedia)
    """
    Cálculo da amplitude móvel para quando o tamanho da amostra é igual a 1 

    :param lista: lista com os valores de cada amostra
    :param index: posição na lista de valores
    return amplitudeMovel
    """
    def calcularAmpMovel(self, lista, index):

        nAmostras = len(lista)
        amplitudeMovel = 0

        if index == 0:
            amplitudeMovel = None
            pass
        else:
            for i in range(0, nAmostras):
                if i == index:
                    amplitudeMovel = abs(lista[index] - lista[index-1])
                    break
                pass
            pass

        return amplitudeMovel

    """
    Cálculo do desvio padrão corrigido

    :param lista: lista com os valores das pesagens
    :return desvio-padrão: retorna o desvio-padrão corrigido
    """
    def calcularStd(self, lista):
        std = numpy.std(lista, ddof=1)
        return self.precisaoCalculo(std)
    
    """
    Cálculo do desvio-padrão médio
    Óbtem os valores do desvio-padrão de cada amostra e cálcula a sua média

    :param lista: lista com os valores de cada amostra
    :return stdMedio: retorna o desvio-padrão médio
    """
    def calcularStdMedio(self, lista):
        nAmostras = len(lista)

        listaValoresStdPorAmostra = []
        for j in range(0, nAmostras):
            valor = lista[j]['std']
            listaValoresStdPorAmostra.append(valor)
            pass

        stdMedio = self.calcularMedia(listaValoresStdPorAmostra)
        
        return self.precisaoCalculo(stdMedio)

    #####
    #Nível 2
    #####
    """
    Cálculo do sigma

    :param rmedia: amplitude média
    :param n: tamanho da amostra
    :return sigma: retorna o sigma
    """
    def calcularSigma(self, rmedia, n):

        d2p = 0
        if n == 1:
            d2p = 1.128
            pass
        else:
            d2p = self.TABLE_SPC.getConstantTableSPC("d2pequeno", n)
            pass
          
        sigma =   rmedia / d2p   
        
        return self.precisaoCalculo(sigma)

    """
    CP - Capacidade do Processo (Taxa de tolerância (a largura dos limites de especificação) à variação atual (tolerância do processo)
    (LSE - LSI) / (6 * sigma)
    
    :param lse: limite superior de especificação
    :param lie: limite inferior de especificação
    :param sigma: sigma
    :return cp: retorna a cp
    """
    def calcularCp(self, lse, lie, sigma):
        cp = (lse - lie) / (6 * sigma)
        return self.precisaoCalculo(cp)

    """
    CPK - Capacidade do Processo (Taxa de tolerância (a largura dos limites de especificação) à variação atual, considerando a média do processo relativa ao ponto médio das especificações.)
    
    :param cpk1 - capacidade do processo superior
    :param cpk2 - capacidade do processo inferior
    :return cpk: retorna a cpk
    """
    def calcularCpk(self, cpk1, cpk2):
        cpk = min(cpk1, cpk2)
        return self.precisaoCalculo(cpk)

    """
    CPK Sup- Capacidade do Processo (Taxa de tolerância (a largura dos limites de especificação) à variação atual, considerando a média do processo relativa ao ponto médio das especificações.)
    
    :param media: média
    :param lse: limite superior de especificação
    :param sigma: sigma
    :return cpk: retorna a cpk superior
    """
    def calcularCpkSup(self, media,  lse, sigma):
        cpkSup = (lse - media) / (3 * sigma)
        return self.precisaoCalculo(cpkSup)
    
    """
    CPK Inf- Capacidade do Processo (Taxa de tolerância (a largura dos limites de especificação) à variação atual, considerando a média do processo relativa ao ponto médio das especificações.)
    
    :param media: média
    :param lse: limite inferior de especificação
    :param sigma: sigma
    :return cpkInf: retorna a cpk inferior
    """
    def calcularCpkInf(self, media, lie, sigma):
        cpkInf = (media - lie) / (3 * sigma)
        return  self.precisaoCalculo(cpkInf)

    """
    Cálculo do Limite Inferior de Especificação
        
    :param lie - limite inferior de especificação
    :return lie - limite inferior de especificação
    """
    def calcularLIE(self, lie, quantidadeNominal, std):
        if lie == None:
            return quantidadeNominal - (3 * std)
        else:
            return lie
            
        pass

    """
    Cálculo do Limite Superior de Especificação
        
    :param lie - limite superior de especificação
    :return lie - limite superior de especificação
    """
    def calcularLSE(self, lse, quantidadeNominal, std):
        if lse == None:
            return quantidadeNominal + (3 * std)
        else:
            return lse
            
        pass

    """
    Cálculo do número de amostras inferiores ao limite inferior de especificação

    :param lista: lista com os valores das amostras
    :param lie: limite inferior de especificação
    :return n_lie: retorna o número de amostras inferiores a lie
    """
    def calcularNLIE(self, lista, lie):
        n_lie = 0

        for x in range(0, len(lista)): 
            if lista[x] < lie:
                n_lie = n_lie + 1
                pass
            pass
        return n_lie   
    

    """
    Cálculo do número de amostras superiores ao limite superior de especificação
    :param lista: lista com os valores das amostras
    :param lse: limite superior de especificação
    :return n_lse: retorna o número de amostras superiores a lse
    """
    def calcularNLSE(self, lista, lse):
        n_lse = 0

        for x in range(0, len(lista)): 
            if lista[x] > lse:
                n_lse = n_lse + 1
                pass
            pass
        return n_lse   

    """
    Cálculo do número de amostras entre o limite inferior e o limite superior de especificação

    :param lista: lista com os valores das amostras
    :param lie: limite inferior de especificação
    :param lse: limite superior de especificação
    :return lie_n_lse: retorna o número de amostras entre lie e lse
    """
    def calcularLIENLSE(self, lista, lie, lse):
        lie_n_lse = 0

        for x in range(0, len(lista)): 
            if lista[x] >= lie and lista[x] <= lse:
                lie_n_lse = lie_n_lse + 1
                pass
            pass
        return lie_n_lse
            
    """
    Cálculo da distribuição normal cumulativa (normcdf)
    
    :param le: limite de especificação (superior ou inferior)
    :param media: média
    :param sigma: sigma
    :return p_lie: retorna a percentagem dos valores das amostras inferiores ao lie
    """
    def normcdf(self, le, media, sigma):
        t = le-media;
        normcdf = 0.5 * math.erfc(-t/(sigma* math.sqrt(2.0)))
        if normcdf>1.0:
            normcdf = 1.0;
        return normcdf

    """
    Cálculo da percentagem de valores das amostras inferiores ao limite inferior de especificação
    
    :param lie: limite inferior de especificação
    :param media: média
    :param sigma: sigma
    :return p_lie: retorna a percentagem dos valores das amostras inferiores ao lie
    """
    def calcularPLIE(self, lie, media, sigma):
        p_lie = 0
        valorAux = 0

        if sigma > 0:
            valorAux = self.normcdf(lie, media, sigma)
            p_lie = round(valorAux * 100, 2)
            pass
        else:
            p_lie = 0
            pass

        return p_lie

    """
    Cálculo da percentagem de valores das amostras superioes ao limite superior de especificação
    
    :param lse: limite superior de especificação
    :param media: média
    :param sigma: sigma
    :return p_lse: retorna a percentagem dos valores das amostras superiores ao lse
    """
    def calcularPLSE(self, lse, media, sigma):
        p_lse = 0
        valorAux = 0

        if sigma > 0:
            valorAux = 1 - self.normcdf(lse, media, sigma)
            p_lse = round(valorAux * 100, 2)
            pass
        else:
            p_lse = 0
            pass

        return p_lse

    """
    Cálculo da percentagem de valores entre o limite inferior e o limite superior de especificação
    
    :param p_lie: limite inferior de especificação
    :param p_lse: limite superior de especificação
    :return lie_p_lse: retorna a percentagem dos valores das amostras entre lie e lse
    """
    def calcularLIEPLSE(self, p_lie, p_lse):
        
        lie_p_lse = 100 - (p_lie + p_lse)
        return lie_p_lse

    """
    Cálculo do Erro Admissível por Defeito

    :param quantidadeNominal - quantidade nominal (em gramas ou mililitro)
    :return ead - retorna o erro admissível por defeito
    """
    def calcularEAD(self, quantidadeNominal):
        ead = 0

        if quantidadeNominal < 50:
            ead = quantidadeNominal * 0.09
            pass
        elif quantidadeNominal >= 50 and quantidadeNominal < 100:
            ead = 4.5
            pass
        elif quantidadeNominal >= 100 and quantidadeNominal < 200:
            ead = 0.045
            pass
        elif quantidadeNominal >= 200 and quantidadeNominal < 300:
            ead = 9.0
            pass
        elif quantidadeNominal >= 300 and quantidadeNominal < 500:
            ead = 0.03
            pass
        elif quantidadeNominal>= 500 and quantidadeNominal < 100:
            ead = 15.0
            pass
        elif quantidadeNominal >= 1000 and quantidadeNominal < 10000:
            ead = 0.015
            pass
        elif quantidadeNominal >= 10000 and quantidadeNominal < 15000:
            ead = 150.0
            pass
        elif quantidadeNominal >= 15000:
            ead = 0.01
            pass
        
        return ead

    """
    Cálculo do 1º Limite Legal (TL1)

    :param quantidadeNominal - quantidade nominal (em gramas ou mililitros)
    :param tl1 - 1º limite legal
    :return tl1 - retorna o 1º limite legal
    """
    def calcularTL1(self, quantidadeNominal, tl1):
        if tl1 != None:
            return tl1
        else:
            ead = self.calcularEAD(quantidadeNominal)
            tl1 = quantidadeNominal - ead
            return tl1

        pass
    
    """
    Cálculo do 2º Limite Legal (TL2)

    :param quantidadeNominal - quantidade nominal (em gramas ou mililitros)
    :param tl2 - 2º limite legal
    :return tl2 - retorna o 2º limite legal
    """
    def calcularTL2(self, quantidadeNominal, tl2):

        if tl2 != None:
            return tl2 
        else:
            ead = self.calcularEAD(quantidadeNominal)
            tl2 = quantidadeNominal - (2 * ead)
            return tl2
        pass
      
    """
    Cálculo do número de amostras inferiores ao limite legal ( 1º limite ou 2º limite legal)
    :param lista: lista com os valores das amostras
    :param tl: limite legal (1º ou 2º limite legal
    :return n_tl: retorna o número de amostras inferiores ao limite legal
    """
    def calcularNTL(self, lista, tl):
        n_tl = 0

        for x in range(0, len(lista)): 
            if lista[x] < tl:
                n_tl = n_tl + 1
                pass
            pass
        return n_tl
  
    """
    Cálculo da percentagem de amostras inferiores ao Limite Legal (TL)

    :param tl - limite legal (1º limite ou 2º limite legal)
    :param media - média
    :param sigma  sigma
    :return p_tl: retorna percentagem dos valores das amostras inferiores a tl
    """
    def calcularPerTL(self, tl, media, sigma):
        p_tl = 0
        valorAux = 0

        if sigma > 0:
            valorAux = self.normcdf(tl, media, sigma)
            p_tl = round(valorAux * 100, 2)
            pass
        else:
            p_tl = 0
            pass

        return p_tl

    
    #############################################################################
    #Critério legal da média
    #############################################################################
    '''
    Obter K
    :param n - número total de pesagens
    :return k - k
    '''
    def obterK(self, n):  
        k = 0
        
        if n > 1:
            t = scipy.stats.t
            normInv = t.ppf(0.005, n - 1)
            k = abs(normInv / math.sqrt(n))

        return k

    """
    Verificar se os parâmetros recebidos verificam o critério legal
    :param quantidadeNominal - quantidade nominal
    :param k -
    :param sc - desvio padrao medio (n>1) ou amplitude movel (n=1)
    :param media - media
    :return result - retorna True se parâmetros passarem no critério legal. caso contrário, retorna falso
    """
    def verificarCriterioLegal(self, quantidadeNominal, k, sc, media):

        criterio = round(quantidadeNominal - k * sc, 2)

        #casas decimais pode ser passada como parametro; para gmL é sempre 2
        if media >= criterio:
            result = True
            pass
        else:
            result = False
            pass

        return criterio, result

    """
    Calcular histograma
    :param lista - lista de valores
    :return xMin - valor min (eixo do x) - valor onde começa o histograma
    :return sizeBucket - tamanho da barra
    :return listaBuckets - lista de barras
    """
    def calcularHistograma(self, lista):

        n = len(sorted(lista))
        k = math.sqrt(n)
        ki = int(round(k)) # número de baldes

        a, binEdges = numpy.histogram(lista, bins = ki)
 
        xMin = self.calcularMinimo(binEdges)
  
        sizeBucket = binEdges[1] - binEdges[0]
    

        listaBuckets = a
        

        #############################################################
        #Desenha o histograma 

        #plt.hist(lista, bins=binEdges)  # plt.hist passes it's arguments to np.histogram
        #plt.show()

        return xMin, sizeBucket, listaBuckets

    ############################################################################# 
    ############################################################################# 
    ############################################################################# 
    #############################################################################      
    """
    Define o resultado do cálculo estatístico com uma precisão de 15 casas decimais

    :param valor - resultado do cálculo estatístico
    :return result - retorna o resultado com uma precisão de 15 casas decimais 
    """  
    def precisaoCalculo(self, valor):
        result = 0
        if float(valor) % 1 == 0:
            result = int(valor)
            pass
        else: 
            strResult = "{0:.15f}".format(valor)
            result = float(strResult)
            pass
        
        return result
        
