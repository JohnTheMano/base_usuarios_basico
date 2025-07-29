import sqlite3

# Crear la conexión y la tabla
conexion = sqlite3.connect("base_usuarios.db")
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS base_usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    edad INTEGER,
    direccion TEXT
)
""")
conexion.commit()
conexion.close()

# Función para crear usuario con todos los campos
def crear_usuario(nombre, email, edad, direccion):
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO base_usuarios (nombre, email, edad, direccion) VALUES (?, ?, ?, ?)", 
        (nombre, email, edad, direccion))
    conexion.commit()
    conexion.close()
    print("Usuario creado con éxito")

# Función para leer usuarios
def leer_usuario():
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM base_usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    if usuarios:
        print("Usuarios encontrados:")
        for usuario in usuarios:
            print(f'ID = {usuario[0]} - Nombre = {usuario[1]} - Email = {usuario[2]} - Edad = {usuario[3]} - Dirección = {usuario[4]}')
    else:
        print("No se encontró ningún usuario.")

# Función para actualizar un usuario
def actualizar_usuario(id_usuario, nuevo_nombre, nuevo_email, nueva_edad, nueva_direccion):
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE base_usuarios SET nombre = ?, email = ?, edad = ?, direccion = ? WHERE id = ?", 
        (nuevo_nombre, nuevo_email, nueva_edad, nueva_direccion, id_usuario))
    conexion.commit()
    conexion.close()
    print('El usuario ha sido actualizado')

# Función para eliminar un usuario
def eliminar_usuario(id_usuario):
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM base_usuarios WHERE id=?", (id_usuario,))
    conexion.commit()
    conexion.close()
    print("El usuario ha sido eliminado")

# Menú para interactuar con el programa
def menu():
    while True:
        print("\n--- MENÚ DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del usuario: ")
            email = input("Ingresa el correo electrónico: ")
            edad = int(input("Ingresa la edad del usuario: "))
            direccion = input("Ingresa la dirección del usuario: ")
            crear_usuario(nombre, email, edad, direccion)
        elif opcion == "2":
            leer_usuario()
        elif opcion == "3":
            try:
                id_usuario = int(input("ID del usuario a actualizar: "))
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_email = input("Nuevo correo electrónico: ")
                nueva_edad = int(input("Nueva edad: "))
                nueva_direccion = input("Nueva dirección: ")
                actualizar_usuario(id_usuario, nuevo_nombre, nuevo_email, nueva_edad, nueva_direccion)
            except ValueError:
                print("ID inválido o edad no válida. Debe ser un número.")
        elif opcion == "4":
            try:
                id_usuario = int(input("ID del usuario a eliminar: "))
                eliminar_usuario(id_usuario)
            except ValueError:
                print("ID inválido. Debe ser un número.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
