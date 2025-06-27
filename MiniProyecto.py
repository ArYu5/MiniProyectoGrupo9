import tkinter as tk
from tkinter import messagebox
import time

ventana = tk.Tk()
ventana.title('Mini Proyecto')
ventana.geometry('1000x600')


ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)


# Reloj
reloj = tk.Label(ventana, font=('Arial', 60), fg='black')
reloj.grid(row=0, column=0, columnspan=3, pady=10)

def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

hora()

# Funciones de estilo
estilo = tk.StringVar()
def estilo_primavera():
    estilo.set("primavera")
    estilos()
def estilo_noche():
    estilo.set("noche")
    estilos()
def estilo_estandar():
    estilo.set("estandar")
    estilos()
def estilo_otono():
    estilo.set("otono")
    estilos()

def estilos():
    frames= [ventana, reloj, frame_entrada, frame_lista, etiqueta1, etiqueta2, etiqueta3, lista_tareas, frame_borrar,]
    textos=[etiqueta1, etiqueta2, etiqueta3, lista_tareas, reloj]
    botones= [boton_eliminar, boton_entrada, boton_salida, boton_eliminartodo]
    if estilo.get() == "noche":
        for i in frames:
            i.configure(bg='#2a2a40')
        for i in textos:
            i.configure(foreground='white')
        for i in botones:
            i.configure(bg='#000000', fg='skyblue')

    elif estilo.get() == "primavera":
        for i in frames:
            i.configure(bg='#eafbea')
        for i in textos:
            i.configure(foreground='darkgreen')
        for i in botones:
            i.configure(bg='orange', fg='black')

    elif estilo.get() == "otono":
        for i in frames:
            i.configure(bg="#f5deb3")
        for i in textos:
            i.configure(fg='saddlebrown')
        for i in botones:
            i.configure(bg='chocolate', fg='white')
    else:
        for i in frames:
            i.configure(bg='SystemButtonFace')
        for i in textos:
            i.configure(foreground='black')
        for i in botones:
            i.configure(bg='SystemButtonFace', fg='black')


# Menú
def info():
    messagebox.showinfo("Acerca de", "Esta aplicación es para registrar el ingreso y egreso de datos, por ejemplo personas, vehículos o mercaderías.")
def ayuda():
    ayuda_texto = "Esta aplicación permite registrar entradas y salidas de vehículos o mercaderías.\n" \
                  "1. Ingrese los detalles en el campo correspondiente.\n" \
                  "2. Presione 'Registrar Entrada' para registrar una entrada.\n" \
                  "3. Presione 'Registrar Salida' para registrar una salida.\n" \
                  "4. Para eliminar un registro, selecciónelo y presione 'Eliminar registro'.\n" 
    messagebox.showinfo("Ayuda", ayuda_texto)

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)
menu_ayuda.add_command(label='Acerca de', command=info)
menu_ayuda.add_command(label='Sobre el uso', command=ayuda)

# Menú Estilos
menu_estilos = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Estilos', menu=menu_estilos)
menu_estilos.add_command(label='Estándar', command=estilo_estandar)
menu_estilos.add_command(label='Primavera', command=estilo_primavera)
menu_estilos.add_command(label='Noche', command=estilo_noche)
menu_estilos.add_command(label='Otoño', command=estilo_otono)


# Ingreso de tarea
frame_entrada = tk.Frame(ventana)
frame_entrada.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=100, pady=10)

frame_entrada.columnconfigure(0, weight=1)
frame_entrada.columnconfigure(1, weight=1)

etiqueta1 = tk.Label(frame_entrada, text="Ingrese detalles: ", font=('Arial', 12))
etiqueta1.grid(row=0, column=0, sticky="w")

ingreso_tarea = tk.Entry(frame_entrada, borderwidth= 4, font= ('Arial', 14))
ingreso_tarea.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

def agregar_ent():
    tarea = ingreso_tarea.get()
    tiempo_tarea = time.strftime("[%d/%m/%Y %H:%M:%S]")
    if tarea:
        lista_tareas.insert(tk.END, f"{tiempo_tarea} - Entrada - {tarea}")
        ingreso_tarea.delete(0, tk.END)
def agregar_sal():
    tarea = ingreso_tarea.get()
    tiempo_tarea = time.strftime("[%d/%m/%Y %H:%M:%S]")
    if tarea:
        lista_tareas.insert(tk.END, f"{tiempo_tarea} - Salida - {tarea}")
        ingreso_tarea.delete(0, tk.END)

boton_entrada = tk.Button(frame_entrada, text='Registar Entrada', command=agregar_ent, bd=4)
boton_entrada.grid(row=2, column=0, sticky="ew", pady=10, padx=40)
boton_salida = tk.Button(frame_entrada, text='Registar Salida', command=agregar_sal, bd=4)
boton_salida.grid(row=2, column=1, sticky="ew", pady=10, padx=40)

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        confirm = messagebox.askyesno(
            "Confirmar eliminación", 
            "¿Está seguro que desea eliminar el registro seleccionado?"
        )
        if confirm:
            lista_tareas.delete(seleccion)

def eliminar_lista():
    confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar todo el registro?")
    if confirm:
        lista_tareas.delete(0, tk.END)

frame_borrar= tk.Frame(ventana)
frame_borrar.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=100, pady=10)

frame_borrar.columnconfigure(0, weight=1)
frame_borrar.columnconfigure(1, weight=1)

boton_eliminar = tk.Button(frame_borrar, text='Eliminar registro', command=eliminar_tarea, bd=4)
boton_eliminar.grid(row=0, column=0, sticky="ew", pady=10, padx=40)
boton_eliminartodo = tk.Button(frame_borrar, text='Borrar todo el registro', command=eliminar_lista, bd=4)
boton_eliminartodo.grid(row=0, column=1, sticky="ew", pady=10, padx=40)

#Para que el cursor esté en la entrada al iniciar
ingreso_tarea.focus_set()

# Lista de tareas con desplazamiento

frame_lista = tk.Frame(ventana)
frame_lista.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=100, pady=10)

frame_lista.rowconfigure(1, weight=1)
frame_lista.columnconfigure(0, weight=1)

etiqueta3 = tk.Label(frame_lista, text="Registro ", font=('Arial', 12))
etiqueta3.grid(row=0, column=0, sticky="w")

lista_tareas = tk.Listbox(frame_lista, borderwidth=4, font= ('Arial', 14))
lista_tareas.grid(row=1, column=0, sticky="nsew")

etiqueta2 = tk.Label(frame_lista, text="Para eliminar algún registro debe seleccionarlo ", font=('Arial', 12))
etiqueta2.grid(row=2, column=0, sticky="w")

scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=lista_tareas.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
lista_tareas.config(yscrollcommand=scrollbar.set)

# Accesos directos con teclado
ventana.bind('<Return>', lambda event: agregar_ent())             # Enter
ventana.bind('<Shift-Return>', lambda event: agregar_sal())       # Shift+Enter
ventana.bind('<Delete>', lambda event: eliminar_tarea())          # Suprimir

ventana.mainloop()
