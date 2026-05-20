au="usuario"
bc="contraseña"
contador=4
while contador>0:
    a=input("ingrese usuario: ").strip()
    b=input("ingrese contraseña: ").strip()
    a=a.lower()
    b=b.lower()
    if  a==au and b==bc:
        print("acceso concedido")
        contador=contador-1
    else:
        print("usuario o contraseñas incorrectos")

 