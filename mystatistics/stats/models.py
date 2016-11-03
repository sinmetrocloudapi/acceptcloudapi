#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import pymysql

class Database():

    #NAME_DATABASE = "dbpesagens1"
    #NAME_DATABASE = "dbpesagens_ex_n3"
    #NAME_DATABASE = "dbpesagens_ex_n3_neg"
    #NAME_DATABASE = "dbpesagens4"
    NAME_DATABASE = "dbpesagens_ex_gml"

    TABLE_AMOSTRAS = "amostras"
    TABLE_PESAGENS = "pesagens"

    def connectionDB(self):
        conn = pymysql.connect(user='root', passwd='root', db= self.NAME_DATABASE)
        return conn        

    def getAllAmostras(self, one=False):

        connection_database = self.connectionDB()

        cursor = connection_database.cursor()
        query = ("SELECT * FROM {0}.{1}").format(self.NAME_DATABASE, self.TABLE_PESAGENS)
        cursor.execute(query)

        r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]

        cursor.close()
        return (r[0] if r else None) if one else r
   
    pass
    