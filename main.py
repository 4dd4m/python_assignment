from operator import attrgetter
import numpy as np
import matplotlib.pyplot as plt

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
        #Representation of a single book
        return "{0:9}|{1:14}|{2:32}|{3:2}|{4:14}|{5:5}|{6:2}|".format(
                self.genre, self.author, self.title, self.coverType,
                self.publisher, self.cost, self.stock)


class Store:
    #Store object, store books, and manipulates them
    def __init__(self):
        self._books = []
        self._totalBooks = 0
        self._totalValue = 0.00
        self._avgPrice = 0.00
        self._genresInStore = {}
        self.importBooks()

    def importBooks(self, filename='books.txt', filterOut=['#','\n']):
        #Open the file, iterate, calls self.addBook()
        try:
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
            self._setTotalNumOfBooks()
            #Update the Store's total value
            self._setTotalValueOfBooks()
            self._setAveragePriceOfBooks()
        except FileNotFoundError:
            print('{0} not found, cannot import'.format(filename))
        except Exception as e:
            print('Ohhh, no: '+e+' Import aborted')

    def addBook(self, Book):
        #Adds a book into the store Either from cl4ss or manual
        self._books.append(Book)
        if Book.genre not in self._genresInStore:
            self._genresInStore[Book.genre] = 1
        else:
            self._genresInStore[Book.genre] += 1
        self._books.sort( key = attrgetter('title'), reverse=False)

    def userAddBook(self):
        #Task 5
        #Interface to the user to Add a book
        print("------------")
        print("Add a Book: ")
        print("------------")
        genre = input("Genre: ")
        author = input("Author: ")
        title = input("Title: ")
        formatType = input("Format [hb-sb]: ")
        publisher = input("Publisher: ")
        cost = float(input("Price: "))
        stock = int(input("stock: "))
        confirm = input("Save Data? [y-n]")

        if confirm == "y" or confirm == "Y":
            oldAverage = self._avgPrice
            book = Book([author, title, formatType,
                        publisher, cost, stock, genre])
            print("---------------------------------")
            print("The Following book has been added")
            print("---------------------------------")
            print(book)
            self.addBook(book)
            #Update the total number of books
            self._setTotalNumOfBooks()
            #Update the Store's total value
            self._setTotalValueOfBooks()
            self._setAveragePriceOfBooks()
            print("Total title now: {0}, AvgPrice changed by: £{1}".format(
                        self._totalBooks, round(self._avgPrice - oldAverage,2)))

    def _setTotalNumOfBooks(self):
        #Count all books in the store
        bookCount = 0
        for book in self._books:
            if book.stock > 0:
                 bookCount += book.stock
        self._totalBooks = bookCount

    def getTotalNumOfBooks(self):
        #Returns with the total number of books
        return self._totalBooks

    def _setTotalValueOfBooks(self):
        #Iterate through self.books and sets their value to self.totalValue
        tempTotal = 0
        for book in self._books:
            #Only if the stock is > 0
            if book.stock > 0:
                titleValue = book.cost * book.stock
                tempTotal += titleValue
        self._totalValue = round(tempTotal,2)

    def getTotalValueOfBooks(self):
        #Get the total value of the books
        return round(self._totalValue,2)

    def _setAveragePriceOfBooks(self):
        #Makes and sets an average price
        average =  self._totalValue / self._totalBooks
        self._avgPrice = round(average,2)

    def getAveragePriceOfBooks(self):
        #Task 2
        #Returns an average price of the books
        print("-----------------------------------")
        print("The average price in Stock: £",self._avgPrice)
        print("-----------------------------------")

    def searchForTitle(self,title, orderBy='title'):
        #Task 5
        #Print out he book for the given title
        listOfBooks = []
        for book in self._books:
            if title in book.title:
                #if the title matches, append
                listOfBooks.append(book)
        if len(listOfBooks) > 0:
            #sort the listOfBooks[] based on book.title
            listOfBooks.sort(key = attrgetter(orderBy), reverse = False)
            counter = 1
            for i in listOfBooks:
                #Assign an id to modify
                #Render the booklist
                print("Id-> {0}. ".format(counter),i)
                counter += 1
            user = int(input("Enter ID to modify: ")) -1
            try:
                if listOfBooks[user]:
                    #confirmation on selected book
                    print("-------------")
                    print("Selected Book")
                    print("-------------")
                    print(listOfBooks[user])
                    print("-------------")
                    #Okay, we have a valid book, pass it to modifyStock()
                    self.modifyStock(listOfBooks[user])
            except IndexError:
                    #The Black Knight always triumphs! Have at you! Come on then.
                    print("Invalid Id...")
                    return False
        else:
            print('No Match')

    def searchForGenre(self, genre="All", orderBy='title'):
        #Task 3
        #list out all the books of a specific genre
        print('--------------------------')
        print('Books for genre: ' + genre)
        print('--------------------------')
        if genre != "All":
            if genre not in self._genresInStore:
                #None shall pass
                print("Invalid Genre")
            else:
                listOfBooks = []
                for book in self._books:
                    if book.genre == genre:
                        listOfBooks.append(book)
                listOfBooks.sort(key = attrgetter(orderBy), reverse = False)
                for i in listOfBooks:
                    print(i)
        else:
            for genre in self._genresInStore:
                print("Genre: {0} Total Books: {1}".format(
                                    genre.title(),self._genresInStore[genre]))

    def listOfBooks(self, books=[], orderBy='title', totals=False):
        #Task 1,6
        #Listing out books by title, optional totals x3
        print('--------------------')
        print('List Of Books stored')
        print('--------------------')
        if len(books) == 0:
            books = self._books
        books.sort(key=attrgetter(orderBy), reverse=False)
        for i in books:
            print(i)
        if totals:
           print("-------------------------------------")
           print("Total books: {0}. Total value: £{1}"
           .format(self._totalBooks, round(self._totalValue,2)))

    def modifyStock(self, Book):
        #Modify the stock of the passed Book
        stock = int(input("Change [+Increase -Decrease]: "))
        if (stock + Book.stock) < 0:
            #OutOfStockPrintMessage
            print("This book is not available anymore.")
            Book.stock = 0  #no negative numbers
        else:
            #if some book still left, just update stock
            newStock = Book.stock + stock
            Book.stock = newStock
            print("The New Stock is: {0}".format(newStock))
        #Update Store Values
        self._setTotalNumOfBooks()
        self._setTotalValueOfBooks()
        self._setAveragePriceOfBooks()

    def diagram(self):
        #Task 7
        plt.rcdefaults()
        #axis label and values
        #[int,int,int]
        numOfBooksPerGenre = []
        #[str,str,str]
        genreLables = []
        for genre in self._genresInStore:
            numOfBooksPerGenre.append(self._genresInStore[genre])
            genreLables.append(genre)
        y_pos = np.arange(len(genreLables))
        #Build & show the chart
        plt.bar(y_pos, numOfBooksPerGenre, align='center', alpha=0.5)
        plt.xticks(y_pos, genreLables)
        plt.ylabel('Number of Books')
        plt.title('Title Breakdown by Genre')
        plt.show()

