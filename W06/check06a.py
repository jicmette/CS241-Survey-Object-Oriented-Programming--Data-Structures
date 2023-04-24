class Book:

    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
      
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    def display_book_info(self):
        print("{} ({}) by {}".format(self.title, self.publication_year, self.author))

class TextBook(Book):

    def __init__(self):
        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print("Subject: {}".format(self.subject))

class PictureBook(Book):

    def __init__(self):
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print("Illustrated by {}".format(self.illustrator))

def main():
    book2 = Book()
    book2.prompt_book_info()
    print()
    book2.display_book_info()
    print()
    text2 = TextBook()
    text2.prompt_book_info()
    text2.prompt_subject()
    print()
    text2.display_book_info()
    text2.display_subject()
    print()
    picture2 = PictureBook()
    picture2.prompt_book_info()
    picture2.prompt_illustrator()
    print()
    picture2.display_book_info()
    picture2.display_illustrator()

if __name__ == "__main__":
   main()