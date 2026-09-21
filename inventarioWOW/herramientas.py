def mostrar_mochila(inventario):
    for objetos in inventario:
        print (f"-{objetos}")
def añadir_objeto(inventario):
    print ("Este es tu inventario actual")
    for objetos in inventario:
        print (f"-{objetos}")
    print("Que objeto deseas añadir")
    objeto = input("")
    inventario.append(objeto)
    print(f"{objeto} ha sido añadido al inventario correctamente")
def eliminar_objeto(inventario):
    a = True
    numero_objetos = len(inventario)    
    
    if numero_objetos > 0:
        while a == True:
            for objetos in inventario:
                print (f"-{objetos}")
            objeto_a_eliminar = input("Elige un objeto del inventario\n")
            if objeto_a_eliminar in inventario:
                inventario.remove(objeto_a_eliminar)
                print ("Eliminado correctamente")
                a = False
            else:
                print ("Ese objeto no esta en el inventario, elige de nuevo")
    elif numero_objetos <= 0:
        print("No hay nada en el inventario")
def guardar_inventario(inventario):
    with open("mochila.txt", "w") as archivo:
        for objetos in inventario:
            archivo.write(f"{objetos}\n")
        print ("Mochila guardada en el PC")
def cargar_datos():
    mochila = []
    try:
        with open("mochila.txt", "r") as archivo:
            for objetos in archivo:
                objeto_limpio = objetos.strip()
                mochila.append(objeto_limpio)
    except FileNotFoundError:
        pass
    return mochila

    

        

    
    
