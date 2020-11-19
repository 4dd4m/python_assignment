class Book:
    #def __init__(author,title, coverType, publisher,cost, stock, genre):
    def __init__(self,bookDetails):
        self.availableGenre = ['fiction', 'biography', 'science', 'religion']
        self.author = str(bookDetails[0])
        self.title = str(bookDetails[1])
        self.coverType = str(bookDetails[2])
        self.publisher = str(bookDetails[3])
        self.cost = float(bookDetails[4])
        self.stock = int(bookDetails[5])
        self.genre = str(bookDetails[6])

    def __str__(self):
        return "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(self.author, self.title, self.coverType, self.publisher, self.cost, self.stock, self.genre)

class Store:
    def __init__(self):
        self.books = []
        pass

    def importBooks(self, filename='books.txt', filterOut=['#','\n']):
        with open(filename, 'r') as f:
                for line in f:
                    if line[0] not in filterOut:
                        line = line.rstrip()
                        bookDetails = line.split(',')
                        counter = 0
                        for i in range(len(bookDetails)):
                            bookDetails[counter] = bookDetails[counter].lstrip()
                            bookDetails[counter] = bookDetails[counter].rstrip()
                            counter += 1
                        bookObject = Book(bookDetails)
                        self.addBook(bookObject)
    def addBook(self, Book):
        self.books.append(Book)
        print(Book)
store = Store()
store.importBooks()
