from libro import Libro, LibroDigital
from usuario import Usuario
from biblioteca import Biblioteca
import re
 
PATRON_TEXTO  = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$")
PATRON_NUMERO = re.compile(r"^\d+$")
 
 
def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.lower() == "exit":
            return "exit"
        if not valor:
            print("Error: este campo no puede estar vacio. Intenta de nuevo.")
            continue
        if valor.isnumeric():
            print("Error: este campo no acepta numeros. Ingresa texto.")
            continue
        if not PATRON_TEXTO.match(valor):
            print("Error: no se permiten caracteres especiales ni numeros.")
            print("       Solo se aceptan letras y espacios.")
            continue
        return valor
 
 
def pedir_numero_entero(mensaje, minimo=1, maximo=None):
    while True:
        valor = input(mensaje).strip()
        if valor.lower() == "exit":
            return None
        if not valor:
            print("Error: este campo no puede estar vacio. Ingresa un numero.")
            continue
        if not PATRON_NUMERO.match(valor):
            print("Error: solo se aceptan digitos (0-9). No uses letras ni simbolos.")
            continue
        numero = int(valor)
        if numero < minimo:
            print(f"Error: el numero debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f"Error: el numero debe ser menor o igual a {maximo}.")
            continue
        return numero
 
 
def pedir_formato(mensaje):
    formatos_validos = {"pdf", "epub"}
    while True:
        valor = input(mensaje).strip()
        if valor.lower() == "exit":
            return None
        if valor == "":
            return "PDF"
        if valor.isnumeric():
            print("Error: el formato no puede ser un numero. Escribe PDF o EPUB.")
            continue
        if valor.lower() not in formatos_validos:
            print("Error: formato no valido. Solo se acepta PDF o EPUB.")
            continue
        return valor.upper()
 
 
def pedir_opcion_menu():
    while True:
        valor = input("\nOpcion: ").strip().lower()
        if valor == "exit":
            return "exit"
        if not valor:
            print("Error: debes ingresar una opcion. Elige un numero del 1 al 7.")
            continue
        if not valor.isnumeric():
            print("Error: la opcion debe ser un numero, no texto. Elige del 1 al 7.")
            continue
        if int(valor) < 1 or int(valor) > 7:
            print("Error: opcion fuera de rango. Elige un numero entre 1 y 7.")
            continue
        return valor
 
 
biblio   = Biblioteca()
usuarios = {}
 
print("=== Sistema de Biblioteca ===")
print("Escribe 'exit' en cualquier campo para cancelar.\n")
 
while True:
    print("\nQue deseas hacer?")
    print("  1. Agregar libro fisico")
    print("  2. Agregar libro digital")
    print("  3. Registrar usuario")
    print("  4. Pedir libro")
    print("  5. Devolver libro")
    print("  6. Mostrar catalogo")
    print("  7. Ver prestamos de un usuario")
    print("  exit. Salir")
 
    opcion = pedir_opcion_menu()
 
    if opcion == "exit":
        print("Saliendo del sistema. Hasta luego.")
        break
 
    elif opcion == "1":
        titulo = pedir_texto("Titulo del libro (solo texto): ")
        if titulo == "exit":
            continue
        autor = pedir_texto("Autor (solo texto): ")
        if autor == "exit":
            continue
        biblio.agregar_libro(Libro(titulo, autor))
        print(f"Libro fisico '{titulo}' agregado.")
 
    elif opcion == "2":
        titulo = pedir_texto("Titulo del libro (solo texto): ")
        if titulo == "exit":
            continue
        autor = pedir_texto("Autor (solo texto): ")
        if autor == "exit":
            continue
        fmt = pedir_formato("Formato (PDF/EPUB) [Enter = PDF]: ")
        if fmt is None:
            continue
        biblio.agregar_libro(LibroDigital(titulo, autor, fmt))
        print(f"Libro digital '{titulo}' ({fmt}) agregado.")
 
    elif opcion == "3":
        nombre = pedir_texto("Nombre del usuario (solo texto): ")
        if nombre == "exit":
            continue
        if nombre in usuarios:
            print("El usuario ya existe.")
        else:
            usuarios[nombre] = Usuario(nombre)
            print(f"Usuario '{nombre}' registrado.")
 
    elif opcion == "4":
        biblio.mostrar_libros()
        nombre = pedir_texto("Nombre del usuario (solo texto): ")
        if nombre == "exit":
            continue
        if nombre not in usuarios:
            print("Usuario no encontrado.")
            continue
        titulo = pedir_texto("Titulo del libro a pedir (solo texto): ")
        if titulo == "exit":
            continue
        libro = biblio.buscar_libro(titulo)
        if libro:
            usuarios[nombre].pedir_libro(libro)
        else:
            print("Libro no encontrado.")
 
    elif opcion == "5":
        nombre = pedir_texto("Nombre del usuario (solo texto): ")
        if nombre == "exit":
            continue
        if nombre not in usuarios:
            print("Usuario no encontrado.")
            continue
        usuario = usuarios[nombre]
        usuario.mostrar_prestamos()
        if not usuario.libros_prestados:
            continue
        titulo = pedir_texto("Titulo del libro a devolver (solo texto): ")
        if titulo == "exit":
            continue
        libro = biblio.buscar_libro(titulo)
        if libro:
            usuario.devolver_libro(libro)
        else:
            print("Libro no encontrado.")
 
    elif opcion == "6":
        biblio.mostrar_libros()
 
    elif opcion == "7":
        nombre = pedir_texto("Nombre del usuario (solo texto): ")
        if nombre == "exit":
            continue
        if nombre not in usuarios:
            print("Usuario no encontrado.")
        else:
            usuarios[nombre].mostrar_prestamos()