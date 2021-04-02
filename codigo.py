#MODULOS-----------------------------------
from fractions import Fraction #para fracciones
import math #para logaritmos
import sys
import operator #para ordenar



##FUNCIONES---------------------------------

#Leer el texto base de un archivo y generar la Fuente de información con frecuencias absolutas.
def fuente_informacion_freq_absolutas(nombre_archivo):
    
    fuente_informacion = {} #diccionario que sera mi fuente (alfabeto + frecuencias)
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                #print(caracter)


                    #Miro si es el caracter de fin de línea en cuyo caso lo agregaré como un doble espacio separado, dos espacios simples vaya, no un nuevo símbolo que sea "  "
                if caracter == "\n":    
                        
                    caracter = " " #convierto el \n en un espacio
                    for i in range(0,2): #0 incluido, 2 excluido --> 2 iteraciones
                        if " " in fuente_informacion: #si ya he añadido antes un espacio
                            fuente_informacion[" "] = fuente_informacion[" "] + 1 #si ya estaba el simbolo solo le sumo una ocurrencia 
                        else:
                            fuente_informacion[" "] = 1 #si es la primera ocurrencia, añado al diccionario el espacio (" ") con una ocurrencia
                   
                else: #si no es el de fin de linea es otro pero que tampoco esta en el alfabeto actualmente

                    #miro si el caracter esta ya en el alfabeto
                    if caracter in fuente_informacion:


                        fuente_informacion[caracter] = fuente_informacion[caracter]+1  #si está le sumo uno a su nº de ocurencias
                    
                    else:
                        
                        fuente_informacion[caracter] = 1  #simplemente le pongo una ocurrencia (al ponerle 1 ocurrencia se añaden la clave y el valor, es decir el caracter y el 1)



            #sigo leyendo la siguiente
            linea = f.readline()
        



      

    #TENIENDO YA EL ALFABETO Y LAS FRECUENCIAS ABS EN EL DICCIONARIO DE NOMBRE fuente_informacion {caracter : freq} las devuelvo
    return fuente_informacion

def leerAlfabetoTalCual(nombre_archivo):
    alfabeto = []
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                alfabeto.append(caracter)
        
            linea = f.readline()

     

    #TENIENDO YA EL ALFABETO lo devuelvo
    return alfabeto

def procesarFuenteInformacion(fuenteInformacion):
    
    alfabeto = []
    
    for i in fuenteInformacion.keys():
        alfabeto.append(i)

    return alfabeto

def leerDatoEntrada(nombre_archivo):
    lista = []
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                
                if caracter == '\n'or caracter == ',' or caracter == ' ': #los \n los ignoramos, como si no estuvieran y las comas y espacios que los separan también
                   continue

                lista.append(caracter)
        
            linea = f.readline()

     

    return lista

def decodLineal(identidad, secuencias, filas, columnas):
    secDecodific = ""
    #Si la identidad esta a la izda en la Generadora me quedo con el numero de posiciones que indiquen las filas desde la izda
    if identidad == "I":
        for secuencia in secuencias: #cada pos del vector secuencias
            print(secuencia)
            for i in range(filas):
                secDecodific = secDecodific + secuencia[i] #i para cada caracter dentro de cada secuencia codificada linealmente desde el 0


    else:    
    #Si no, desde la derecha
          for secuencia in secuencias: #cada pos del vector secuencias
            for i in range(filas, columnas):
                secDecodific = secDecodific + secuencia[i]#i para cada caracter dentro de cada secuencia codificada linealmente desde la segunda mitad

    return secDecodific

def decodFuente(secuencia, alfabeto, base):
    
    caracter = ''

    #  Convertir cada bloque de binario al entero decimal (en éste caso)
    entero = int(secuencia, base) #convierto la secuencia en string a un numero en la base que hayamos metido, si es 2 binario a decimal, si es 3 ternario a decimal
    print(entero)

    # Calculo la posicion en el alfabeto para el entero anterior
    posicion = entero + 1

    # Busco en el alfabeto la posicion teniendo en cuenta que tal como está almacenado el índice es la posición obtenida anterior-1
    print(alfabeto[posicion-1])

    caracter = alfabeto[posicion-1]

    return caracter







##PROGRAMA------------------------
print("Bienvenid@ a la Práctica 3: Simulacion de una codificación binaria lineal SIN RUIDO")
print("Introduzca las Filas de la matríz")
filas = input()
print("Introduzca las Columnas de la matríz")
columnas = input()
print("La Generadora es de Orden "+filas+"x"+columnas)

filas = int(filas) #Lo parseo a entero
columnas = int(columnas) #Lo parseo a entero

print("¿En qué parte de la generadora está la Identidad?[D/I]")
identidad = input()

if identidad != 'D' and identidad != 'I':
    print("Error de entrada")
    exit()



    #1. Cargar Alfabeto 

