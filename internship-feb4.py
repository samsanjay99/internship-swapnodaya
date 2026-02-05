"""Father and Son (Single Inheritance + super())
"""
class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("surname is ", self.surname)

    def display_father_name(self):
        print("The fathername is ", self.father_name)


class son(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)

    def display_name(self):
        print("name is ", self.name)


child_obj=son("john", "K","Rajesh")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_name()

"""Example 2: Books and IssuedBooks
Code
"""

class Books:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display_books_details(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)


class IssuedBooks(Books):
    def __init__(self,title,author,issued_to,issued_date):
        self.issued_to=issued_to
        self.issued_date=issued_date
        super().__init__(title, author)

    def display_issued_books_details(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)
        print("The name of the person issued to is", self.issued_to)
        print("The date of issued is",self.issued_date)


IB=IssuedBooks("Python","John","Students","04-02-26")
IB.display_books_details()
