class Library:
    def __init__(self):
      self.noBooks = 0
      self.books = []
      
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
        
    def Details(self):
      print(f"The no of books available are {self.noBooks}. The books are as follows")
      for book in self.books:
        print(book + ".")
        
k1 = Library() #Object k1
k1.addBook("Harry Potter")
k1.addBook("Rich Dad Poor Dad")
k1.addBook("Think and Grow Rich")
k1.addBook("Atomic Habbits")
k1.Details()

print(k1.books)


