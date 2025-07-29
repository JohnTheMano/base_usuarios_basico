import sqlite3

conexion = sqlite3.connect("base_usuarios.db")
cursor = conexion.cursor()

cursor.execute("""
create table if not exists base_usuarios(
    id integer primary key autoincrement,
    nombre text not null
    )""")
conexion.commit()
conexion.close()

def crear_usuario(nombre):
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO base_usuarios (nombre) VALUES (?)", (nombre,))
    conexion.commit()
    conexion.close()
    print("Usuario creado con éxito")

def leer_usuario(nombre):
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM base_usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    if usuarios:
        print("Usuarios encontrados:")
        for usuario in usuarios:
            print(f'ID = {usuario[0]} - Nombre = {usuario[1]}')
    else:
        print("No se encontró ningún usuario con ese nombre.")

def actualizar_usuario(id_usuario,nuevo_nombre):
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE base_usuarios SET nombre = ? WHERE id = ?", (nuevo_nombre, id_usuario))
    conexion.commit()
    conexion.close()
    print('El usuario ha sido actualizado')

def eliminar_usuario(id_usuario):
    conexion = sqlite3.connect("base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM base_usuarios WHERE id=?",(id_usuario,))
    conexion.commit()
    conexion.close()
    print("El usuario ha sido eliminado")


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
            crear_usuario(nombre)
        elif opcion == "2":
            leer_usuario(None)  # O puedes modificar la función si quieres buscar por nombre
        elif opcion == "3":
            try:
                id_usuario = int(input("ID del usuario a actualizar: "))
                nuevo_nombre = input("Nuevo nombre: ")
                actualizar_usuario(id_usuario, nuevo_nombre)
            except ValueError:
                print("ID inválido. Debe ser un número.")
        elif opcion == "4":
            try:
                id_usuario = int(input("ID del usuario a eliminar: "))
                eliminar_usuario(id_usuario)
            except ValueError:
                print("ID inválido. Debe ser un número.")
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
