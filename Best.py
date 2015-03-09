# -*- encoding: utf-8 -*-
__author__ = 'fredy'


def SeleccionMejor(sel,best666,peso_max):
    nuevo=[]
    seleccionados=sel[:]
    seleccionados.sort(key=lambda x: x[-1])
    if len(best666)==0:
        b=seleccionados[0]
        nuevo=b[:]
    else:
        if seleccionados[0][-1] <= int(peso_max) and seleccionados[0][-2] > best666[-2]:
            b=seleccionados[0]
            nuevo=b[:]
        else:
            nuevo=best666[:]
    return nuevo