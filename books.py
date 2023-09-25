"""
Crea una aplicación para llevar un registro de libros utilizando clases en Python.
La aplicación debe permitir agregar libros, buscar libros por título y mostrar la lista de libros.
"""
from pprint import  pprint

class Books:
    def __init__(self):
        self.books = []

    def add_book(self, id, title, author):
        book = {
            "id": id,
            "title": title,
            "author": author
        }
        self.books.append(book)

    def list_books(self):
        return self.books

    def search_book_by_title(self, search):
        results = []
        for book in self.books:
            if search.lower() in book["title"].lower() or search.lower() in book["author"].lower():
                results.append(book)
        return results

books = Books()

books.add_book(1, 'EL imperio final', "Brandon sanderson")
books.add_book(1, 'Harry Potter', "J.K Rowlin")
books.add_book(1, 'Pozo de la asension', "Brandon Sanderson")

pprint(books.list_books())
print("-----------")
pprint(books.search_book_by_title("sanderson"))