import sqlite3

# 1. Conexión a la base de datos SQLite
# Si el archivo de la base de datos no existe, se creará automáticamente.

nombre_db =  "escuela.db"
conexion = sqlite3.connect(nombre_db)

# El cursor es el objeto que nos permite ejecutar comandos SQL
cursor = conexion.cursor()

# 2. Creación de una tabla llamada "estudiantes"
# Usamos triple comilla """ para permitir múltiples líneas de texto

sql_create = """
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    carrera TEXT NOT NULL,
    edad INTEGER NOT NULL
)
"""
cursor.execute(sql_create)
print("Tabla 'estudiantes' creada con éxito.")

# 3. Inserción de datos en la tabla "estudiantes"

print("Insertando datos en la tabla 'estudiantes'...")

nuevos_estudiantes = [
    ("Ana", "García", "Ingeniería", 20),
    ("Luis", "Martínez", "Medicina", 22),
    ("María", "López", "Derecho", 21),
    ("Carlos", "Pérez", "Arquitectura", 23)]
cursor.executemany("INSERT INTO estudiantes (nombre, apellido, carrera, edad) VALUES (?, ?, ?, ?)", nuevos_estudiantes)

# Importante en Python: confirmar los cambios con commit()
conexion.commit()
print("Datos insertados con éxito.")

# 4. Consulta de datos en la tabla "estudiantes"

print("\nConsultando datos de la tabla 'estudiantes'...")

cursor.execute("SELECT * FROM estudiantes")
resultados = cursor.fetchall()
for estudiantes in resultados:
    # Estudiante es una tupla con los datos de cada fila
    id_estudiante, nombre, apellido, carrera, edad = estudiantes
    print(f"ID: {id_estudiante}, Nombre: {nombre}, Apellido: {apellido}, Carrera: {carrera}, Edad: {edad}")

# 5. cierre de la conexión a la base de datos
conexion.close()
print("Conexión a la base de datos cerrada.")

# Fin del archivo database.py
                   