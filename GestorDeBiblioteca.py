a=input("ingrese usuario: ")
b=input("ingrese contraseña: ")
au="usuario"
ac="contraseña"
a=a.lower()
b=b.lower()
contador=1
while contador<=3:
    if a!=au and b!=ac:
        print("contraseña o usuario incorrectos")
    contador=contador+1
else:
    print("bienvenido ", a)
 