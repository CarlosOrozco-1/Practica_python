print("--- Calculadora V2.0 ---")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Que operación deseas realizar? : ")

# Solicitar los números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Lógica para realizar la operación seleccionada
# En Python no existe la estructura switch-case, se usa if-elif-else

if opcion == '1':
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división de {num1} entre {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor selecciona una opción del 1 al 4.")

    # Fin del programa