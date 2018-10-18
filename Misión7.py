#DiegoArmandoAyalaHernández
#A01376727
#Menu que da la opcion para dividir o para encontrar un numero mayor
def dividir(dividendo, divisor):         # Recibe un dividendo y divisor y calcula el resultado 
    divedendo = dividendo
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    
    print('%d / %d = %d, sobra %d' % (divedendo, divisor, cociente, dividendo))

def encontrarMayor ():   # Devuelve el numéro mayor
    mayor = 0
    valor = int(input("Teclea un número [Teclea -1 para salir]: "))
    if valor == -1:
        print('No hay valor mayor')
    else:
        while valor != -1:
            numero = int(input("Teclea una serie de números para encontrar el mayor: "))
            if numero > mayor:
                mayor = numero
            if numero == -1:
                break
        print('El mayor es: ', mayor)

def menu ():                           # Despliega un menu con las 3 opciones que se pueden elegir
    print("Misión 07", "Ciclos While")
    print("Autor:", "Diego Armando Ayala Hernández")
    print("Marícula:", "A01376727")
    print("1.", "Calcular divisiones")
    print("2.", "Encontrar el mayor")
    print("3.", "Salir")
    opcion = int(input("Teclea tu opción: "))
    print("")
    return opcion

def main():        # Función principal
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            dividendo= int(input("Dividendo:"))
            divisor=int(input("divisor:"))
            dividir(dividendo, divisor)
        if opcion == 2:
            encontrarMayor()
        if opcion != 1 and opcion != 2 and opcion != 3:
            print('Error', ',' 'Teclea 1, 2 o 3')
        print('')
        print('')
        opcion = menu()
    if opcion == 3:
        print("Gracias por utilizar este programa, regresa pronto.")

main()  # Llama a la función principal