def mainMenu():
    #represent main menu
    print("-------------")
    print("BookStore API")
    print("-------------")
    print("1. List of books\n2. Average Price/Title\n3. NumOfBooks/Genre")
    print("4. Add a book\n5. Modify Stock\n6. Ordered List by Title")
    print("7. Diagram representation\n8. Exit")
    print("-------------------------")

if __name__ == "__main__":
    try:
        #instantiate
        store = Store()
        #render main menu
        mainMenu()
        #user input
        user = ""
        while user != "8" or user != 'q':
        #if user doesnt input 8 or q just keep rendering
            user = input("Operation [1-8]?: ")
            if user == "1":
                store.listOfBooks(totals=True)
                mainMenu()
            elif user == "2":
                store.getAveragePriceOfBooks()
                mainMenu()
            elif user == "3":
                store.searchForGenre()
                mainMenu()
            elif user == "4":
                store.userAddBook()
                mainMenu()
            elif user == "5":
                query = input("Searching for books: ")
                store.searchForTitle(query)
                mainMenu()
            elif user == "6":
                store.listOfBooks([],'title')
                mainMenu()
            elif user == "7":
                store.diagram()
                mainMenu()
            elif user == "8":
                break;
            else:
                mainMenu()
        print("Bye")
    except KeyboardInterrupt:
        print('Bye')
