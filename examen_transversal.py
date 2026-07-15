Colección = []

#cada diccionario debe incluir el titutlo del libro, copias, prestamo y disponibilidad

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro\n2. Buscar libro\n3. Eliminar libro\n4. Actualizar disponibilidad\n5. Mostrar libros\n6. Salir")
    print("=====================================")

def opcion():
    op = int(input("Ingrese la opción que desea: "))
    if 1 <= op <= 6:
        return op
    else:
        print("Ingrese una opción especificada en el menu por favor.")
    
def validación_nombre(nom):
    if nom == " " or len(nom) == 0:
        return False
    else:
        return True
    
def validación_cantidad(copias):
    if copias <= 0:
        return False
    else:
        return True


def validación_periodo(duracion):
    if duracion <= 0:
        return False
    else:
        return True
    
    
    
def opcion_1(Colección):
    while True:
        print("Por favor, ingrese el titulo del libro")
        nom = str(input(""))
        validación_1 = validación_nombre(nom)
        if validación_1 == True:
            print("El titulo ha sido ingresado correctamente")
            break
        else:
            print("El titulo ingresado no es puede estar en blanco, no se ha podido registrar el libro.")
            break
    while validación_1 == True:
        print("Por favor, ingrese la cantidad de copias del libro")
        copias = int(input(""))
        validación_2 = validación_cantidad(copias)
        if validación_2 == True:
            print("La cantidad de copias ha sido ingresada correctamente")
            break
        else:
            print("La cantidad de copias no puede ser de 0 o menor, no se ha podido registrar el libro")
            break
    while validación_1 == True and validación_2 == True:
        print("Por favor, ingrese la cantidad de días que dura el periodo de prestamo")
        duracion = int(input(""))
        validación_3 = validación_periodo(duracion)
        if validación_3 == False:
            print("La cantidad de duración del prestamo no puede ser de 0 o menor, no se ha podido registrar el libro.")
            break
        elif validación_3 == True:
            print("La duración del prestamo ha sido registrada correctamente")
            Colección.append({"Nombre" : nom, "Cantidad de copias" : copias, "Días de prestamo" : duracion})
            break
            
            
def opción_2(titulo_buscar, Colección):
    for libro in Colección:
        if titulo_buscar == libro:
            return titulo_buscar
        else:
            return print("El titulo ingresado no se encuentra en la colección de la biblioteca")
            
def opción_5():
    for titulos in Colección:
            print(titulos)
    
    
    
while True:
    menu()
    op = opcion()
    if op == 1:
        opcion_1(Colección)
    elif op == 2:
        titulo_buscar = str(input("Ingrese el titulo del libro que desea pedir: "))
        opción_2()
    elif op == 5:
        opción_5()
    