"""
    Crea una clase llamada Libro que tenga los siguientes atributos:

    titulo: El título del libro.
    autor: El autor del libro.
    anio_publicacion: El año de publicación del libro.
    disponible: Un valor booleano que indica si el libro está disponible o no en la biblioteca.
    La clase también debe tener los siguientes métodos:

    prestar_libro(): Este método cambia el estado del libro a no disponible si está disponible. Si el libro ya está prestado, debe imprimir un mensaje indicando que el libro no está disponible.
    devolver_libro(): Este método cambia el estado del libro a disponible si estaba prestado. Si el libro ya estaba disponible, debe imprimir un mensaje indicando que el libro ya está en la biblioteca.
    informacion(): Este método imprime la información del libro (título, autor, año de publicación y disponibilidad).
    Luego, crea algunas instancias de la clase Libro y realiza algunas operaciones de préstamo y devolución.

"""


class Library:
    def __init__(self, title, author, year_published, available):
        self._title = title
        self._author = author
        self._year_published = year_published
        self._available = available


    def lend_book(self):
        if self._available == True:
            self._available = False
            print("Prestamo correcto")
        else:
            print("El libro no esta disponible")

    def return_book(self):
        if self._available == False:
            self._available = True
            print("Libro devuelto")
        else:
            print("El libro no estaba prestado")

    def get_info(self):
        print("Nombre: ", self._title)
        print("Autor: ", self._author)
        print("Año de publicación: ", self._year_published)
        status = "Disponible" if self._available else "No disponible"
        print(f'Estado: {status}')



libro1 = Library("Juego de Tronos", "Desconocido", 2010, True)

libro1.lend_book()
libro1.lend_book()
libro1.return_book()
libro1.get_info()
print("--------------------")
libro1.lend_book()
libro1.get_info()
