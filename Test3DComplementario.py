Luis Alberto Hoil Ambros Teste 3D.py
"""
Programa que solicita las cordenadas del hit point 
y permite saber si el hit point se encuentra fuera o dentro del Área
triangulo.
tuve que instalar kerboard con pip install keyboard
Luis Alberto Hoil Ambros
"""

import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import keyboard


def plotTriangulo(x,y,z):
    plt.axis([0,150,120,0])
    plt.axis('on')
    plt.grid(True)
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.title('Test3DComplemetario')





    #___Ploteo triangulo base
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k') 
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')
    plt.text(60,65,'A',color='r')#——EtiquetaA

    #____Hitpoint
    plt.scatter(x[3],y[3],s=20,color='r')

    #____Trazo de los triangulos
    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color=('b')) 
    plt.plot([x[1],x[3]],[y[1],y[3]],linestyle=':',color=('g'))
    plt.plot([x[2],x[3]],[y[2],y[3]],linestyle=':',color=('r'))



    #——Etiquetas de las esquinas de los triangulos
    plt.text(35,63,'0',color=('b')) 
    plt.text(25,10,'1',color=('g'))
    plt.text(83,63,'2',color=('r'))
    plt.text(x[3]+2,y[3],'3')



    #——Calcular lineas del triangulo A
    abA=sqrt(((x[1]-x[0])*(x[1]-x[0])) + ((y[1]-y[0])*(y[1]-y[0])))
    acB=sqrt(((x[2]-x[0])*(x[2]-x[0])) + ((y[2]-y[0])*(y[2]-y[0])))
    bcC=sqrt(((x[2]-x[1])*(x[2]-x[1])) + ((y[2]-y[1])*(y[2]-y[1])))

    pA = abA+acB+bcC
    spA = pA/2
    AreaA= sqrt((spA*(spA-abA)*(spA-acB)*(spA-bcC)))
    plt.text(100,20,'A=') #——plot output
    dle='%7.0f'% (AreaA)
    dls=str(dle)
    plt.text(105,40,dls)



    #——Calcular perimetro Triangulo A1 
    abA1=sqrt(((x[1]-x[0])*(x[1]-x[0])) + ((y[1]-y[0])*(y[1]-y[0])))
    acB1=sqrt(((x[3]-x[0])*(x[3]-x[0])) + ((y[3]-y[0])*(y[3]-y[0])))
    bcC1=sqrt(((x[3]-x[1])*(x[3]-x[1])) + ((y[3]-y[1])*(y[3]-y[1])))

    pA1 = abA1+acB1+bcC1
    spA1 = pA1/2
    AreaA1= sqrt((spA1*(spA1-abA1)*(spA1-acB1)*(spA1-bcC1)))
    plt.text(100,40,'A1=') #——plot output
    dle='%7.0f'% (AreaA1)
    dls=str(dle)
    plt.text(110,45,dls)

    #——Calcular perimetro Triangulo A2 
    abA2=sqrt(((x[3]-x[0])*(x[3]-x[0])) + ((y[3]-y[0])*(y[3]-y[0])))
    acB2=sqrt(((x[2]-x[0])*(x[2]-x[0])) + ((y[2]-y[0])*(y[2]-y[0])))
    bcC2=sqrt(((x[3]-x[2])*(x[3]-x[2])) + ((y[3]-y[2])*(y[3]-y[2])))

    pA2 = abA2+acB2+bcC2
    spA2 = pA2/2
    AreaA2= sqrt((spA2*(spA2-abA2)*(spA2-acB2)*(spA2-bcC2)))
    plt.text(100,60,'A2=') #——plot output
    dle='%7.0f'% (AreaA2)
    dls=str(dle)
    plt.text(110,60,dls)

    areaSuma=AreaA1+AreaA2

    #se determina si el hit point está afuera o dentro del limite
    if(areaSuma<AreaA):
        plt.text(20,100,'El HitPoint se encuentra dentro de los limites')
    else:
        plt.text(20,100,'El Hitpoint se encuentra fuera de los limites')


    plt.show()

print("Ingrese Enter para continuar, para terminar proceso presione Esc")
while True:

    if keyboard.is_pressed('ENTER'):
        input()    
        #____Pedir puntos de las coordenadas x y y del hitpoint
        pntx = float(input('ingresa la coordena x del hitpoint ='))
        pnty = float(input('ingresa la coordena y del hitpoint ='))
        #___Plano
        x=[40,30,80,pntx] 
        y=[60,10,60,pnty]
        z=[0,0,0,0]

        plotTriangulo(x,y,z)



    if keyboard.is_pressed('Esc'):
        print("Ejecución finalizada")
        break

    
