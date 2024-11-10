#Proyecto: Calculadora Básica
#Objetivo: Crear un programa que permita al usuario ingresar dos números y elegir una operación (suma, resta, multiplicación o división). El programa debe mostrar el resultado de la operación seleccionada.

#Instrucciones:
#Solicitar entrada del usuario: Pregunta al usuario por dos números y por qué operación desea realizar.
#Realizar la operación: Basado en la opción elegida, realiza la operación y muestra el resultado.
#Validación: Asegúrate de manejar el caso de la división por cero.
#Ejemplo de flujo:
#El programa muestra un menú de operaciones.
#El usuario ingresa los números y selecciona la operación.
#El programa muestra el resultado de la operación.

def realizar_calculo():
    print("\n¡Bienvenido a la calculadora basica! Vamos a hacer algunos calculos")

    try:
        a= float(input("Ingresa el primer numero: "))
        b= float(input("Ingresa el segundo numero: "))
    except ValueError:
        print("\nError: Por favor ingrese numeros validos")
        return

    print("\nOperaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    operacion= input("\nPor favor elige la operacion (1/2/3/4): ")

    while operacion not in["1", "2", "3", "4"]:
        operacion = input("\nPor favor elige una operacion valida (1/2/3/4)")

    if operacion == "1":
        resultado= a + b
        print("\nEl resultado de la suma es:", resultado)
    elif operacion == "2":
        resultado= a-b
        print("\nEl resultado de la resta es:", resultado)
    elif operacion =="3":
        resultado= a * b
        print("\nEl resultado de la multiplicacion es:", resultado)
    elif operacion == "4":
        if b != 0:
            resultado= a / b
            print("\nEl resultado de la division es:", resultado)
        else:
            print("\nError: No se puede dividir entre cero")
    else:
        print("\nOpcion invalida")

while True:
    realizar_calculo()
    continuar = input("\n¿Quieres hacer otra operacion? (si/no): ").lower()
    if continuar!= "si":
        print("\nGracias por usa la calculadora.")
        break