import random # Importa el módulo random para generar números aleatorios libreria estandar

print("¡Bienvenido al juego de adivinanza de números!")

# Genera un número aleatorio entre 1 y 100
# Nota: random.randint(a, b) incluye ambos extremos a y b

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 10

print("He seleccionado un número entre 1 y 100.")

# Bucle principal del juego, bucle infinito hasta que se rompa con break
while True:
    try:
        entrada = input("Tu intento: ")
        numero_usuario = int(entrada)  # Convierte la entrada a entero
        intentos += 1 # Incrementa el contador de intentos

        if numero_usuario == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
            break  # Sale del bucle si el usuario adivina correctamente
        elif numero_usuario < numero_secreto:
            print("Más alto... busca un número mayor.")
        else:
            print("Más bajo... busca un número menor.")

        if intentos >= max_intentos:
            print(f"Lo siento, has alcanzado el máximo de intentos. El número era {numero_secreto}.")
            break  # Sale del bucle si se alcanzan los intentos máximos
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Fin del juego
