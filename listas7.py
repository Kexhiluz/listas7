import time
import os
#defino las listas
provincia=['Avila','Burgos','Leon','Palencia','Salamanca','Segovia','Soria','Valladolid','Zamora','Castilla y Leon']
casos_confirmados=['414','719','821','262','1030','567','523','886','192','5414']
casos_nuevos=['33','46','95','42','148','64','92','79','24','623']
try:
    os.system ("cls")
    def Dar_alta(provincia,casos_confirmados,casos_nuevos):
        nombre=input("Introduce el nombre de la provincia: ")
        indice=casos_confirmados(nombre)
        indice2=casos_nuevos(nombre)
        if nombre in provincia:
            print("La provincia es:",nombre, "El numero de casos confirmados es:",casos_confirmados[indice], "Y el numero de casos nuevos es:",casos_nuevos[indice2])

    def Modificar(casos_confirmados,casos_nuevos):
        nombre=input("Introduce el nombre de la provincia: ")
        if nombre in provincia:
            confirmados_nuevo=int(input("Introduce el nuevo numero de casos confirmados: "))
            indice=provincia.index(nombre)
            casos_confirmados[indice]=confirmados_nuevo
            print("El nuevo numero de casos confirmados es de: ",casos_confirmados[indice])
        else:
            print("No has introducido una provincia valida")
    #no consigo entender como hacer que funcione la funcion Nuevos_confirmados().
    def Nuevos_confirmados():
        nombre=input("Introduce el nombre de la provincia: ")
        if nombre in provincia:
            for nombre in nombre:
                print(provincia[nombre]+" "+str(casos_confirmados[nombre])+" "+str(casos_nuevos[nombre]))
    
    def Listado_general():
        for x in range(0,10):
            print(provincia[x]+" "+str(casos_confirmados[x])+" "+str(casos_nuevos[x]))


    print("Situación epidemiológica del coronavirus (COVID-19) en Castilla y León ")
    print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
    while True:
        print("\t1.- Dar de alta Provincia y datos (confirmados y nuevos)")
        print("\t2.- Introduce una provincia para modificar sus datos(confirmados y nuevos) " )
        print("\t3.- Numero Total de casos Confirmados y Nuevos en la Comunidad ")
        print("\t4.- Listado de la situacion  general por provincias(confirmados y nuevos)")
        print("\t5.- Salir")
        opcion=int(input("Elige una opcion: "))
        if opcion==1:
            Dar_alta(provincia,casos_confirmados,casos_nuevos)
        elif opcion==2:
            Modificar(casos_confirmados,casos_nuevos)
        elif opcion==3:
            Nuevos_confirmados()
        elif opcion==4:
            Listado_general()
        else:
            break
except ValueError:
    print("No pude convertir el dato a un entero.")
except Exception as e:
    print("Ha ocurrido un error no previsto del tipo ", type(e).__name__ )