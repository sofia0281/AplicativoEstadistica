#Definimos las librerias
from scipy.stats import norm
#calculo númerico, manejo de vectores y arreglos
import numpy as np
#crear gráficos 
import matplotlib.pyplot as plt
import math
#funciones del sistema operativo
import os
#añadir espera
import time 

def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
#--------------------------------------------------------------------------------------------------
# mu= media
# sigma= desviación estandar
def graficar(mu, sigma):
    # Generamos los datos para la distribución normal que se van a graficar
    #crea una linea de números en intervalos para la creación del eje x
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100); #La primera parte es el recorrido de X y la segunda el número de momentos
    #eje y, por cada x hay un y
    y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma)**2); 

    # Creamos el gráfico de la distribución normal
    plt.plot(x, y);
    plt.title('Distribución Normal');
    plt.xlabel('Valores');
    plt.ylabel('Probabilidad');
    plt.grid(True);

    # Mostramos el gráfico
    plt.show()

#---------------------------------------------------------------------------------------------------------

def mayorque(mu, sigma):
    x = float(input("El dato debe de ser mayor que: "))
    z = (x - mu)/sigma
    if(x < mu):
        print("La probabilidad de que sea mayor que ",x," es ",(1 - norm.cdf(z))*100,"%")
    elif(x > mu):
        print("La probabilidad de que sea mayor que ",x," es ",(0.5-(norm.cdf(z)-0.5)) * 100,"%")
    else:
        print("La probabilidad de que sea mayor que ",x," es 50%")

def menorque(mu, sigma):
    x = float(input("El dato debe de ser menor que: "))
    z = (x - mu)/sigma
    if(x > mu):
        print("La probabilidad de que sea menor que ",x," es ",norm.cdf(z) * 100,"%")
    elif(x < mu):
        print("La probabilidad de que sea menor que ",x," es ",(norm.cdf(z)-0.5) * 100,"%")
    else:
        print("La probabilidad de que sea menor que ",x," es 50%")

#-----------------------------------------------------------------------
def entreque(mu, sigma):
    x1 = float(input("El dato 1 debe de ser entre que: "))
    x2 = float(input("El dato 2 debe de ser entre que: "))
    z1 = (x1 - mu)/sigma
    z2 = (x2 - mu)/sigma

    if (x1 == x2):
        print("La probabilidad de que esté entre ",x1,"y ",x2," es 0%")
    elif (x1 > mu and x2 > mu):
        if x1 > x2:
            print("La probabilidad de que esté entre ",x1,"y ",x2," es ",(norm.cdf(z1)-norm.cdf(z2)) * 100,"%")
        if x1 < x2:
            print("La probabilidad de que esté entre ",x1,"y ",x2," es ",(norm.cdf(z2)-norm.cdf(z1)) * 100,"%")       
    elif (x1 < mu and x2 < mu):
        if x1 > x2:
            print("La probabilidad de que esté entre ",x1,"y ",x2," es ",(norm.cdf(z2)-norm.cdf(z1)) * -100,"%")
        if x1 < x2:
            print("La probabilidad de que esté entre ",x1,"y ",x2," es ",(norm.cdf(z1)-norm.cdf(z2)) * -100,"%")      
    elif ((x1 < mu and x2 > mu) or (x1 > mu and x2 < mu)):
        print("La probabilidad de que esté entre ",x1,"y ",x2," es ",(norm.cdf(z2)-norm.cdf(z1)) * 100,"%")

def menu():
    opcion1 = 0
    Datos = False
    borrarPantalla()
    print("Hola! Este programa te permitirá conocer las probabilidades de datos aleatorios a partir de la media y desviación estandar.")
    print("Además permite ingresar n número de datos con los cuales podrás trabajar la normal estandar y normal tipificada.\n")
    opcion2 = int(input("¿Desea introducir datos (0) o la media y desviación estandar (1)? (0/1): "))
    if  opcion2 == 0:

        Datos = True
        nDatos = int(input("¿Cuantos datos desea ingresar? "))
        datos_originales = np.empty(nDatos)
        #ciclo para ingresar el número de datos que desea ingresar el usuario
        for i in range(nDatos):
            datos_originales[i] = float(input("Ingrese el dato {}: ".format(i+1)))

        if int(input("\n¿Desea trabajar con la normal (0) o con la normal tipificada (1)? (0/1): ")) == 0:
            mu = np.mean(datos_originales)
            sigma = np.std(datos_originales)
            datos_tipificados = datos_originales
        else:
            datos_tipificados = (datos_originales - np.mean(datos_originales)) / np.std(datos_originales)
            mu = np.mean(datos_tipificados)
            sigma = math.ceil(np.std(datos_tipificados))
    elif opcion2 == 1:
        mu = float(input("Indique la media: "))
        sigma = float(input("Indique la desviación estandar: "))
    else:
        print("\nOpción inválida.")
        opcion1 = 5 
    #este menú aparece para tanto opcion=0 y opcion=1
    if(opcion1 != 5):
        while opcion1 != "5":
            borrarPantalla()
            print("0. Mostrar datos.")
            print("1. Graficar.")
            print("2. Probabilidad que sea mayor que.")
            print("3. Probabilidad que sea menor que.")
            print("4. Probabilidad que esté entre un mínimo y un máximo")
            print("5. Salir.")
            opcion = input("Ingrese una opcion: ")
            if opcion == "0":
                if(Datos == True):
                    print(datos_tipificados)
                else:
                    borrarPantalla()
                    print("No se han ingresaron datos.")
                    time.sleep(5)
            elif opcion == "1":
                graficar(mu, sigma)
            elif opcion == "2":
                borrarPantalla()
                mayorque(mu, sigma)
                time.sleep(5)
            elif opcion == "3":
                borrarPantalla()
                menorque(mu, sigma)
                time.sleep(5)
            elif opcion == "4":
                borrarPantalla()
                entreque(mu, sigma)
                time.sleep(5)
            elif opcion == "5":
                borrarPantalla()
                break;  
            else:
                print("Opcion invalida, ingrese una opcion valida.")
    print("Gracias por usar nuestro sistema.\n")

menu()