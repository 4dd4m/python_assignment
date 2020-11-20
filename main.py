class Book:
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
        self._books = []
        self._totalBooks = 0
        self._totalValue = 0.00
        self._avgPrice = 0.00
        self._genresInStore = {}

    def importBooks(self, filename='books.txt', filterOut=['#','\n']):
        #Open the file
        with open(filename, 'r') as f:
                #For every line in the file
                for line in f:
                    #If line contains commnets or \n, it doesnt count
                    if line[0] not in filterOut:
                        #Strip the whitespaces from the line start and end
                        line = line.rstrip()
                        line = line.lstrip()
                        #Create a list along commas
                        bookDetails = line.split(',')
                        counter = 0
                        #Iterate through the details
                        for i in range(len(bookDetails)):
                            #strip out the whitespace from float ' 10.00'
                            bookDetails[counter] = bookDetails[counter].lstrip()
                            bookDetails[counter] = bookDetails[counter].rstrip()
                            counter += 1
                        #create a book
                        bookObject = Book(bookDetails)
                        #Add them to the store
                        self.addBook(bookObject)
        #Update the total number of books
        self.setTotalNumOfBooks()
        #Update the Store's total value
        self.setTotalValueOfBooks()
        #Update the average price of the books
        self.setAveragePriceOfBooks()

    def addBook(self, Book):
        #Adds a book into the store
        self._books.append(Book)
        if Book.genre not in self._genresInStore:
            self._genresInStore[Book.genre] = 1
        else:
            self._genresInStore[Book.genre] += 1


    def setTotalNumOfBooks(self):
        #Count all books in the store
        if len(self._books) > 0:
            self._totalBooks = len(self._books)

    def getTotalNumOfBooks(self):
        #Returns with the total number of books
        return self._totalValue

    def setTotalValueOfBooks(self):
        #Iterate through self.books and sets their value to self.totalValue
        for book in self._books:
            #Only if the stock is > 0
            if book.stock > 0:
                titleValue = book.cost * book.stock
                self._totalValue += titleValue
        round(self._totalValue,2)

    def getTotalValueOfBooks(self):
        #Get the total value of the books
        return self._totalValue

    def setAveragePriceOfBooks(self):
        #Makes and sets an average price based on two variable
        average =  self._totalValue / self._totalBooks
        self._avgPrice = round(average,2)

    def searchForTitle(self,title):
        for book in self._books:
            if title in book.title:
                return book
            else:
                return "The book isn't found in the store"


store = Store()
store.importBooks()
print(store._totalBooks)
print(store._totalValue)
print(store._avgPrice)
print(store._genresInStore)
print(store.searchForTitle('rew'))
