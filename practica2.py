import time
import os

def limpiar():
    os.system("cls")

def numeros():
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    return num1, num2

def menus():
    while True:
        limpiar()
        print("Opciones")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            dividir()
        elif opcion == "5":
            print("Saliendo del programa")
            time.sleep(2)
            break
        else:
            print("Opcion invalida")
            time.sleep(2)

def sumar():
    limpiar()
    num1, num2 =numeros()
    print("Resultado =", num1 + num2)
    time.sleep(3)

def restar():
    limpiar()
    num1, num2 = numeros()
    print("Resultado =", num1 - num2)
    time.sleep(3)

def multiplicar():
    limpiar()
    num1, num2 = numeros()
    print("Resultado =", num1 * num2)
    time.sleep(3)

def dividir():
    limpiar()
    num1, num2 = numeros()
    if num2 == 0:
        print("No se puede dividir entre cero")
    else:
        print("Resultado =", num1 / num2)
    time.sleep(3)

if __name__ == "__main__":
    menus()
