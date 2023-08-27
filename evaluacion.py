
#alumnos = [["Juan",7],
#           ["Maria",10],
 #          ["Pablo",9],
 #          ["Florencia",6]]
#promedio = 0
#for persona in alumnos:
#    promedio = promedio + persona[1]
#promedio = promedio / len(alumnos)
#print("El promedio es: ", int(promedio))
#x = 20
#for i in range(x,0,-1):
 #       if(i % 2 == 0):
  #              print(i,end=" ")
#alumnos = [["Juan","Programacion"],
 #          ["Maria","Logica"],
  #         ["Pablo","Programacion"],
   #        ["Florencia","Modelado"]]
#def misAlumnos(alumnos):
 #   alumnos_programacion = []
  #  for personas in alumnos:
   #     if(personas[1] == "Programacion"):
    #        alumnos_programacion.append(personas)
    #return alumnos_programacion
#print(misAlumnos(alumnos))
listado = [["Azucar",600,2],
           ["Harina",300,3],
           ["Manteca",400,1]]
def sumaPrecios(carrito):
    total = 0
    for articulo in carrito:
        total += articulo[1]
    return total
print("Total = $", sumaPrecios(listado))

