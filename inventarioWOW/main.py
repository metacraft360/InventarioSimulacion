from herramientas import mostrar_mochila, eliminar_objeto, añadir_objeto, guardar_inventario, cargar_datos

print ("***Bienvenido al inventario***\n¿Que deseas hacer?\nMostrar inventario (1)\nAñadir objeto(2)\nEliminar objeto(3)")
a = True
mochila_usuario = cargar_datos()
while a:
    b = True
    try:
        accion = int(input("Elige (1-3)\n"))
        if accion == 1:
            if len(mochila_usuario) <= 0:
                print("Tu mochila esta vacía, farmea cabron")
            else:
                mostrar_mochila(mochila_usuario)
        elif accion == 2:
            añadir_objeto(mochila_usuario)
        elif accion == 3:
            eliminar_objeto(mochila_usuario)
        else:
            print ("Elige entre (1-3)")
        while b:
            try:
                salir = input("Quieres salir de la mochila(y/n)")
                if salir == "y":
                    print ("Saliendo de la mochia。。。")
                    a = False
                    b = False
                    guardar_inventario(mochila_usuario)
                elif salir == "n":
                    b = False
                else:
                    print ("Elige entre (y/n)")
                pass
            except ValueError:
                print ("Elige ente (y/n)")
        
        

    except ValueError:
        print ("Elige un numero")




