class Book:
    def __init__(self,title, genre, author, code):
        self.title= title
        self.genre=genre
        self.author=author
        self.code= code

    def __str__(self):
        return f"Book{self.title} in{self.genre} genre, by {self.author}"

class Library:
    def __init__(self):
        self.books=[]

    def add(self, book):
        self.books.append(book)
        print(f"{book.title} was added")

    def remove(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f" book {book.title} was removed")  
                return
        print(f"{title} not found")


    def search(self, title):
        title= title.strip()
        founds=[]
        for book in self.books:
            if title in book.title:
                founds.append(book)
        
        if founds:
            print("found books in this title: ")
            for book in founds:
                print(book)

        else:
            print("not found")
    
    def display(self):
        if self.books:
            print("available books: ")
            for book in self.books:
                print(book)
        else:
            print("the library is empty")

        

library=Library()

book1=Book(" looking for Alaska", "Drama","John Green","12")
book2=Book(" the Heckory","adventure","Agata","13")
book3=Book(" animal farm","Drama","George Orwell","14")
book4=Book(" the last day of...","pragmatic","Victor Hugo","15")

library.add(book1)
library.add(book2)
library.add(book3)
library.add(book4)

library.search("mom")

library.display()