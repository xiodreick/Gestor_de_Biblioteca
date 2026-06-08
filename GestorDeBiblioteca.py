# unico usuario
usuario_admin="infocal"
contraseña_admin="contraseña1234"

# Inventario inicial con campos de 'nombre', 'stock' y 'precio'
inventario={
    "1": {"nombre": "MoMo", "stock": 5, "precio": 12},
    "2": {"nombre": "Raza De Bronce", "stock": 32, "precio": 15},
    "3": {"nombre": "Tempestad En La Cordillera", "stock": 12, "precio": 18},
    "4": {"nombre": "Mallko", "stock": 40, "precio": 10},
    "5": {"nombre": "El Principito", "stock": 23, "precio": 8},
    "6": {"nombre": "Mago De Oz", "stock": 35, "precio": 9},
    "7": {"nombre": "Maria", "stock": 53, "precio": 11},
    "8": {"nombre": "El Hombre Que Calculaba", "stock": 31, "precio": 14},
    "9": {"nombre": "Heroes De Guerra", "stock": 39, "precio": 16},
    "10": {"nombre": "Historia De Bolivia", "stock": 13, "precio": 20},
    "11": {"nombre": "Borracho Estaba Pero Me Acuerdo", "stock": 23, "precio": 13}}
print("1.- Iniciar sesion\n2.- Salir")
opcion=int(input("Ingrese opcion: "))
#primer uso del if para validar inicio de sesion
if opcion==1:
    contador=3
    while contador > 0:
        #el uso de strip y lower para evitar errores por mayúsculas o espacios accidentales (no es muy recomendable en un login pero ayuda si el usuario no esta acostumbrado a escribir sin errores)
        a=input("Ingrese usuario: ").strip().lower()
        b=input("Ingrese contraseña: ").strip().lower()
        if a==usuario_admin and b==contraseña_admin:
            print("\n-- ACCESO CONCEDIDO --")
            #while para mantener el programa activo hasta que el usuario decida salir (muestra las opciones 1,2,3 y 4 del menú)
            while True:
                print("\n1.- Ver inventario\n2.- Modificar cantidad y precio\n3.- Añadir nuevo libro\n4.- Salir")
                e=int(input("Ingrese opcion: "))
                #muestra el inventario de forma ordenada con stock y precio
                if e==1:
                    print("\n--- INVENTARIO ACTUAL ---")
                    #.join para mostrar el inventario en líneas separadas y con formato personalizado
                    #.items() para recorrer el diccionario del inventario y mostrar cada libro con su número, nombre, stock y precio
                    #for para llamar a cada libro por su número (clave) y mostrar sus datos (nombre, stock y precio) de forma clara
                    print("\n".join(f"[{clave}] {datos['nombre']} - Stock: {datos['stock']} - Precio: {datos['precio']} Bs." for clave, datos in inventario.items()))
                #modifica el stock y precio de un libro ya existente
                elif e==2:
                    #input porque la clave esta en formato string (el numero esta en texto), strip para eliminar espacios y evitar errores
                    clave=input("\nIngrese el número del libro a modificar: ").strip()
                    if clave in inventario:
                        nuevo_stock=int(input(f"Nuevo stock para '{inventario[clave]['nombre']}': "))
                        
                        #uso de .recplace para borrar en caso de que el usuario ingrese "Bs" o puntos o espacios al modificar el precio
                        entrada_precio=input(f"Nuevo precio para '{inventario[clave]['nombre']}' (en Bs.): ").lower()
                        precio_limpio=entrada_precio.replace("bs", "").replace(".", "").replace(" ", "")
                        
                        inventario[clave]['precio']=int(precio_limpio)
                        inventario[clave]['stock']=nuevo_stock
                        print("Libro actualizado")
                    else:
                        print("El numero del libro no existe.")
                #añade un nuevo libro al inventario con su nombre, stock y precio
                elif e==3:
                    nuevo_libro=str(len(inventario) + 1)
                    nombre=input("\nNombre del nuevo libro: ").strip()
                    stock=int(input("Cantidad o stock inicial: "))
                    
                    #uso de .recplace para borrar en caso de que el usuario ingrese "Bs" o puntos o espacios al añadir un nuevo libro
                    entrada_precio=input("Precio del libro (sin decimales): ").lower()
                    precio_limpio=entrada_precio.replace("bs", "").replace(".", "").replace(" ", "")
                    
                    inventario[nuevo_libro]={"nombre": nombre, "stock": stock, "precio": int(precio_limpio)}
                    print(f"'{nombre}' añadido con éxito bajo el numero {nuevo_libro}")
                #salir del programa en caso de que no se requiera iniciar sesion o despues de acabar las modificaciones   
                elif e==4:
                    print("Saliendo del programa")
                    print("---VUELVA PRONTO---")  
                    break
            break
        else:
            contador=contador-1
            print(f"USUARIO O CONTRASEÑA INCORRECTOS.\nIntentos restantes: {contador}")
            if contador==0:
                print("SE AGOTARON LOS INTENTOS.")
elif opcion==2:
    print("\nSaliendo del programa")
    print("---VUELVA PRONTO---")
