#Importacion de Liberias
import tkinter as tk
import numpy as np

#Paso 2. Crear una clase Principal Simplex
class SimplexSolcion:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Metodo Simplex")

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

        self.btn_resolver=tk.Button(self.ventana,text="Resolver")
        self.btn_resolver.grid(row=5,column=0,padx=10,pady=10)

        self.btn_iteraciones=tk.Button(self.ventana, text="Iterar")
        self.btn_iteraciones.grid(row=5,column=1,padx=10)

        self.texto_Salida=tk.Text(self.ventana, height=20, width=100)
        self.texto_Salida.grid(row=6,column=0, padx=10,pady=10)




ventanaApp=tk.Tk()
aplicacion=SimplexSolcion(ventanaApp)
ventanaApp.mainloop()



#ventana=tk.Tk()
#entrad=tk.Text(ventana, height=10,width=40).grid(row=0,column=0)
#titulo=tk.Button(ventana,text="Simplex")
#titulo.pack()
#pantalla=tk.Frame(ventana).grid(row=4,column=0)
#ventana.mainloop()

