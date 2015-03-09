# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from random import randrange
import random

def LeerArticulos():
    dic={}
    archi=open('articulos.txt','r')
    linea="a"
    c=1
    while linea!="":
        try:
            linea=archi.readline()
            listita=[]
            a=linea.split(',')
            b=a[3]
            d=b[:-1]
            listita.append(int(a[0]))
            listita.append(int(a[1]))
            listita.append(int(a[2]))
            listita.append(d)
            dic[c]=listita
            c=c+1
        except IndexError,e:
            pass #encontro un salto de linea.
    archi.close()
    return dic

def PrimeraGeneracionAleatoria(all,num_cromo):
    primera=[]
    prueba=all.items()
    prueba.sort(key=lambda x:x[1][-1])
    n= prueba[-1][-1][-1] # donde n es el numero mayor que tendrán nuestros articulos. en cuanto a existencia
    for x in range(0,int(num_cromo)):
        cromosoma=[]
        for i in range(len(all)):
            bandera=random.randrange(0,2)
            if bandera==1:
                existencia=random.randrange(1,n+1)
            else:
                existencia=0
            pareja=[bandera,existencia]
            cromosoma.append(pareja)
        primera.append(cromosoma)
    return primera,n


def Imprimir(lista):
    pass
    #print "============================================================================================================="
    #for i in lista:
    #    print i
    #print "============================================================================================================="
def ImprimirBest(best):
    pass
    #print "============================================================================================================="
    #print best
    #print "=