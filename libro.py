# libro.py — Clase base con encapsulamiento

class Libro:
    """Clase base que representa un libro genérico."""

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__disponible = True 
    def prestar(self):
        """Marca el libro como prestado. Retorna True si tuvo éxito."""
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        """Marca el libro como disponible nuevamente."""
        self.__disponible = True

    def esta_disponible(self):
        """Retorna True si el libro está disponible."""
        return self.__disponible

    def descripcion(self):
        """Polimorfismo: cada subclase puede sobrescribir este método."""
        return f"[Libro] '{self.titulo}' — {self.autor}"
class LibroDigital(Libro):
    """Hereda de Libro. Representa un e-book; nunca se queda 'sin stock'."""

    def __init__(self, titulo, autor, formato="PDF"):
        super().__init__(titulo, autor)   # Llama al constructor del padre
        self.formato = formato

    def prestar(self):
        """Polimorfismo: un libro digital siempre se puede prestar."""
        return True 
    def devolver(self):
        """Polimorfismo: devolver un digital no hace nada especial."""
        pass

    def descripcion(self):
        """Polimorfismo: descripción específica para libros digitales."""
        return f"[Digital/{self.formato}] '{self.titulo}' — {self.autor}"

