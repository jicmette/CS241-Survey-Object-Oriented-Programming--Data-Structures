class Date:

    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2010

    def prompt_user(self):
        self.day = int(input("Day: "))
        self.month = int(input("Month: "))
        self.year = int(input("Year: "))

    def display(self):
        print("{}/{}/{}".format(self.day, self.month, self.year))

