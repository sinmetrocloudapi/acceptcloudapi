#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from sys import getsizeof
from stats import models, estatisticas, cartacontrolo_xr, cartacontrolo_xs
from django import views
from collections import OrderedDict

class Estatistica_Geral:

    global IS_PRE_EMBALADOS
    global DICT_TOTAL_AMOSTRAS
    global DICT_ESTATISTICAS_AMOSTRAS
    global TAMANHO_AMOSTRA 
    global LIMITE_SUPERIOR_ESPECIFICACAO
    global LIMITE_INFERIOR_ESPECIFICACAO
    global QUANTIDADE_NOMINAL
    global PRIMEIRO_LIMITE_LEGAL
    global SEGUNDO_LIMITE_LEGAL
    global CASAS_DECIMAIS_VISIVEIS
    global PRECISAO_CALCULO

    global DICT_ESTUDO_CAPACIDADE 

    def main(self, isPreEmbalados, dictTotalAmostras, tamanhoAmostra, lse, lie, quantidadeNominal, tl1, tl2, casasDecimaisVisiveis, precisaoCalculo):
        self.IS_PRE_EMBALADOS = isPreEmbalados
        self.DICT_TOTAL_AMOSTRAS = dictTotalAmostras

        self.TAMANHO_AMOSTRA = tamanhoAmostra

        self.LIMITE_SUPERIOR_ESPECIFICACAO = lse
        self.LIMITE_INFERIOR_ESPECIFICACAO = lie 

        self.QUANTIDADE_NOMINAL = quantidadeNominal

        self.PRIMEIRO_LIMITE_LEGAL = tl1        
        self.SEGUNDO_LIMITE_LEGAL = tl2

        self.CASAS_DECIMAIS_VISIVEIS = casasDecimaisVisiveis
        self.PRECISAO_CALCULO = precisaoCalculo
    
        self.DICT_ESTUDO_CAPACIDADE = OrderedDict()

        calculos_estatisticos = estatisticas.Estatistica()
        calculos_estatisticos.main(self.PRECISAO_CALCULO)

        nPesagens = calculos_estatisticos.calcularN(self.DICT_TOTAL_AMOSTRAS) ##n = 100    

        nAmostras = calculos_estatisticos.calcularNAmostras(nPesagens, self.TAMANHO_AMOSTRA) #n:amostras = 25
    
        ##dicionário que contém toda a informação das pesagens por amostra
        g = globals()
        dictPerAmostra = self.splitPesagensPerAmostras(self.DICT_TOTAL_AMOSTRAS, nAmostras)

        self.DICT_ESTATISTICAS_AMOSTRAS = []

        estudoCapacidade = []

        if self.TAMANHO_AMOSTRA == 1:
            self.DICT_ESTATISTICAS_AMOSTRAS = []

            listaValoresAmostras = self.obterValoresAmostras(calculos_estatisticos, self.DICT_TOTAL_AMOSTRAS)

            totalAmostras = calculos_estatisticos.calcularN(self.DICT_TOTAL_AMOSTRAS)

            for j in range(0, totalAmostras):
                id = dictTotalAmostras[j]['id_amostra']
                valor = dictTotalAmostras[j]['valor']
                
                std = 0

                amplitudeMovel = calculos_estatisticos.calcularAmpMovel(listaValoresAmostras, j)

                self.DICT_ESTATISTICAS_AMOSTRAS.append({'idAmostra': id, 'n': self.TAMANHO_AMOSTRA, 'valor': valor, 'std': std, 'amplitude': amplitudeMovel})
                
                pass
            
        else:
            ##dicionário que contém toda a informação estatística por amostra
            self.DICT_ESTATISTICAS_AMOSTRAS = []

            for i in range(1, nAmostras + 1):
               
                globals()['listaAmostra_{0}'.format(i)] = dictPerAmostra[i-1]
                self.DICT_ESTATISTICAS_AMOSTRAS.append(self.estatisticasPorAmostra(calculos_estatisticos, globals()['listaAmostra_{0}'.format(i)], self.DICT_ESTATISTICAS_AMOSTRAS))
                pass
        
            #lista com os valores de todas as amostras
            listaValoresAmostras = self.obterValoresAmostras(calculos_estatisticos, self.DICT_TOTAL_AMOSTRAS)

            pass
    

        #estudo capacidade para todas as amostras
        estudoCapacidade = self.obterEstudoCapacidade(calculos_estatisticos, sorted(listaValoresAmostras))

        return estudoCapacidade

    def obterIdAmostra(self, estatistica, dictTotalAmostras):
        
        totalAmostras = estatistica.calcularN(dictTotalAmostras)

        id = 0
        for j in range(0, totalAmostras):
            valor = dictTotalAmostras[j]['id_amostra']
            pass

        return valor


    def obterValoresAmostras(self, estatistica, dictTotalAmostras):
        
        totalAmostras = estatistica.calcularN(dictTotalAmostras)

        listaValoresAmostras = []
        for j in range(0, totalAmostras):
            valor = dictTotalAmostras[j]['valor']
            listaValoresAmostras.append(valor)
            pass

        return listaValoresAmostras
    
 
    def obterDadosPorAmostra(self, idAmostra, tamanhoAmostra):

        listaAmostra = globals()['listaAmostra_{0}'.format(idAmostra)]
     
        listaValoresAmostra = []
        for j in range(0, tamanhoAmostra):
            n = listaAmostra[j]['n']
            valor = listaAmostra[j]['valor']
    
            listaValoresAmostra.append(valor)

        return listaValoresAmostra

    
    def estatisticasPorAmostra(self, estatistica, listaAmostras, dictEstatisticasPerAmostra):

        listaValoresPorAmostra = []
  
        for i in range(0, self.TAMANHO_AMOSTRA):
            idAmostra = listaAmostras[i]['id_amostra']
            n = listaAmostras[i]['n']
            valor = listaAmostras[i]['valor']

            listaValoresPorAmostra.append(valor)
            pass

        listaValoresPorAmostra = sorted(listaValoresPorAmostra)

        if self.TAMANHO_AMOSTRA == 1:
            std = 0

            amplitude = estatistica.calcularAmpMovel(listaValoresPorAmostra)

            dictEstatisticasPerAmostra = {'idAmostra':idAmostra, 'n': self.TAMANHO_AMOSTRA, 'std': std, 'amplitude': amplitude}
            
            pass
        else: 
            media = estatistica.calcularMedia(listaValoresPorAmostra)
            maximo = estatistica.calcularMaximo(listaValoresPorAmostra)
            minimo = estatistica.calcularMinimo(listaValoresPorAmostra)
            std = estatistica.calcularStd(listaValoresPorAmostra)
            amplitude = estatistica.calcularAmplitude(minimo, maximo)
        
            dictEstatisticasPerAmostra = {'idAmostra':idAmostra, 'n': self.TAMANHO_AMOSTRA, 'media': media, 'max': maximo, 'min': minimo, 'std': std, 'amplitude': amplitude}
            pass
        
        return dictEstatisticasPerAmostra

    def obterEstudoCapacidade(self, estatistica, dictTotalAmostras):
        
        result = []
        if self.IS_PRE_EMBALADOS == False: 
        
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "tamanho_amostra", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_amostras", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lie", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lse", dictTotalAmostras))

            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "media", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "minimo", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "maximo", dictTotalAmostras))
            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "amplitude", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "amp_media", self.DICT_ESTATISTICAS_AMOSTRAS))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "std", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "std_medio", self.DICT_ESTATISTICAS_AMOSTRAS))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "sigma", self.DICT_ESTATISTICAS_AMOSTRAS))

            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cp", dictTotalAmostras))         
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cpk", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cpk_sup", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cpk_inf", dictTotalAmostras))

           
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_lie", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_lse", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lie_n_lse", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "p_lie", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "p_lse", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lie_p_lse", dictTotalAmostras))
            ######################################################################################

            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "histograma", dictTotalAmostras))
           
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cartaxr", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cartaxs", dictTotalAmostras))
      
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "criteriolegalmedia", dictTotalAmostras))

            pass
        else:
            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "tamanho_amostra", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_amostras", dictTotalAmostras))
            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lie", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lse", dictTotalAmostras))
     
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "media", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "minimo", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "maximo", dictTotalAmostras))
            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "amplitude", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "amp_media", self.DICT_ESTATISTICAS_AMOSTRAS))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "std", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "std_medio", self.DICT_ESTATISTICAS_AMOSTRAS))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "sigma", self.DICT_ESTATISTICAS_AMOSTRAS))
            
            ######################################################################################

            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cp", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cpk", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cpk_sup", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cpk_inf", dictTotalAmostras))
            
            ######################################################################################
            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_lie", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_lse", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lie_n_lse", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "p_lie", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "p_lse", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "lie_p_lse", dictTotalAmostras))
    
            ######################################################################################
            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "tl1", dictTotalAmostras))        
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "tl2", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_tl1", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "n_tl2", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "per_tl1", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "per_tl2", dictTotalAmostras))

            ######################################################################################
            
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "histograma", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cartaxr", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "cartaxs", dictTotalAmostras))
            self.DICT_ESTUDO_CAPACIDADE.update(self.estatisticaPorParametro(estatistica, "criteriolegalmedia", dictTotalAmostras))
            
            pass      
        
        return self.DICT_ESTUDO_CAPACIDADE

    def estatisticaPorParametro(self, estatistica, parametro, listaDadosAmostra):   
        dictTESTE = []
    
        if parametro.upper() == 'TAMANHO_AMOSTRA':
            
            return self.jsonString("N", self.TAMANHO_AMOSTRA)

        elif parametro.upper() == 'N_AMOSTRAS':
            nPesagens = estatistica.calcularN(listaDadosAmostra)
            nAmostras = estatistica.calcularNAmostras(nPesagens, self.TAMANHO_AMOSTRA)
            
            return self.jsonString("nAmostras", nAmostras)

        elif parametro.upper() == 'N':
            n = estatistica.calcularN(listaDadosAmostra)

            return self.jsonString("n", n)

        elif parametro.upper() == 'LIE':
            std = estatistica.calcularStd(listaDadosAmostra)
            lie = estatistica.calcularLIE(self.LIMITE_INFERIOR_ESPECIFICACAO, self.QUANTIDADE_NOMINAL, std)
            
            return self.jsonString("lie", lie) 

        elif parametro.upper() == 'LSE':
            std = estatistica.calcularStd(listaDadosAmostra)
            lse = estatistica.calcularLIE(self.LIMITE_SUPERIOR_ESPECIFICACAO, self.QUANTIDADE_NOMINAL, std)

            return self.jsonString("lse", lse) 

        elif parametro.upper() == 'MEDIA':
            media = estatistica.calcularMedia(listaDadosAmostra)
       
            result = self.mostrarResultado(media, self.CASAS_DECIMAIS_VISIVEIS)

            return self.jsonString("media", result)   

        elif parametro.upper() == 'MAXIMO':
            maximo = estatistica.calcularMaximo(listaDadosAmostra)

            result = self.mostrarResultado(maximo, None)
  
            return self.jsonString("maximo", result)    
    
        elif parametro.upper() == 'MINIMO':
            minimo = estatistica.calcularMinimo(listaDadosAmostra)

            result = self.mostrarResultado(minimo, None)
   
            return self.jsonString("minimo", result)

        elif parametro.upper() == 'AMPLITUDE':
            minimo = estatistica.calcularMinimo(listaDadosAmostra)
            maximo = estatistica.calcularMaximo(listaDadosAmostra)
            amplitude = estatistica.calcularAmplitude(minimo, maximo)

            result = self.mostrarResultado(amplitude, self.CASAS_DECIMAIS_VISIVEIS)

            return self.jsonString("amplitude", result)

        elif parametro.upper() == 'AMP_MEDIA':
          
            amplitudeMedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)

            result = self.mostrarResultado(amplitudeMedia, self.CASAS_DECIMAIS_VISIVEIS)

            return self.jsonString("amplitudeMedia", result)
        
        elif parametro.upper() == 'STD':
            std = estatistica.calcularStd(listaDadosAmostra)

            result = self.mostrarResultado(std, self.CASAS_DECIMAIS_VISIVEIS + 1)

            return self.jsonString("std", result)
            
        elif parametro.upper() == 'STD_MEDIO':
            stdMedio =estatistica.calcularStdMedio(self.DICT_ESTATISTICAS_AMOSTRAS)

            result = self.mostrarResultado(stdMedio, self.CASAS_DECIMAIS_VISIVEIS + 1)

            return self.jsonString("stdMedio", result)
        elif parametro.upper() == 'SIGMA':
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)

            result = self.mostrarResultado(sigma, self.CASAS_DECIMAIS_VISIVEIS + 1)

            return self.jsonString("sigma", result)

        elif parametro.upper() == 'CP':
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            cp = estatistica.calcularCp(self.LIMITE_SUPERIOR_ESPECIFICACAO, self.LIMITE_INFERIOR_ESPECIFICACAO, sigma)

            result = self.mostrarResultado(cp, self.CASAS_DECIMAIS_VISIVEIS)

            return self.jsonString("cp", result)   
  
        elif parametro.upper() == 'CPK':
            media = estatistica.calcularMedia(listaDadosAmostra)
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            cpk1 = estatistica.calcularCpkSup(media, self.LIMITE_SUPERIOR_ESPECIFICACAO, sigma)
            cpk2 = estatistica.calcularCpkInf(media, self.LIMITE_INFERIOR_ESPECIFICACAO, sigma)
            cpk = estatistica.calcularCpk(cpk1, cpk2)

            result = self.mostrarResultado(cpk, self.CASAS_DECIMAIS_VISIVEIS)
            
            return self.jsonString("cpk", result) 

        elif parametro.upper() == 'CPK_SUP':
            media = estatistica.calcularMedia(listaDadosAmostra)
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            cpk_sup = estatistica.calcularCpkSup(media, self.LIMITE_SUPERIOR_ESPECIFICACAO, sigma)

            result = self.mostrarResultado(cpk_sup, self.CASAS_DECIMAIS_VISIVEIS)

            return self.jsonString("cpk_sup", result) 
        elif parametro.upper() == 'CPK_INF':
            media = estatistica.calcularMedia(listaDadosAmostra)
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            cpk_inf = estatistica.calcularCpkInf(media, self.LIMITE_INFERIOR_ESPECIFICACAO, sigma)
       
            result = self.mostrarResultado(cpk_inf, self.CASAS_DECIMAIS_VISIVEIS)
   
            return self.jsonString("cpk_inf", result) 

        elif parametro.upper() == 'N_LIE':
            n_lie = estatistica.calcularNLIE(listaDadosAmostra, self.LIMITE_INFERIOR_ESPECIFICACAO)
        
            return self.jsonString("n_lie", n_lie) 

        elif parametro.upper() == 'N_LSE':
            n_lse = estatistica.calcularNLSE(listaDadosAmostra, self.LIMITE_SUPERIOR_ESPECIFICACAO)
           
            return self.jsonString("n_lse", n_lse)

        elif parametro.upper() == 'LIE_N_LSE':
            lie_n_lse = estatistica.calcularLIENLSE(listaDadosAmostra, self.LIMITE_INFERIOR_ESPECIFICACAO, self.LIMITE_SUPERIOR_ESPECIFICACAO)
         
            return self.jsonString("lie_n_lse", lie_n_lse)
     
        elif parametro.upper() == 'P_LSE':
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            media = estatistica.calcularMedia(listaDadosAmostra)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            p_lse = estatistica.calcularPLSE(self.LIMITE_SUPERIOR_ESPECIFICACAO, media, sigma)
            
            result = round(p_lse, 2)
     
            return self.jsonString("p_lse", "{0} %".format(result))
            
        elif parametro.upper() == 'P_LIE':

            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            media = estatistica.calcularMedia(listaDadosAmostra)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
       
            p_lie = estatistica.calcularPLIE(self.LIMITE_INFERIOR_ESPECIFICACAO, media, sigma)
            
            result = round(p_lie, 2)
  
            return self.jsonString("p_lie", "{0} %".format(result))

        elif parametro.upper() == 'LIE_P_LSE':
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            media = estatistica.calcularMedia(listaDadosAmostra)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            p_lie = estatistica.calcularPLIE(self.LIMITE_INFERIOR_ESPECIFICACAO, media, sigma)
            p_lse = estatistica.calcularPLSE(self.LIMITE_SUPERIOR_ESPECIFICACAO, media, sigma)
            lie_p_lse = estatistica.calcularLIEPLSE(p_lie, p_lse)
            result = round(lie_p_lse, self.CASAS_DECIMAIS_VISIVEIS)

            return self.jsonString("lie_p_lse", "{0} %".format(result))

        elif parametro.upper() == 'TL1':
            tl1 = estatistica.calcularTL1(self.QUANTIDADE_NOMINAL, self.PRIMEIRO_LIMITE_LEGAL)
 
            return self.jsonString("tl1", tl1)

        elif parametro.upper() == 'TL2':
            tl2 = estatistica.calcularTL2(self.QUANTIDADE_NOMINAL, self.SEGUNDO_LIMITE_LEGAL)

            return self.jsonString("tl2", tl2)
        
        elif parametro.upper() == 'N_TL1':
            tl1 = estatistica.calcularTL1(self.QUANTIDADE_NOMINAL, self.PRIMEIRO_LIMITE_LEGAL)
            n_tl1 = estatistica.calcularNTL(listaDadosAmostra, tl1)
            
            return self.jsonString("n_tl1", n_tl1)

        elif parametro.upper() == 'N_TL2':
            tl2 = estatistica.calcularTL2(self.QUANTIDADE_NOMINAL, self.SEGUNDO_LIMITE_LEGAL)
            n_tl2 = estatistica.calcularNTL(listaDadosAmostra, tl2)

            return self.jsonString("n_tl2", n_tl2)

        elif parametro.upper() == 'PER_TL1':
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            media = estatistica.calcularMedia(listaDadosAmostra)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            tl1 = estatistica.calcularTL1(self.QUANTIDADE_NOMINAL, self.PRIMEIRO_LIMITE_LEGAL)
            per_tl1 = estatistica.calcularPerTL(tl1, media, sigma)
            result = round(per_tl1, self.CASAS_DECIMAIS_VISIVEIS)

            return self.jsonString("per_tl1", "{0} %".format(result))

        elif parametro.upper() == 'PER_TL2':
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            media = estatistica.calcularMedia(listaDadosAmostra)
            sigma = estatistica.calcularSigma(rmedia, self.TAMANHO_AMOSTRA)
            tl2 = estatistica.calcularTL2(self.QUANTIDADE_NOMINAL, self.SEGUNDO_LIMITE_LEGAL)
            per_tl2 = estatistica.calcularPerTL(tl2, media, sigma)
            
            result = round(per_tl2, self.CASAS_DECIMAIS_VISIVEIS)
     
            return self.jsonString("per_tl2", "{0} %".format(result))
        ########################################################################################################################
        
        elif parametro.upper() == 'HISTOGRAMA':       

            return self.jsonHistogram(estatistica, listaDadosAmostra) 

        elif parametro.upper() == 'CARTAXR':
      
            media = estatistica.calcularMedia(listaDadosAmostra)
            rmedia = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
            
            cartaControloXR = cartacontrolo_xr.CartaControloXR()

            return cartaControloXR.main(n=self.TAMANHO_AMOSTRA, media=media, rmedia=rmedia, casasdecimais = self.CASAS_DECIMAIS_VISIVEIS)

        elif parametro.upper() == 'CARTAXS':
            media = estatistica.calcularMedia(listaDadosAmostra)
            stdMedio = estatistica.calcularStdMedio(self.DICT_ESTATISTICAS_AMOSTRAS)
           
            cartaControloXS = cartacontrolo_xs.CartaControloXS()

            return cartaControloXS.main(n=self.TAMANHO_AMOSTRA, media=media, std=stdMedio, casasdecimais = self.CASAS_DECIMAIS_VISIVEIS)

        elif parametro.upper() == 'CRITERIOLEGALMEDIA':
            
            n = estatistica.calcularN(listaDadosAmostra)
            media = estatistica.calcularMedia(listaDadosAmostra) 
            sc = 0
            
            if self.TAMANHO_AMOSTRA == 1:
                sc = estatistica.calcularAmpMedia(self.DICT_ESTATISTICAS_AMOSTRAS)
                pass
            else:
                sc = estatistica.calcularStdMedio(self.DICT_ESTATISTICAS_AMOSTRAS)
                pass

            k = estatistica.obterK(n)

            criterio_legal_media, validacao = estatistica.verificarCriterioLegal(self.QUANTIDADE_NOMINAL, k, sc, media)
            
            return self.jsonCriterioLegalMedia(media, criterio_legal_media, validacao)
           
        ########################################################################################################################
        else:
            return ""

        pass

    def splitPesagensPerAmostras(self, alist, wanted_parts=1):
        length = len(alist)

        return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts)]

    pass

    def mostrarResultado(self, valor, casasdecimais):
        resultado = 0
        if(casasdecimais == None):
            resultado = valor
        else: 
            resultado = round(valor, casasdecimais)
        
        if resultado % 1 == 0:
            return int(resultado)
        else: 
            return resultado

    def jsonString(self, nome, valor):
        newItem ={}
        newItem[nome] = valor

        return newItem

    def jsonHistogram(self, estatistica, listaAmostras):
        xMin, sizeBucket, listaBuckets = estatistica.calcularHistograma(listaAmostras)
    
        dictHistograma = {}
        dictHistograma["dados_histograma"] = {
            
            'xMin' : xMin,
            'sizeBucket' : round(sizeBucket, self.CASAS_DECIMAIS_VISIVEIS), 
            'listaBuckets' : list(listaBuckets)
            }

        return dictHistograma

    def jsonCriterioLegalMedia(self, media, criterio, validacaocriteriolegal):
        
        dictCriterioLegalMedia = {}
        dictCriterioLegalMedia["criteriolegalmedia"] = {
            
            'media' : media,
            'criterio' : criterio, 
            'validacaocriteriolegal' : validacaocriteriolegal
            }

        return dictCriterioLegalMedia

    
       
