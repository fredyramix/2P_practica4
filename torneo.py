# -*- encoding: utf-8 -*-
from funciones import Imprimir

__author__ = 'fredy'
import random


def Torneo(funcion_penalizada):
    p=[]
    tam=len(funcion_penalizada)
    for x in funcion_penalizada:
        x.append(random.randint(0,tam-1))
        p.append(x)
    #se asigno una pareja al azar para producir el torneo.
    Imprimir(funcion_penalizada)
    seleccionados=[]
    for y in p:
        h=y[-1]
        p[h]
        if y[-4] < p[h][-4]:
            seleccionados.append(y[:-1])
        else:
            seleccionados.append(p[h][:-1])
    return seleccionados