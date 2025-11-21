#Definición de la Clase

class Tarea:
    #Constructor de la clase
    # En TS: constructor(titulo: string) { ... }
    # En Python: def __init__(self, titulo):
    
    def __init__(self, titulo):
        # ATRIBUTOS
        # En TS: this.titulo = titulo;
        self.titulo = titulo
        self.completada = False # Por defecto, la tarea no está completada
        
    # MÉTODO (Void)
    # En TS: marcarCompletada() { ... }
    # En Python: siempre el primer parámetro es 'self'
    def completar(self):
        self.completada = True
        print(f"Tarea '{self.titulo}' marcada como completada.")
        
        #MÉTODO (Devuelve un valor)
    def __str__(self):
        # Este método mágico es como el .toString() de Java
        # Define cómo se ve el objeto si haces print(objeto)  
        estado = "[x]" if self.completada else "[ ]"
        return f"{estado} {self.titulo}"
# --- USO DE LA CLASE ---
# Instanciación (¡Ojo! No se usa la palabra 'new')
# En TS: const t1 = new Tarea("Aprender Python");

t1= Tarea("Aprender Python")
t2= Tarea("Configurar vsCode")

# Uso de métodos
print("--- Antes de completar ---")

print(t1) # Llama a t1.__str__()
print(t2)

print("\n--- Después de completar ---")
t1.completar() # Marca la tarea 1 como completada

print("\n--- Estado final ---")
print(t1)
print(t2)

# Acceder a atributos directamente
print(f"\nEl título de la tarea 2 es: {t2.titulo}")

#fin del archivo clases.py