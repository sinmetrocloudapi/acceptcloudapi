#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from BeautifulSoup import BeautifulSoup

import os, sys
import simplejson
import numpy
import statistics

from stats import models, estatisticas, estatistica_geral
from django import views
from django.http.request import HttpRequest
from statistics import mean, pstdev
import collections

def index(request):
    
    db = models.Database()
    stats = estatisticas.Estatistica()

    conn = db.connectionDB()

    ##dicionário com toda a informação das pesagens (consulta à base de dados)
    dictTotalAmostras = db.getAllAmostras()

    estatistica_parent = estatistica_geral.Estatistica_Geral()

    #n = 1
    #result = estatistica_parent.main(False, dictTotalAmostras, tamanhoAmostra = 1, lse = 8, lie = 4, quantidadeNominal = 750, tl1 = None, tl2 = None, casasDecimaisVisiveis = 2, precisaoCalculo = 15)
    
    #n = 3
    #result = estatistica_parent.main(False, dictTotalAmostras, tamanhoAmostra = 3, lse = 24.28, lie = 23.91, quantidadeNominal = 750, tl1 = None, tl2 = None, casasDecimaisVisiveis = 3, precisaoCalculo = 15)
    
    #n = 3 (numeros negativos)
    #result = estatistica_parent.main(False, dictTotalAmostras, tamanhoAmostra = 3, lse = 0.05, lie = -0.15, quantidadeNominal = 750, tl1 = None, tl2 = None, casasDecimaisVisiveis = 3, precisaoCalculo = 15)
    
    #n = 4
    #result = estatistica_parent.main(True, dictTotalAmostras, tamanhoAmostra = 4, lse = 756, lie = 744, quantidadeNominal = 750, tl1 = 735, tl2 = 720, casasDecimaisVisiveis = 3, precisaoCalculo = 15)

    #n = 4 (gml)
    result = estatistica_parent.main(True, dictTotalAmostras, tamanhoAmostra = 4, lse = 1006, lie = 994, quantidadeNominal = 1000, tl1 = 735, tl2 = 720, casasDecimaisVisiveis = 2, precisaoCalculo = 15)
    
    obj = simplejson.dumps(result, ensure_ascii=False, sort_keys=True, indent=4)
    
    return HttpResponse(obj, content_type ="application/json")

    pass
