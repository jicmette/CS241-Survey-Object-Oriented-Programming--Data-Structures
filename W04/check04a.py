class Person:

    def __init__(self):
        self.name = "anonymous"
        self.birthyear = "unknown"

    def display(self):
        print("{} (b. {})" .format(self.name, self.birthyear))

class Book:

    def __init__(self):
        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"

    def display_book(self):
        print(self.title)
        print("Publisher:")
        print(self.publisher)
        print("Author:")
        self.author.display()

def main():
    bookname = Book()
    bookname.display_book()
    print()
    print("Please enter the following:")
    bookname.author.name = input("Name: ")
    bookname.author.birthyear = input("Year: ")
    bookname.title = input("Title: ")
    bookname.publisher = input("Publisher: ")
    print()
    bookname.display_book()

if __name__ == "__main__":
   main()