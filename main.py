from operator import attrgetter

class Book:
    def __init__(self,bookDetails):
        #A book allowed genre types
        self.availableGenre = ['fiction', 'biography', 'science', 'religion']
        #A single book
        self.author = str(bookDetails[0])
        self.title = str(bookDetails[1])
        self.coverType = str(bookDetails[2])
        self.publisher = str(bookDetails[3])
        self.cost = float(bookDetails[4])
        self.stock = int(bookDetails[5])
        self.genre = str(bookDetails[6])

    def __str__(self):
        #Prints the book details
        return "{0:9}|{1:14}|{2:32}|{3:2}|{4:14}|{5:5}|{6:2}|".format(self.genre, self.author, self.title, self.coverType, self.publisher, self.cost,
        self.stock)

class Store:
    #Store object, store books, and manipulates them
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
        self._books.sort( key = attrgetter('title'), reverse=False)

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
        return round(self._totalValue,2)

    def setAveragePriceOfBooks(self):
        #Makes and sets an average price based on two variable
        average =  self._totalValue / self._totalBooks
        self._avgPrice = round(average,2)

    def searchForTitle(self,title, orderBy='title'):
        #Print out he book for the given title
        listOfBooks = []
        for book in self._books:
            if title in book.title:
                listOfBooks.append(book)
        if len(listOfBooks) > 0:
            listOfBooks.sort(key = attrgetter(orderBy), reverse = False)
            for i in listOfBooks:
                print(i)
        else:
            print('No Match')

    def searchForGenre(self, genre, orderBy='title'):
        #list out all the books of a specific genre
        print('--------------------------')
        print('Books for genre: ' + genre)
        print('--------------------------')
        if genre not in self._genresInStore:
            print("Invalid Genre")
        else:
            listOfBooks = []
            for book in self._books:
                if book.genre == genre:
                    listOfBooks.append(book)
            listOfBooks.sort(key = attrgetter(orderBy), reverse = False)
            for i in listOfBooks:
                print(i)

    def listOfBooks(self, books=[], orderBy='title', totals=False):
        print('--------------------')
        print('List Of Books stored')
        print('--------------------')
        if len(books) == 0:
            books = self._books
        books.sort(key=attrgetter(orderBy), reverse=False)
        for i in books:
            print(i)
        if totals:
           print("----------------------------------------------------")
           print("Total books: {0}. Total value: {1}. Average: {2}".format(self._totalBooks, round(self._totalValue,2), self._avgPrice))


store = Store()
store.importBooks()
store.listOfBooks(totals=True)
