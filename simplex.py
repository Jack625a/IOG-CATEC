#Paso 1. Importar la libreria de ciencia Py - Programacion Lineal
from scipy.optimize import linprog


#Ejericio 1. Situación: Una empresa de tecnología produce teléfonos y tablets. Cada teléfono se vende por 200 bolivianos y cada tablet por 300 bolivianos.
#Restricciones:
#La empresa puede producir hasta 300 teléfonos.
#La empresa puede producir hasta 200 tablets.
#La capacidad de producción total es de 400 dispositivos.

#Paso 2. Coeficientes de la funcion objetivo
#Z=MAXIMIZAR
#X1=CANTIDAD TELEFONOS
#x2=CANTIDAD TABLETS
#Z=200X+300X2=> Z-200X1-300X2=0

#Coeficientes de la funcion objetivo
c=[-10,-15]

#Restricciones
#x1<=300
#x2<=200
#x1+x2<=400
#x1>=0 , x2>=0

#Coeficientes de las restricciones
a=[
    [1,0],
    [0,1],
    [1,1]
]

#Lado derecho de las igualdades
b=[100,80,150]


#Resolver el ejercicio
resolver=linprog(c,A_ub=a,b_ub=b,method='simplex')

#Mostrar los resultados
print('Z= ',resolver.fun)
print('Variables x1,x2= ', resolver.x)

