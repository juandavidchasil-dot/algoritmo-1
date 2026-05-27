
from libro import Libro
class Biblioteca:
    """Gestiona el catálogo de libros disponibles."""

    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        """Agrega un objeto Libro (o subclase) al catálogo."""
        self.libros.append(libro)

    def mostrar_libros(self):
        """Muestra todos los libros y su estado.
        Usa polimorfismo al llamar libro.descripcion() y esta_disponible()."""
        if not self.libros:
            print("  No hay libros en la biblioteca.")
            return
        print("\n  Catálogo de la biblioteca:")
        for i, libro in enumerate(self.libros, 1):
            estado = "Disponible" if libro.esta_disponible() else "Prestado"
            print(f"    {i}. {libro.descripcion()} — {estado}")

    def buscar_libro(self, titulo):
        """Busca un libro por título (sin distinguir mayúsculas)."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
