import json
import os

ARCHIVO_TAREAS = "mis_tareas_objeto.json"

# Definición de la clase Tarea

class Tarea:
    def __init__(self, titulo, completada=False):
        self.titulo = titulo
        self.completada = completada
        
    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "✓" if self.completada else "✗"
        return f"{estado} {self.titulo}"
    
    # Importante: Método para convertir el objeto a un diccionario
    # Esto es necesario para que json.dump() pueda guardar el objeto

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "completada": self.completada
        }
    
# 2. Logíca de persistencia

def guardar_tareas(lista_de_objetos):
    # Convertimos la lista de Objetos Tarea a lista de Diccionarios
    # Usamos List Comprehension: [t.to_dict() for t in lista]
    datos_para_json  = [t.to_dict() for t in lista_de_objetos]

    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(datos_para_json, f, indent=4)

def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    
    try:
        with open(ARCHIVO_TAREAS, "r") as f:
            datos_cargados = json.load(f)
            # Convertimos la lista de Diccionarios a lista de Objetos Tarea
            # Reconstruimos cada objeto Tarea usando Tarea(**d)

            mis_objetos = []
            for d in lista_diccionarios:
                # Instanciamos la clase con los datos del diccionario

                nueva_tarea = Tarea(d["titulo"], d["completada"])
                mis_objetos.append(nueva_tarea)
                return mis_objetos
    except json.JSONDecodeError:
        return []
    
    # 3. Menu y lógica de la aplicación
def main():
        mis_tareas = cargar_tareas() # Lista de objetos Tarea

        while True:
            print("\n--- Gestor de Tareas ---")
            print("1. Ver tareas")
            print("2. Agregar tarea")
            print("3. Marcar tarea como completada") # Nueva opción
            print("4. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                for i, tarea in enumerate(mis_tareas, start=1):
                    # Usamos el __str__ de la clase Tarea
                    print(f"{i}. {tarea}")

            elif opcion == "2":
                        titulo_tarea = input("Ingresa el título de la tarea: ")
                    # Instanciamos la clase (usamos POO)
                        nueva_tarea = Tarea(titulo_tarea)
                        mis_tareas.append(nueva_tarea)
                        guardar_tareas(mis_tareas)
                        print("Tarea agregada con éxito!")

            elif opcion == "3":
                try:
                    idx = int(input("Número de la tarea a completar: ")) - 1
                    if 0 <= idx < len(mis_tareas):
                     # LLamamos al método completar del objeto Tarea
                        mis_tareas[idx].completar()
                        guardar_tareas(mis_tareas)
                        print("Tarea completada con éxito!")
                except ValueError:
                        print("Por favor, ingresa un número válido.")

            elif opcion == "4":
                print("¡Hasta luego!")
                break
            
if __name__ == "__main__":
    main()