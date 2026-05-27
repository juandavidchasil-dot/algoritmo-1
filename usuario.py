
from libro import Libro 

class Usuario:
    """Representa un usuario que puede pedir y devolver libros."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = [] 
    def pedir_libro(self, libro):
        """Intenta pedir un libro. Usa polimorfismo: llama libro.prestar()
        sin importar si es Libro, LibroDigital o LibroReferencia."""
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} tomó: {libro.descripcion()}")
        else:
            print(f"'{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        """Devuelve un libro que el usuario tiene prestado."""
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} devolvió: '{libro.titulo}'")
        else:
            print("Este usuario no tiene ese libro.")

    def mostrar_prestamos(self):
        """Lista los libros actualmente en préstamo."""
        if not self.libros_prestados:
            print(f"  {self.nombre} no tiene libros prestados.")
        else:
            print(f"\n  Libros de {self.nombre}:")
            for i, libro in enumerate(self.libros_prestados, 1):
                print(f"    {i}. {libro.descripcion()}")
