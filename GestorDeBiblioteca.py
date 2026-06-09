usuario_principal="infocal"
contraseña_principal="contraseña1234"

# aqui se depositara el nuevo usuario junto a su inventario desde cero
usuario_2=""
contraseña_2=""
inventario_2={}

# Inventario del usuario principal
inventario_principal={
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


# bucle principal para que el programa regrese al menu despues de registrarse o cerrar sesion
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("\n1.- Iniciar sesion\n2.- Registrar nuevo usuario\n3.- Salir")
    opcion=int(input("Ingrese opcion: "))

    # primer uso del if para validar inicio de sesion
    if opcion==1:
        contador=3
        # while para limitar los intentos de inicio de sesion a 3
        while contador > 0:
            # el uso de strip y lower para evitar errores por mayusculas o espacios accidentales (no es muy recomendable en un login pero ayuda si el usuario no esta acostumbrado a escribir sin errores)
            a=input("Ingrese usuario: ").strip().lower()
            b=input("Ingrese contraseña: ").strip().lower()
            # colocamos verificado en False por defecto para que solo se vuelva True si se cumplen las condiciones de validación
            verificado=False
            # Validacion para el usuario principal
            if a==usuario_principal and b==contraseña_principal:
                print("\n--- ACCESO CONCEDIDO USUARIO PRINCIPAL ---")
                # llamamos al inventario del usuario principal
                inventario=inventario_principal  
                verificado=True
            # Validacion para el segundo usuario (solo si ya se registro)
            elif usuario_2 != "" and a==usuario_2 and b==contraseña_2:
                print(f"\n--- ACCESO CONCEDIDO ({usuario_2.upper()}) ---")
                # llamamos al inventario del segundo usuario
                inventario=inventario_2  
                verificado=True
            else:
                verificado=False
            # Si el usuario se verifica correctamente, se le muestra el menu de inventario, si no se le resta un intento y se le informa de los intentos restantes
            if verificado:
                # while para mantener el programa activo hasta que el usuario decida salir
                while True:
                    print("\n1.- Ver inventario\n2.- Modificar cantidad y precio\n3.- Añadir libro\n4.- Eliminar libro\n5.- Salir al menu principal")
                    e=int(input("Ingrese opcion: "))  
                    # muestra el inventario de forma ordenada con stock y precio
                    if e==1:
                        print("\n--- INVENTARIO ACTUAL ---")
                        # es para cuando el segundo usuario acaba de crear su cuenta y aun no tiene libros añadidos
                        if len(inventario)==0:
                            print("El inventario esta vacio. Añada un libro en la opcion 3.")
                        else:
                            # .join para mostrar el inventario en lineas separadas y con el formato personalizado
                            print("\n".join(f"[{clave}] {datos['nombre']} - Stock: {datos['stock']} - Precio: {datos['precio']} Bs." for clave, datos in inventario.items()))
                    
                    # modifica el stock y precio de un libro ya existente
                    elif e==2:
                        numero_libro=input("\nIngrese el numero del libro a modificar: ").strip()
                        if numero_libro in inventario:
                            nuevo_stock=int(input(f"Nuevo stock para '{inventario[numero_libro]['nombre']}': "))
                            nuevo_precio=input(f"Nuevo precio para '{inventario[numero_libro]['nombre']}' (en Bs.): ").lower()
                            # .replace para eliminar extras inecesarios que puedan llegar a escribirse (los mas comunes)
                            precio_actualizado=nuevo_precio.replace("bs", "").replace(".", "").replace(" ", "").replace(",", "").replace("BS", "")
                            inventario[numero_libro]['precio']=int(precio_actualizado)
                            inventario[numero_libro]['stock']=nuevo_stock
                            print("\nLibro actualizado")
                        else:
                            print("\nEl numero del libro no existe.")
                    
                    # añade un nuevo libro al inventario con su nombre, stock y precio
                    elif e==3:
                        nuevo_libro=str(len(inventario) + 1)
                        nombre=input("\nNombre del nuevo libro: ").strip()
                        stock=int(input("Cantidad o stock inicial: "))
                        nuevo_precio=input("Precio del libro (sin decimales): ").lower()
                        precio_actualizado=nuevo_precio.replace("bs", "").replace(".", "").replace(" ", "").replace(",", "").replace("BS", "")
                        inventario[nuevo_libro]={"nombre": nombre, "stock": stock, "precio": int(precio_actualizado)}
                        print(f"'{nombre}' añadido con éxito bajo el numero {nuevo_libro}")
                    # elimina un libro existente del inventario actual
                    elif e==4:
                        numero_libro=input("\nIngrese el número del libro que desea eliminar: ").strip()
                        if numero_libro in inventario:
                            nombre_eliminado=inventario[numero_libro]['nombre']
                            del inventario[numero_libro]
                            print(f"El libro '{nombre_eliminado}' ha sido eliminado correctamente.")
                        else:
                            print("El numero del libro no existe.")
                    # con esto volvemos al menu principal para iniciar sesion o registrar un nuevo usuario
                    elif e==5:
                        print("Cerrando sesion...")
                        # break para salir del menu del inventario y volver al menu principal
                        break
                # break para salir del bucle de intentos una vez que el usuario ha cerrado sesion    
                break  
            else:
                contador=contador - 1
                print(f"USUARIO O CONTRASEÑA INCORRECTOS.\nIntentos restantes: {contador}")
                if contador==0:
                    print("SE AGOTARON LOS INTENTOS.")
                    #break para salir del bucle  de intentos
                    break 

    # para registrar al nuevo usuario
    elif opcion==2:
        print("\n--- REGISTRO DE NUEVO USUARIO ---")
        nuevo_usuario=input("Ingrese nombre de nuevo usuario: ").strip().lower()
        
        # para que el nuevo usuario no use el mismo nombre que el usuario principal
        if nuevo_usuario==usuario_principal:
            print("Ese nombre de usuario ya esta ocupado por el usuario principal.")
        else:
            usuario_2=nuevo_usuario
            contraseña_2=input(f"Agregue una contraseña a {usuario_2}: ").strip().lower()
            print(f"\n'{usuario_2}' registrado con exito. Su inventario se encuentra vacio por el momento.")
    # cerrar el programa
    elif opcion==3:
        print("\nSaliendo del programa")
        print("---VUELVA PRONTO---")
        break