#ENTRADA TAL CUAL DEL ARCHIVO
#alfabeto = leerAlfabetoTalCual('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_3_SI/Resolución/Alfabeto.txt')
#print("Tal cual del archivo", alfabeto)

fuenteInformacion = fuente_informacion_freq_absolutas('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_3_SI/Resolución/Alfabeto.txt')
print("Tam Alf = ", sum(fuenteInformacion.values()))
alfabeto = procesarFuenteInformacion(fuenteInformacion) #de la fuente de informacion nos quedamos solo con el alfabeto en una lista

print("Alfabeto = ", alfabeto)
print("Tamaño = ", len(alfabeto))
m = len(alfabeto)


#ENTRADA MANUAL
#alfabeto = []
#alfabeto = ['P','R','A','C','T','I','C','A','T','R','E','S']
#print(alfabeto)


    # Leer dato entrada (lista L)

lista = leerDatoEntrada('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_3_SI/Resolución/Dato.txt')
print("Lista Entrada", lista)


    # Calculo el tamaño de la lista y lo divido por el número de columnas de la generadora
tam = len(lista)
print("Tam Dato Entrada = ", tam)

cociente = tam // columnas
resto = tam % columnas

print("Cociente = ", cociente)
print("Resto = ", resto)


    # De la lista leída tendremos: "cociente" secuencias de "columnas" elementos y una cola de "resto" elementos

secuencia = ""
secuencias = []
contador = 0

for i in range(cociente*columnas):
    secuencia = secuencia + lista[i] #añado el elemento subi de la lista de entrada
    print(secuencia)
    contador = contador + 1
    
    if contador == columnas:
        #he completado una secuencia, la salvo en el vector de secuencias separadas
        secuencias.append(secuencia)
        print("vuelco")
        secuencia = ""
        contador = 0


cola = ""

for i in range((cociente*columnas), tam): #cociente*columnas fue excluido en el bucle previo porque llegaba justo hasta el valor anterior a ese y ahora parto desde ese inclusive y hasta el final para coger todo lo que quede
    cola = cola + lista[i]


print(secuencias)
print(cola)


    # Decodificación Lineal

cod_fuente_lista = decodLineal(identidad, secuencias, filas, columnas) #tengo la secuencia decodificada linealmente sin la cola
cod_fuente_lista = cod_fuente_lista + cola
print(cod_fuente_lista)


    # Calcular la longitud mínima en bloque (para codificar en binario en éste caso)

print("Introduzca la base de la codificación [Binario --> 2]")
base = input()
base = int(base)
m = int(m)


# Calcular el logaritmo en base, la indicada, del nº símbolos del alfabeto
long_min = math.log(m,base)
print(long_min)

# Separo parte entera del resultado y parte decimal
parte_decimal, parte_entera = math.modf(long_min)
print(parte_entera) #Como tiene que ser el entero superior siempre va a ser 1 mas que el que salga
print(parte_decimal)

long_min = int(parte_entera+1) #hago un cast a entero porque sino quedaba float
print("Longitud mínima (Entero Superior) = ", long_min)



    # Troceo la secuencia en bloques de esa long mínima

secsCodFuente = []
secuenciaLongMin = ""
contador = 0

for i in cod_fuente_lista: #caracter a caracter de las secuencias
    secuenciaLongMin = secuenciaLongMin + i #añado cada caracter
    contador = contador + 1
    
    if contador == long_min:
        #he completado una secuencia, la salvo en el vector de secuencias separadas
        secsCodFuente.append(secuenciaLongMin)
        print("vuelco")
        secuenciaLongMin = ""
        contador = 0


print(secsCodFuente)

    # CICLO - Repetir tantas veces como secuencias de long mínima haya en nuestra secsCodFuente. Es decir, como marque la longitud
mensaje = ""

for secuencia in secsCodFuente: #recorro cada secuencia de long mínima del array
    mensaje = mensaje + decodFuente(secuencia, alfabeto, base)


print("\n======================================================================")
print("MENSAJE DECODIFICADO ="+mensaje)
print("======================================================================")

print("\nFIN DEL PROGRAMA")
       







##APENDICES:

    #pintar todos los valores del diccionario
#for i in fuente_freq_abs.values():
#        print(i)

    #pintar todas las claves del diccionario
#for i in fuente_freq_abs.keys():
#        print(i)

    #manejar clave y valor a la vez en un diccionario para ir por las posiciones
#for clave, valor in fuente_de_informacion.items():  
#        fuente_de_informacion[clave] = Fraction(valor, total_frecuencias)


    #fraccion es numerador/denominador
#fraccion = Fraction(1, 2) #--> 1/2
#print(fraccion)


    #logaritmo en base 2 de 100
#math.log(100,2)



#utf8stdout = open(1, 'w', encoding='utf-8', closefd=False) # fd 1 is stdout
#cadena = "ó"
#print(cadena)
#for i in fuente_freq_abs.keys():
    #print(i, file=utf8stdout)
