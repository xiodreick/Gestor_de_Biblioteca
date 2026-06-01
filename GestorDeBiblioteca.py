print(" 1.- iniciar sesion\n","2.- registrarse\n","3.- salir")
d=int(input("ingrese opcion: "))
au="usuario"
bc="contraseña"
nu=""
cu=""
inventario={
                "1.-":{"MoMo":2,"stock":5},
                "2.-":{"Raza De Bronce":3,"stock":3},
                "3.-":{"Tempestad En La Cordillera":3,"stock":3},
                "4.-":{"Mallko":3,"stock":3},
                "5.-":{"El Principito":3,"stock":3},
                "6.-":{"Mago De Oz":3,"stock":3},
                "7.-":{"Maria":3,"stock":3},
                "8.-":{"El Hombre Que Calculaba":3,"stock":3},
                "9.-":{"Heroes De Guerra":3,"stock":3},
                "10.-":{"Historia De Bolivia":3,"stock":3},
                "11.-":{"Borracho Estaba Pero Me Acuerdo":3,"stock":3}}
contador=3
if d==1:

        while contador>0:
            a=input("ingrese usuario: ")
            b=input("ingrese contraseña: ")
            if  a==au and b==bc:
                print("-- acceso concedido --\n","1.- ver inventario\n","2.- Añadir o Quitar\n","3.- Salir")
                e=int(input("ingrese opcion: "))
                if e==1:
                      print(inventario)
                break
            else:
                print("usuario o contraseña incorrectos")
                contador=contador-1
            
elif d==2:
        
    nu=input("ingrese nombre de usuario nuevo: ").strip()
    cu=input("ingrese contraseña (8 caracteres minimo): ").strip()
        
elif len(cu)>=8:
          print("contraseña guardada")
else:
          print("contraseña muy corta")
