class Book:
    def __init__(self,isbn,title,author,pub_year,book_status = None):
        self.isbn = isbn
        self.title = title
        self.author= author
        self.pub_year = pub_year

        if (book_status==None): #similar to; if book_status is None:
            book_status = []  
        self.book_status = book_status

        #method to add list of book statuses
    def add_book_status(self, book_status):
        self.book_status.append(book_status)
        return self.book_status
        #this is how to make the above variables printable
    def __str__(self):
        return f'Book({self.isbn},{self.title},{self.author},{self.pub_year},{self.book_status})'
list_book_status = ['Onsale','Published','Authored']        
#instatiating a class i.e creating objects | equivalent to insert statement in Databases
book1 = Book(1,'Zora','Lara',2021)
book2 = Book(2,'Bell','Labs',1960,list_book_status)
print(book1)
print(book2)

       