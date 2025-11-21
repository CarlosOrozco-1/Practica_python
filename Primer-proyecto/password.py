import random # Importa el módulo random para generar números aleatorios libreria estandar
import string # Importa el módulo string para operaciones con cadenas libreria estandar


print("Generador de Contraseñas Seguras")

# Solicitar la longitud de la contraseña al usuario
# Asegurarse de que la longitud sea un número entero válido
# Bucle hasta que se obtenga una entrada válida

carcateres = string.ascii_letters + string.digits + string.punctuation

# Pedimos al usuario la longitud de la contraseña

try:
    Longitud = int(input("Ingresa la longitud deseada para la contraseña (mínimo 8 caracteres): "))

    if Longitud < 8:
        print("La longitud mínima recomendada es de 8 caracteres. Por favor, intenta de nuevo.")


    # 3. La Magia (List Comprehension vs Bucle tradicional)
    # Opción A (Estilo Clásico):
    # password_lista = []
    # for i in range(longitud):
    #     char = random.choice(caracteres)
    #     password_lista.append(char)

    # Opción B (Estilo Python Pro - "List Comprehension"):
    # Es una forma de crear listas en una sola línea. Muy potente.

    password_lista = [random.choice(carcateres) for _ in range(Longitud)]

    # 4. Convertir la lista en una cadena
    password = ''.join(password_lista)
    print(f"Tu contraseña segura es: {password}")

except ValueError:
    print("Por favor, ingresa un número entero válido para la longitud de la contraseña.")

# Fin del programa
