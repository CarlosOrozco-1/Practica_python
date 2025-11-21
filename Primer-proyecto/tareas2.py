import json
import os

ARCHIVO_TAREAS = "mis_tareas.json"

# --- FUNCIONES (La lógica separada del flujo principal) ---

def cargar_tareas():
    """Lee el archivo JSON y devuelve una lista de tareas."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return [] # Si no existe el archivo, retornamos lista vacía
    
    try:
        with open(ARCHIVO_TAREAS, "r") as archivo:
            return json.load(archivo) # ¡Magia! Convierte texto JSON a lista/dicts de Python
    except:
        return []

def guardar_tareas(tareas):
    """Escribe la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w") as archivo:
        json.dump(tareas, archivo, indent=4) # dump() escribe los datos en el archivo

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver Tareas")
    print("2. Agregar Tarea")
    print("3. Eliminar Tarea")
    print("4. Salir")

# --- FLUJO PRINCIPAL (Main Loop) ---

def main():
    tareas = cargar_tareas() # Cargamos al inicio

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- TUS TAREAS ---")
            if not tareas:
                print("No tienes tareas pendientes.")
            else:
                # enumerate nos da el índice (i) y el valor (t) al mismo tiempo
                for i, t in enumerate(tareas, start=1): 
                    estado = "[x]" if t["completada"] else "[ ]"
                    print(f"{i}. {estado} {t['titulo']}")

        elif opcion == "2":
            titulo = input("Descripción de la tarea: ")
            # Creamos un diccionario (objeto JSON)
            nueva_tarea = {
                "titulo": titulo,
                "completada": False
            }
            tareas.append(nueva_tarea)
            guardar_tareas(tareas) # Guardamos cambios
            print("Tarea guardada.")

        elif opcion == "3":
            try:
                indice = int(input("Número de tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    eliminada = tareas.pop(indice)
                    guardar_tareas(tareas) # Guardamos cambios
                    print(f"Eliminada: {eliminada['titulo']}")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Debes ingresar un número.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# Esto es el equivalente al 'public static void main' de Java
# Asegura que este código solo corra si ejecutamos este archivo directamente
if __name__ == "__main__":
    main()