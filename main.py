# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from funciones import *
from Evaluar import *
from Penalizar import *
from Torneo import *
from Best import *
from mutacion import *
from cruzamiento import Cruzamiento
def main():
    tabla=LeerArticulos() #obtener la tabla de articulos
    #all contiene la forma: {1:[3,4,5]} donde 1 es su llave o numero de articulo 3 es su peso, 4 su importancia y 5 la cantidad.
    print tabla
    #Definir primera generacion aleatoria donde tomaremos el numero maximo de la cantidad de productos para que sea
    #nuestro tamaño del cromosoma
    num_cromo=raw_input("Introduzca el numero de cromosomas:\n")
    peso_max=raw_input("Ingrese el peso maximo de la caja:\n")
    primera,n=PrimeraGeneracionAleatoria(tabla,num_cromo)
    Imprimir(primera)
    num_gen=raw_input("Ingrese el numero de generaciones:\n")
    c=1
    print "Comienza algoritmo genetico esto puede llevar algunos minutos por favor espere..."
    best=[]
    while c!=int(num_gen):
        #comienza ciclo.
        #Evaluar funcion de x
        funcion_evaluada=EvaluarFX(primera,tabla)
        #Cromosoma = [ (1,3), (0,0) , (8,9).....n , peso , importancia ] ya multiplicando el peso y la importancia por el numero de existencias
        #Siguiente paso Penalizar !
        funcion_penalizada=Penalizar(funcion_evaluada,tabla,peso_max)
        Imprimir(funcion_penalizada)
        #Siguiene paso selección por torneo..
        seleccionados=Torneo(funcion_penalizada)
        Imprimir (seleccionados)
        #Seleccionar el mejor de todos :D
        best666=SeleccionMejor(seleccionados,best,peso_max)
        best=best666[:]
        ImprimirBest(best)
        #Proceso de cruzamiento.
        cruzados=Cruzamiento(seleccionados)
        Imprimir(cruzados)
        ImprimirBest(best)
        #continua proceso de mutacion.
        mut=Mutacion(cruzados,num_cromo,n)
        mutados=mut[:]
        Imprimir(mutados)
        primera=mut[:]
        c=c+1
        #raw_input("#####################################################################################################################")
    print best
    print "Acabo en numero de generacion= " + str(c)
    print("El resultado final es: \n")
    print "N°  \tPeso   \tImportancia\tExistencia\t\tPeso X Existencia\t\t Importancia X Existencia"

    PesoTotal=0
    ImportanciaTotal=0
    for x in range(0,len(best)-1):
        try:
            if best[x][0]==1:
                articulo=tabla[x+1]
                pes=articulo[0]
                impo = articulo[1]
                ex= best[x][1]
                pt=pes*ex
                it=impo*ex
                PesoTotal=PesoTotal+pt
                ImportanciaTotal=ImportanciaTotal + it
                print ""+str(x+1)+"\t\t"+str(pes)+"\t\t\t"+str(impo)+"\t\t\t"+str(ex)+"\t\t\t\t"+str(pt)+"\t\t\t\t\t\t\t"+str(it)
            else:
                pass
        except TypeError,e:
            pass #llego a fin
    print "\t\tPeso Total  \tImportancia total"
    print "\t\t   "+str(PesoTotal) +"\t\t\t\t"+str(ImportanciaTotal)


main()