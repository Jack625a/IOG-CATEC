#Importacion de librerias
from scipy.optimize import linprog
import numpy as np

def obtener(datos):
    return input(datos).strip()

def imprimir_Iteracion(interacion,tabla):
    print(f"\nIteracion: {interacion}")
    print("Tabla Simplex")
    print(tabla)

def inicio():
    print("Metodo Simplex para Programacion Lineal (Paso a Paso)")
    #Obtener los coeficientes de la funcion objetivo
    c_entradas=obtener('Ingrese los coeficientes de la funcion objetivo, separados por espacio: ')
    c=list(map(float, c_entradas.split()))

    #Numero de restricciones
    num_restricciones=int(obtener("Ingres el numero de restricciones: "))

    #Obtener los coeficientes de las restricciones
    A=[]
    for i in range(num_restricciones):
        a_entrada=obtener(f"Ingrese los coeficientes de la restrccion {i+1} (Que esten separados por espacio): ")
        A.append(list(map(float,a_entrada.split())))

    #Obtener los coeficientes del las igualdades del lado derecho de las restricciones
    b_entrada=obtener("Ingrese los coeficientes de las igualdades del lado derecho de las restricciones (separados por espacio): ")
    b=list(map(float, b_entrada.split()))

    #Negar los coeficientes de la funcion objetivo para Maximizar
    c=[-coef for coef in c]


    #Convertir A(Coeficientes de restricciones)  y b(Coeficientes igualdad) en matrices 
    A=np.array(A)
    b=np.array(b)

    #Inicializar la tabla simplex
    num_variables=len(c)
    num_saltos=len(b)
    tabla=np.hstack([A,np.eye(num_saltos),b.reshape(-1,1)])
    c_completo=np.hstack([c,np.zeros(num_saltos+1)])
    tabla=np.vstack([tabla,c_completo])

    iteracion=0
    imprimir_Iteracion(iteracion, tabla)

    #Realizar la iteraciones hasta que la funcion objetivo no tenga valores negativos
    while True:
        if all(i>=0 for i in tabla[-1, :-1]):
            print("\nSolucion Optima Encontrada")
            print(f"Valor Optimo: Z= {-tabla[-1,:-1]}")
            solucion=tabla[:-1,-1]
            print(f"Variables de desición Xn: {solucion[:num_variables]}")
            break
        #Seleccionar la columna pivote
        pivote_columna=np.argmin(tabla[-1,:-1]) #Entrantes
        if all(fila[pivote_columna]<=0 for fila in tabla[:-1]):
            print("Erro al resolver el problema")
            break

        #Realizar el pivoteo
        calculo=[fila[-1]/fila[pivote_columna] if fila[pivote_columna]>0 else float('inf') for fila in tabla[:-1]] #Fila valores salientes
        pivote_fila=np.argmin(calculo)
        elemento_pivote=tabla[pivote_fila,pivote_columna]
        tabla[pivote_fila]=tabla[pivote_fila]/elemento_pivote
        for i in range(len(tabla)):
            if i != pivote_fila:
                tabla[i]=tabla[i]-tabla[i,pivote_columna]*tabla[pivote_fila]
        
        iteracion= iteracion+1
        imprimir_Iteracion(iteracion,tabla)



inicio()
                                







