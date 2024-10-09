

class Book:
    
    #constructor to initialize the book instance
    def __init__(self, title, author, year):
        self.titel = title
        self.author = author
        self.year = year


    #constructor to print a message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.titel}")


    #string repersentation : used by print() or str()
    def __str__(self):
        return f"{self.titel} by {self.author}, published in {self.year}"


    #official repersentation : used by repr() or for debugging
    def __repr__(self):
        return f"Book('{self.titel}', {self.author}, {self.year})"
    