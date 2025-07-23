import tkinter as tk
from tkinter import messagebox
import os

RUTA_DATOS = "c:/Users/juanc/Desktop/SEMESTRE_2025_01/POO/Actividad_6/Users.txt"

class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre32
        self.identificacion = identificacion

    def __str__(self):
        return f"{self.nombre},{self.identificacion}"

class AdministradorUsuarios:
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo
        os.makedirs(os.path.dirname(self.ruta), exist_ok=True)
        if not os.path.exists(self.ruta):
            open(self.ruta, 'w').close()

    def obtener_todos(self):
        with open(self.ruta, "r") as archivo:
            return [linea.strip().split(",") for linea in archivo if linea.strip()]

    def registrar(self, persona):
        if self.existe(persona.identificacion):
            return False
        with open(self.ruta, "a") as archivo:
            archivo.write(str(persona) + "\n")
        return True

    def existe(self, identificacion):
        return any(usuario[1] == identificacion for usuario in self.obtener_todos())

    def modificar(self, persona):
        registros = self.obtener_todos()
        modificados = []
        fue_encontrado = False
        for nombre_guardado, id_guardado in registros:
            if id_guardado == persona.identificacion:
                modificados.append([persona.nombre, persona.identificacion])
                fue_encontrado = True
            else:
                modificados.append([nombre_guardado, id_guardado])
        if fue_encontrado:
            with open(self.ruta, "w") as archivo:
                for nombre, iden in modificados:
                    archivo.write(f"{nombre},{iden}\n")
        return fue_encontrado

    def borrar(self, identificacion):
        registros = self.obtener_todos()
        filtrados = [linea for linea in registros if linea[1] != identificacion]
        if len(filtrados) == len(registros):
            return False
        with open(self.ruta, "w") as archivo:
            for nombre, iden in filtrados:
                archivo.write(f"{nombre},{iden}\n")
        return True

class Aplicacion:
    def __init__(self, admin):
        self.admin = admin
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Personas")
        self.ventana.geometry("400x250")
        self.ventana.resizable(False, False)

        tk.Label(self.ventana, text="Nombre", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.ventana, text="Identificación", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.campo_nombre = tk.Entry(self.ventana, font=('Arial', 12), width=25)
        self.campo_id = tk.Entry(self.ventana, font=('Arial', 12), width=25)

        self.campo_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.campo_id.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.ventana, text="Registrar", width=15, command=self.registrar).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.ventana, text="Mostrar", width=15, command=self.mostrar).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.ventana, text="Modificar", width=15, command=self.modificar).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.ventana, text="Borrar", width=15, command=self.borrar).grid(row=3, column=1, padx=10, pady=10)

        self.ventana.mainloop()

    def registrar(self):
        nombre = self.campo_nombre.get().strip()
        identificacion = self.campo_id.get().strip()
        if not nombre or not identificacion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        persona = Persona(nombre, identificacion)
        if self.admin.registrar(persona):
            messagebox.showinfo("Éxito", "Persona registrada.")
        else:
            messagebox.showerror("Error", f"El ID '{identificacion}' ya está en uso.")

    def mostrar(self):
        personas = self.admin.obtener_todos()
        mensaje = "\n".join(f"Nombre: {nombre}, ID: {iden}" for nombre, iden in personas) or "No hay registros disponibles."
        messagebox.showinfo("Personas Registradas", mensaje)

    def modificar(self):
        nombre = self.campo_nombre.get().strip()
        identificacion = self.campo_id.get().strip()
        if not nombre or not identificacion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        persona = Persona(nombre, identificacion)
        if self.admin.modificar(persona):
            messagebox.showinfo("Éxito", "Datos actualizados.")
        else:
            messagebox.showerror("Error", f"No se encontró un usuario con ID '{identificacion}'.")

    def borrar(self):
        identificacion = self.campo_id.get().strip()
        if not identificacion:
            messagebox.showerror("Error", "Debe ingresar un ID.")
            return
        if self.admin.borrar(identificacion):
            messagebox.showinfo("Éxito", "Registro eliminado.")
        else:
            messagebox.showerror("Error", f"No se encontró un usuario con ID '{identificacion}'.")

if __name__ == "__main__":
    gestor_personas = AdministradorUsuarios(RUTA_DATOS)
    Aplicacion(gestor_personas)

