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

print("\nHola usuario ahora estas entrando a una calculadora")
print("\npor favor ingresa dos numeros para hacer las operaciones")

a= float(input("\nIngresa el primer numero: "))
b= float(input("\nIngresa el segundo numero: "))

print("\nOperaciones")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

operacion= input("\nPor favor elige la operacion (1/2/3/4): ")

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