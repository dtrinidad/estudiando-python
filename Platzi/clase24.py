#!/bin/python
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El Libro {self.title} ha sido prestaod.")
        else:
            print(f"El libro {self.title} no esta disponible.")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")

class user:
    def __init__(self, name, user_id):
        self.name = name
        self.use_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book.title)
        else:
            print(f"El libro {book.title} no esta disponible")
         
    def return_book(self,book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
        else:
            print(f"El libro {book.title} no esta en la lista de prestados.")

class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado.")

    def show_available(self):
        print("Libros disponibles: ")
        for i in self.books:
            if i.available:
                print(f"- {i.title} por {i.author}")

#Crear Libros
book1 = book("El Principito", "Antoine de Saint-Exupery")
book2 = book("(1984)", "George Orwell")

#Crear Usuario
user1 = user("Diego", "001")

#Crear Biblioteca
Library1 = library()
Library1.add_book(book1)
Library1.add_book(book2)
Library1.register_user(user1)


print("\n\n#Mostrar libros")
Library1.show_available()

#Realizar prestamo
user1.borrow_book(book1)



print("\n\n#Mostrar libros")
Library1.show_available()


#Devolver libro
user1.return_book(book1)
print("\n\n#Mostrar libros")
Library1.show_available()
