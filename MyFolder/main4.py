#reader should able to search specific book in library
#reader should borrow the book from library
#reader should return the book to the library
#library should get stat of the book - book name, quantity of book

#librarian should make the purchase of the book, and 

class Library:

    def __init__(self):
        self.books = []

    def add(self, book_name):
        self.books.append(book_name)

    def search(self, book_name):
        if self.books != []:
            if book_name in self.books:
                return book_name
            return ""
        return ""
    
    def pop(self, book_name):
        self.books.remove[book_name]


    def count(self):
        for i, c in enumerate(self.books):
            
            
        
class Reader:

    def __init__(self):
        self.library = Library()

    def search(self, book_name):
        book = self.library.search(book_name)
        if book:
            print(f"boo found: {book_name}")
        else:
            print("There is no book available in library")

    def borrow(self, book_name):
        pass

    def return_book(self, book_name):
        pass



