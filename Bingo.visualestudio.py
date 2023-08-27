import random
import tkinter as tk

def generar_carton():
    numeros = random.sample(range(1, 91), 15)
    carton = [numeros[:5], numeros[5:10], numeros[10:]]
    return carton

def llamar_numero():
    numero = random.randint(1, 90)
    lbl_numero.config(text=f"Número llamado: {numero}")
    if numero in numeros_llamados:
        llamar_numero()
    else:
        numeros_llamados.add(numero)
        verificar_carton(numero)

def verificar_carton(numero):
    for i in range(3):
        for j in range(5):
            if carton[i][j] == numero:
                lbl_carton[i][j].config(bg="green")
    
    for i in range(3):
        if all(lbl_carton[i][j]['bg'] == 'green' for j in range(5)):
            lbl_mensaje.config(text="¡Bingo! Has ganado.")
            btn_llamar.config(state=tk.DISABLED)
            return
    
    if len(numeros_llamados) == 90:
        lbl_mensaje.config(text="Fin del juego.")
        btn_llamar.config(state=tk.DISABLED)

# Crear ventana
ventana = tk.Tk()
ventana.title("Bingo")

# Generar cartón
carton = generar_carton()

# Crear etiquetas para mostrar el cartón
lbl_carton = []
for i in range(3):
    fila = []
    for j in range(5):
        numero = carton[i][j]
        lbl = tk.Label(ventana, text=str(numero), width=5, height=2, relief=tk.RAISED)
        lbl.grid(row=i, column=j, padx=5, pady=5)
        fila.append(lbl)
    lbl_carton.append(fila)

# Crear etiqueta para mostrar el número llamado
lbl_numero = tk.Label(ventana, text="Número llamado:", font=("Arial", 16))
lbl_numero.grid(row=3, column=0, columnspan=5, pady=10)

# Crear botón para llamar número
btn_llamar = tk.Button(ventana, text="Llamar número", font=("Arial", 14), command=llamar_numero)
btn_llamar.grid(row=4, column=0, columnspan=5, pady=10)

# Crear etiqueta para mostrar mensaje de resultado
lbl_mensaje = tk.Label(ventana, text="", font=("Arial", 16))
lbl_mensaje.grid(row=5, column=0, columnspan=5, pady=10)

# Conjunto para almacenar los números llamados
numeros_llamados = set()

# Iniciar ventana
ventana.mainloop()

