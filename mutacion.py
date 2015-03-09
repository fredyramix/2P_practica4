# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import random


def Mutacion(cruz,num_cromo,n):
    #print n
    #print num_cromo
    #for x in cruz:
    #    print x
    num=random.randrange(0,int(num_cromo)-1)
    #print num
    #print cruz[num]
    num_articulo=random.randrange(0,len(cruz[num])-1)
    #print num_articulo
    #print cruz[num][num_articulo]
    pos=random.randrange(0,2)
    #print pos
    #print cruz[num][num_articulo][pos]
    #a=cruz[num][num_articulo][pos]
    if pos==0:
        if cruz[num][num_articulo][pos]==0:
            cruz[num][num_articulo][pos]=1
        else:
            cruz[num][num_articulo][pos]=0
    if pos==1:
        cruz[num][num_articulo][pos]=random.randint(1,n)


    #print cruz[num]
    #print "===="
    #for x in cruz:
    #   print x
    #raw_input("Esperad")
    return cruz

