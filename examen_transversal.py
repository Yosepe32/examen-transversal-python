Colección = []

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
            Colección.append({"Nombre" : nom, "Cantidad de copias" : copias, "Días de prestamo" : duracion, "Estado" : "Disponible"})
            break
            
            
def opción_2(titulo_buscar, Colección):
    for i in Colección:
        if i["Nombre"] == titulo_buscar:
            print(i)
        else:
            print(f"El libro {titulo_buscar} no se encuentra registrado en la biblioteca..")
            
def opción_3(titulo_buscar, Colección):
    for i in Colección:
        count = -1 + 1
        if i["Nombre"] == titulo_buscar:
            del Colección[count]
            print("El libro se ha eliminado correctamente.")
        else:
            print(f"El libro {titulo_buscar} no existe en la biblioteca.")
            
def opción_5():
    print("=== LISTA DE LIBROS ===")
    for titulos in Colección:
        print("********************************************")
        print(titulos)
        print("********************************************")

def opcion_6():
    print("Gracias por usar el sistema. Vuelva Pronto")
    return True
    
    
while True:
    menu()
    op = opcion()
    if op == 1:
        opcion_1(Colección)
    elif op == 2:
        titulo_buscar = str(input("Ingrese el titulo del libro que desea pedir: "))
        opción_2(titulo_buscar, Colección)
    elif op == 3:
        titulo_buscar = str(input("Ingrese el titulo del nombre que desea eliminar: "))
        opción_3(titulo_buscar, Colección)
    elif op == 5:
        opción_5()
    elif op == 6:
        finalización = opcion_6()
        if finalización == True:
            break    