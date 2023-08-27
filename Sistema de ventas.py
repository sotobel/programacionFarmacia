import tkinter as tk
from tkinter import messagebox
class VentanaInicioSesion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")

        # Etiqueta y campo de entrada para el nombre de usuario
        tk.Label(root, text="Nombre de Usuario:").pack()
        self.usuario_entry = tk.Entry(root)
        self.usuario_entry.pack()

        # Etiqueta y campo de entrada para la contraseña
        tk.Label(root, text="Contraseña:").pack()
        self.contrasena_entry = tk.Entry(root, show="*")  # Muestra asteriscos para la contraseña
        self.contrasena_entry.pack()

        # Botón de inicio de sesión
        tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion).pack()

    def iniciar_sesion(self):
        # Aquí puedes verificar las credenciales del usuario
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        # Ejemplo simple: verifica si el usuario y la contraseña son correctos
        if usuario == "usuario" and contrasena == "contrasena":
            messagebox.showinfo("Inicio de Sesión", "Sesión iniciada con éxito.")
            self.root.destroy()  # Cierra la ventana de inicio de sesión
        else:
            messagebox.showerror("Error de Inicio de Sesión", "Credenciales incorrectas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaInicioSesion(root)
    root.mainloop()

class SistemaDeVentas:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")  # Ancho x Alto
        self.root.title("Sistema de Ventas")

        self.productos = {
            "Paracetamol": 2.5,
            "Ibuprofeno": 3.0,
            "Vitamina C": 5.0,
            "Jarabe para la tos": 4.5,
            # Agrega más productos y precios aquí
        }

        self.carrito = {}
        self.total = 0.0

        self.etiqueta_producto = tk.Label(root, text="Producto:")
        self.etiqueta_producto.pack()
        self.producto_var = tk.StringVar()
        self.menu_productos = tk.OptionMenu(root, self.producto_var, *self.productos.keys())
        self.menu_productos.pack()

        self.etiqueta_cantidad = tk.Label(root, text="Cantidad:")
        self.etiqueta_cantidad.pack()
        self.cantidad_var = tk.IntVar()
        self.entry_cantidad = tk.Entry(root, textvariable=self.cantidad_var)
        self.entry_cantidad.pack()

        self.boton_agregar = tk.Button(root, text="Agregar al Carrito", command=self.agregar_al_carrito)
        self.boton_agregar.pack()

        self.boton_facturar = tk.Button(root, text="Facturar", command=self.mostrar_factura)
        self.boton_facturar.pack()

    def agregar_al_carrito(self):
        producto = self.producto_var.get()
        cantidad = self.cantidad_var.get()

        if producto in self.productos and cantidad > 0:
            if producto in self.carrito:
                self.carrito[producto] += cantidad
            else:
                self.carrito[producto] = cantidad

            self.total += self.productos[producto] * cantidad

            messagebox.showinfo("Éxito", f"Se agregó {cantidad} {producto} al carrito.")
        else:
            messagebox.showerror("Error", "Producto o cantidad no válidos.")

    def mostrar_factura(self):
        if not self.carrito:
            messagebox.showerror("Error", "El carrito está vacío.")
            return

        factura = "Factura de Compra:\n\n"
        for producto, cantidad in self.carrito.items():
            factura += f"{producto}: {cantidad} unidades\n"

        factura += f"\nTotal a Pagar: ${self.total:.2f}"

        messagebox.showinfo("Factura", factura)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDeVentas(root)
    root.mainloop()