from data_stark import lista_personajes
from os import system

def menu():
    from os import system
    system("cls")


    print("         *** Menu **** ")
    print("1.Nombre de cada superheroe")
    print("2.Nombre y altura de cada superheroe")
    print("3.El superhéroe más alto")
    print("4.el superhéroe más bajo")
    print("5.Promedio de los superhéroes")
    print("6.Nombre del superhéroe asociado al max y min")
    print("7.El superhéroe más y menos pesado.")
    print("10.Salir")

    opcion = input("Ingrese opcion: ")
    return opcion

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def nombre_superheroe(lista_personajes):
    """Nombre de cada superheroe

    Args:
        lista_personajes (string): Me trae cada nombre que este en el diccionario 
    """
    for superheroe in lista_personajes:
        nombre = superheroe['nombre']
        print(f"Nombres de Superhéroes:{nombre}")
# nombre_superheroe(lista_personajes)

# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def nombre_y_altura(nombre, altura):
    for elemento in lista_personajes:
        nombre = elemento['nombre']
        altura = elemento['altura']
        print(f"Nombre: {nombre} \n Altura: {altura}")
# nombre_y_altura("nombre", "altura")

# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

def superhero_mas_alto (lista_personajes):
    max_altura = 0

    for elemento in lista_personajes:
        altura_cadena = elemento['altura']
        altura = float(altura_cadena)
        if altura > max_altura:
            max_altura = altura

    print(f"El superheroe mas alto mide: {max_altura} cm")

# superhero_mas_alto(lista_personajes)

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

def superhero_mas_bajo (lista_personajes):
    """Superheroe mas bajo

    Args:
        lista_personajes (string): comienza desde el segundo elemento hacia adelante, asi obtengo todos los elementos para poder trabajar con el resto de los elementos
    """
    primera_altura_dela_cadena = lista_personajes[0]['altura']
    min_altura = float(primera_altura_dela_cadena)

    for elemento in lista_personajes[1:]:
        altura_cadena = elemento['altura']
        altura = float(altura_cadena)
        if altura == None or altura < min_altura:
            min_altura = altura

    print(f"El superheroe mas bajo mide: {min_altura} cm")
# superhero_mas_bajo(lista_personajes)

# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)

def promedio_De_alturas (lista_personajes):
    suma_alturas = 0
    cantidad_personajes = len(lista_personajes)

    for personaje in lista_personajes:
        altura_cadena = personaje['altura']
        altura = float(altura_cadena)
        suma_alturas += altura

        promedio = suma_alturas / cantidad_personajes
    print(f"El promedio de las alturas es: {promedio} cm ")
# promedio_De_alturas(lista_personajes)

# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)



def nombres_de_los_superheroes():
    altura = None
    for elemento in lista_personajes:
        max_altura= float(elemento['altura'])
        nombre = elemento['nombre']
        
        if altura == None or altura < max_altura:
            altura = max_altura
            nombre_del_mas_bajo = nombre 
    mensaje = f"El superheroe mas alto mide: {max_altura}  cm y su nombre es {nombre_del_mas_bajo}"
    return mensaje
# print(nombres_de_los_superheroes())


# H. Calcular e informar cual es el superhéroe más y menos pesado.

def super_mas_pesado():
    peso_mas_pesado = None
    peso_mas_liviano = None

    for mas_pesados in lista_personajes:
        cadena_peso = float(mas_pesados['peso'])
        nombre = mas_pesados['nombre']

        if peso_mas_pesado == None or peso_mas_pesado < cadena_peso:
            peso_mas_pesado = cadena_peso
            nombre_Del_mas_pesado = nombre

        if peso_mas_liviano == None or peso_mas_liviano > cadena_peso:
            peso_mas_liviano = cadena_peso
            nombre_del_mas_liviano = nombre

    mensaje = f"eL superheroe mas pesado es {nombre_Del_mas_pesado} y pesa {peso_mas_pesado} kg \n el superheroe mas liviando es {nombre_del_mas_liviano} y pesa {peso_mas_liviano}"
    return mensaje
    
# print(super_mas_pesado()) 

# I. Ordenar el código implementando una función para cada uno de los valores
# informados.

while True:
    match (menu()):
        case "1":
            nombre_superheroe(lista_personajes)
        case "2":
            nombre_y_altura("nombre", "altura")
        case "3":
            superhero_mas_alto(lista_personajes)
        case "4":
            superhero_mas_bajo(lista_personajes)
        case "5":
            promedio_De_alturas(lista_personajes)

        case "6":
            print(nombres_de_los_superheroes())

        case "7":
            print(super_mas_pesado())
        case "10":
            break

    system("pause")
