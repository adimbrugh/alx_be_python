

class Book:

    #constructor to initialize the book instance
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    #constructor to print a message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")


    #string repersentation : used by print() or str()
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"


    #official repersentation : used by repr() or for debugging
    def __repr__(self):
        return f"Book('{self.title}', {self.author}, {self.year})"
    