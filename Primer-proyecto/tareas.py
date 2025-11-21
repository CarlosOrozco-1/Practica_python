import json
import os

ARCHIVO_TAREAS = "mis_tareas.json"

# --- FUNCIONES ---

def cargar_tareas():
    """Lee el archivo JSON y devuelve una lista de tareas."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return [] 
    
    try:
        with open(ARCHIVO_TAREAS, "r") as archivo:
            return json.load(archivo)
    except:
        return []

# ERROR 1 CORREGIDO:
# Estas funciones deben estar pegadas al margen izquierdo, NO dentro de cargar_tareas
def guardar_tareas(tareas):
    """Escribe la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver Tareas")
    print("2. Agregar Tarea")
    print("3. Eliminar Tarea")
    print("4. Salir")

# --- FLUJO PRINCIPAL ---

def main():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- Tus Tareas ---")
            if not tareas:
                print("No tienes tareas pendientes.")
            else:
                for i, t in enumerate(tareas, start=1):
                    estado = "[x]" if t["completada"] else "[ ]"
                    print(f"{i}. {estado} {t['titulo']}")

        # ERROR 2 CORREGIDO:
        # Este elif estaba indentado dentro del bloque anterior. 
        # Debe estar al mismo nivel que el 'if opcion == "1"'
        elif opcion == "2":            
            titulo = input("Descripción de la tarea: ")
            nueva_tarea = {
                "titulo": titulo,
                "completada": False
            }
            tareas.append(nueva_tarea)
            guardar_tareas(tareas)
            print("Tarea guardada.")

        elif opcion == "3":
            # ERROR 3 CORREGIDO: Faltaba el bloque 'try' antes del except
            try:
                indice = int(input("Número de la tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    guardar_tareas(tareas)
                    print(f"Tarea '{tarea_eliminada['titulo']}' eliminada.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "4":
            print("Saliendo del gestor de tareas. ¡Hasta luego!")
            break   
        else:
            print("Opción no válida. Por favor elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()