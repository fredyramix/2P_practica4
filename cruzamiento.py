# -*- encoding: utf-8 -*-
__author__ = 'fredy'

def Cruzamiento(seleccionados):
    sel = []
    for x in seleccionados:
        y=x[:-3]
        sel.append(y)
    #es para eliminar los datos que ya no nos sirven
    mitad= len(sel)/2
    cruzados=[]
    while len(sel) != 0:
        mitad1=sel[0][0:mitad]
        mitad2=sel[0][mitad:]
        mitad3=sel[1][0:mitad]
        mitad4=sel[1][mitad:]
        cruzados.append(mitad1+mitad4)
        cruzados.append(mitad3+mitad2)
        del sel[0]
        del sel[0]
    return cruzados