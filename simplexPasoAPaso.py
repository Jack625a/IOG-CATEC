import numpy as np
from scipy.optimize import linprog


def obtener(datos):
    return input(datos).strip()

def imprimir_Iteracion(iteracion, tabla):
    print(f"\nIteración: {iteracion}")
    print("Tabla Simplex")
    print(tabla)

def inicio():
    print("Método Simplex para Programación Lineal (Paso a Paso)")
    
    # Obtener los coeficientes de la función objetivo
    c_entradas = obtener('Ingrese los coeficientes de la función objetivo, separados por espacio: ')
    c = list(map(float, c_entradas.split()))

    # Número de restricciones
    num_restricciones = int(obtener("Ingrese el número de restricciones: "))

    # Obtener los coeficientes de las restricciones
    A = []
    for i in range(num_restricciones):
        a_entrada = obtener(f"Ingrese los coeficientes de la restricción {i + 1} (Que estén separados por espacio): ")
        A.append(list(map(float, a_entrada.split())))

    # Obtener los coeficientes de las igualdades del lado derecho de las restricciones
    b_entrada = obtener("Ingrese los coeficientes de las igualdades del lado derecho de las restricciones (separados por espacio): ")
    b = list(map(float, b_entrada.split()))

    # Negar los coeficientes de la función objetivo para maximizar
    c = [-coef for coef in c]

    # Convertir A (Coeficientes de restricciones) y b (Coeficientes igualdad) en matrices 
    A = np.array(A)
    b = np.array(b)

    # Inicializar la tabla simplex
    num_variables = len(c)
    num_filas = len(b)
    tabla = np.hstack([A, np.eye(num_filas), b.reshape(-1, 1)])
    c_completo = np.hstack([c, np.zeros(num_filas + 1)])
    tabla = np.vstack([tabla, c_completo])

    iteracion = 0
    imprimir_Iteracion(iteracion, tabla)

    # Realizar iteraciones hasta que la función objetivo no tenga valores negativos
    while True:
        if all(i >= 0 for i in tabla[-1, :-1]):
            print("\nSolución Óptima Encontrada")
            print(f"Valor Óptimo: Z = {tabla[-1, -1]}")
            solucion = tabla[:-1, -1]
            #print(f"Variables de decisión Xn: {solucion[:num_variables]}")
            resolver=linprog(c,A_ub=A,b_ub=b,method='highs')
            print('Variables x1,x2= ', resolver.x)
            break
        
        # Seleccionar la columna pivote
        pivote_columna = np.argmin(tabla[-1, :-1])  # Entrantes
        if all(fila[pivote_columna] <= 0 for fila in tabla[:-1]):
            print("Error al resolver el problema")
            break

        # Realizar el pivoteo
        calculo = [fila[-1] / fila[pivote_columna] if fila[pivote_columna] > 0 else float('inf') for fila in tabla[:-1]]  # Fila valores salientes
        pivote_fila = np.argmin(calculo)
        elemento_pivote = tabla[pivote_fila, pivote_columna]
        tabla[pivote_fila] = tabla[pivote_fila] / elemento_pivote
        for i in range(len(tabla)):
            if i != pivote_fila:
                tabla[i] = tabla[i] - tabla[i, pivote_columna] * tabla[pivote_fila]
        
        iteracion += 1
        imprimir_Iteracion(iteracion, tabla)


print("Metodo Simplex para Programación Lineal")
print("Bienvenido")
m=True
while m:
    opcion=input("Desea resolver los ejercicios de programacion lineal? 1.SI 2.NO: ")
    if opcion=="1":
        inicio()
    elif opcion=="2":
        m=False
