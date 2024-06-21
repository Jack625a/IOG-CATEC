#Importacion de Liberias
import tkinter as tk
import numpy as np
from tkinter import messagebox
from scipy.optimize import linprog

#Paso 2. Crear una clase Principal Simplex
class SimplexSolucion:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Metodo Simplex Paso a Paso")

        self.crear_interfaz()
        self.iteracion=0
        self.tabla=None
        self.num_variables=0
        self.num_holgura=0
    
    #Paso 3. Creacion de las acciones o metodos de la clase
    def crear_interfaz(self):
        tk.Label(self.ventana, text="Coeficientes de la funcion objetivo separados por espacio: ").grid(row=0,column=0, padx=10, pady=10)
        self.entrada_funcion_objetivo=tk.Entry(self.ventana)
        self.entrada_funcion_objetivo.grid(row=0,column=1, padx=10,pady=10)

        tk.Label(self.ventana, text="Numero de restricciones: ").grid(row=1,column=0, padx=10, pady=10)
        self.entrada_num_restricciones=tk.Entry(self.ventana)
        self.entrada_num_restricciones.grid(row=1,column=1, padx=10,pady=10)

        tk.Label(self.ventana, text="Coefiecientes de las restricciones separados por espacio: ").grid(row=2,column=0, padx=20, pady=10)
        self.entrada_restricciones=tk.Text(self.ventana, height=8,width=50)
        self.entrada_restricciones.grid(row=2,column=1, padx=10, pady=10)

        tk.Label(self.ventana,text="Coeficientes del lado derecho de la igualdad separados por espacio: ").grid(row=3,column=0, padx=10, pady=10)
        self.entrada_igualdad=tk.Entry(self.ventana)
        self.entrada_igualdad.grid(row=3, column=1, padx=10, pady=10)

        self.btn_pantalla=tk.Frame(self.ventana)
        self.btn_pantalla.grid(row=4,column=0,padx=10, pady=10)

        self.btn_resolver=tk.Button(self.ventana,text="Resolver", command=self.inciar_simplex)
        self.btn_resolver.grid(row=5,column=0,padx=10,pady=10)

        self.btn_iteraciones=tk.Button(self.ventana, text="Iterar", command=self.pasoApaso)
        self.btn_iteraciones.grid(row=5,column=1,padx=10)

        self.btn_resetear=tk.Button(self.ventana, text="Borrar Datos", command=self.borrar)
        self.btn_resetear.grid(row=5,column=2,padx=10)

        self.texto_Salida=tk.Text(self.ventana, height=20, width=100)
        self.texto_Salida.grid(row=6,column=0, padx=10,pady=10, columnspan=3)

    #Incializacion del programa
    def inciar_simplex(self):
        try:
            c_entrada=self.entrada_funcion_objetivo.get().strip()
            c = list(map(float, c_entrada.split()))

            num_restricciones=int(self.entrada_num_restricciones.get().strip())

            entrada_restricciones=self.entrada_restricciones.get("1.0",tk.END).strip().split('\n')

            A=[list(map(float, line.split())) for line in entrada_restricciones]

            b_entrada=self.entrada_igualdad.get().strip()
            b=list(map(float, b_entrada.split()))

            # Negar los coeficientes de la función objetivo para maximizar
            c = [-coef for coef in c]
            # Convertir A (Coeficientes de restricciones) y b (Coeficientes igualdad) en matrices 
            A = np.array(A)
            b = np.array(b)

            # Inicializar la tabla simplex
            self.num_variables = len(c)
            self.num_filas = len(b)
            self.tabla = np.hstack([A, np.eye(self.num_filas), b.reshape(-1, 1)])
            self.c_completo = np.hstack([c, np.zeros(self.num_filas + 1)])
            self.tabla = np.vstack([self.tabla, self.c_completo])

            self.iteracion = 0
            self.imprimir_Iteracion()

            self.btn_iteraciones.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error al resolver el problema", str(e))
    
    #Resolver el ejercicio paso a paso
    def pasoApaso(self):
        #Comprobar que se encontro la solucion optima
        if all(i>=0 for i in self.tabla[-1,:-1]):
            self.texto_Salida.insert(tk.END, "\nSolución Óptima Encontrada.\n")
            self.texto_Salida.insert(tk.END,f"Valor Óptimo: Z = {self.tabla[-1, -1]}\n")

            solucion=self.tabla[1:,-1]
            self.texto_Salida.insert(tk.END,f"Valor de decision: {solucion[:self.num_variables]}\n")
            self.btn_iteraciones.config(state=tk.DISABLED)
            return

        # Seleccionar la columna pivote
        pivote_columna = np.argmin(self.tabla[-1, :-1])  # Entrantes
        if all(fila[pivote_columna] <= 0 for fila in self.tabla[:-1]):
            self.texto_Salida.insert(tk.END, "Error al resolver el problema")
            self.btn_iteraciones.config(state=tk.DISABLED)
            return
        # Realizar el pivoteo
        calculo = [fila[-1] / fila[pivote_columna] if fila[pivote_columna] > 0 else float('inf') for fila in self.tabla[:-1]]  # Fila valores salientes
        pivote_fila = np.argmin(calculo)
        #Pivoteo
        elemento_pivote = self.tabla[pivote_fila, pivote_columna]
        self.tabla[pivote_fila] = self.tabla[pivote_fila] / elemento_pivote
        for i in range(len(self.tabla)):
            if i != pivote_fila:
                self.tabla[i] = self.tabla[i] - self.tabla[i, pivote_columna] * self.tabla[pivote_fila]
        self.iteracion += 1
        self.imprimir_Iteracion()
    
    def imprimir_Iteracion(self):
        self.texto_Salida.insert(tk.END, f"\nIteracion {self.iteracion} \n")
        self.texto_Salida.insert(tk.END, "TABLA SIMPLEX \n")
        self.texto_Salida.insert(tk.END,f"{self.tabla}\n")

    #metodo para borra los datos de la pantalla
    def borrar(self):
        self.entrada_funcion_objetivo.delete(0,tk.END)
        self.entrada_num_restricciones.delete(0,tk.END)
        self.entrada_restricciones.delete('1.0',tk.END)
        self.entrada_igualdad.delete(0,tk.END)
        self.texto_Salida.delete('1.0',tk.END)
        self.btn_iteraciones.config(state=tk.DISABLED)
        #Restablecer las variables 
        self.iteracion=0
        self.tabla=None
        self.num_variables=0
        self.num_holgura=0





ventanaApp=tk.Tk()
aplicacion=SimplexSolucion(ventanaApp)
ventanaApp.mainloop()



#ventana=tk.Tk()
#entrad=tk.Text(ventana, height=10,width=40).grid(row=0,column=0)
#titulo=tk.Button(ventana,text="Simplex")
#titulo.pack()
#pantalla=tk.Frame(ventana).grid(row=4,column=0)
#ventana.mainloop()

