# import ipdb

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property 
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception
        
    @property 
    def book(self):
        return self._book
    
    @book.setter 
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception
        
    @property 
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception
         
    @property 
    def royalties(self):
        return self._royalties
    
    @royalties.setter 
    def royalties(self, value):
        if isinstance(value, int) or value < 0:
            self._royalties = value
        else:
            raise Exception
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if contract.date == date]


b1 = Book("A Giving Tree")
a1 = Author("Shel Silverstein")
c1 = Contract(a1, b1, "Monday", 20)

b2 = Book("Harry Potter")
a2 = Author("JK Rowling")
c2 = Contract(a2, b2, "Tuesday", 40)

# ipdb.set_trace()