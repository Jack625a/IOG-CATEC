from scipy.optimize import linprog 

#Funcion para obtener datos de entrada (input)
def obtener(datos):
    return input(datos).strip()
def datos():
    #Obtener los coefiecientes de la funcion objetivo
    c_entradas=obtener('Ingrese los coeficientes de la funcion objetivo, separados por espacio: ')
    c=list(map(float, c_entradas.split()))

    #Determinar el numero de restricciones
    num_restricciones=int(obtener("Ingrese la cantidad de restricciones: "))


    #Obtener los coefiecientes de las restricciones
    A=[]
    for i in range(num_restricciones):
        a_entrada=obtener(f"Ingrese los coeficientes de la restrccion {i+1} (Que esten separados por espacio): ")
        A.append(list(map(float,a_entrada.split())))
    #print(A)

    #Obtener los coeficientes de las igualdades del lado derecho de la tabla
    b_entrada=obtener("Ingrese los coeficientes de las igualdades del lado derecho de las restricciones (separados por espacio): ")
    b=list(map(float, b_entrada.split()))

    #Negar los coeficientes de la funcion objetivo para maximizar
    c=[-coef for coef in c]

    #Resolver el ejercicio
    resolver=linprog(c,A_ub=A,b_ub=b,method='simplex')
    print('Z= ',-resolver.fun)
    print('Variables x1,x2= ', resolver.x)

print("Metodo Simplex para Programación Lineal")
print("Bienvenido")
m=True
while m:
    opcion=input("Desea resolver los ejercicios de programacion lineal? 1.SI 2.NO: ")
    if opcion=="1":
        datos()
    elif opcion=="2":
        m=False