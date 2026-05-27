print(" 1.- iniciar sesion\n","2.- registrarse\n","3.- salir")
d=int(input("ingrese opcion: "))
au="usuario"
bc="contraseña"
contador=3
if d==1:

        while contador>0:
            a=input("ingrese usuario: ")
            b=input("ingrese contraseña: ")
            if  a==au and b==bc:
                print("acceso concedido")
                break
            else:
                print("usuario o contraseña incorrectos")
                contador=contador-1
            
if d==2:
        
    nu=input("ingrese nombre de usuario nuevo: ").strip()
    cu=input("ingrese contraseña (8 caracteres minimo): ").strip()
        
elif len(cu)>=8:
          print("contraseña guardada")
else:
          print("contraseña muy corta")
