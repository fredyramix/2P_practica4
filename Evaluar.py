# -*- encoding: utf-8 -*-
__author__ = 'fredy'


def EvaluarFX(primera,tabla):
    #Cromosoma = [ (1,3), (0,0) , (8,9).....n , peso , importancia ]
    p=[]
    for x in primera:
        peso=0
        importancia=0
        c=1
        for y in x:
            if y[0]==1:
                pes= tabla[c][0]*y[1] #multiplicamos cada costo e importancia por el numero de articulos que estamos ocupando
                impor= tabla[c][1]*y[1]
                peso = peso + int(pes)
                importancia = importancia + int(impor)
            c=c+1
        x.append(peso)
        x.append(importancia)
        p.append(x)
    return p