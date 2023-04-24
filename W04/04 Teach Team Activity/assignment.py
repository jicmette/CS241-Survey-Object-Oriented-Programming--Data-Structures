from date import Date

class Assignment:

    def __init__(self):
        self.name = ""
        self.start = Date()
        self.due = Date()
        self.end = Date()

    def prompt_user1(self):
        self.name = input("Name: ")
        print()
        print("Start Date:")
        self.start.prompt_user()
        print()
        print("Due Date:")
        self.due.prompt_user()
        print()
        print("End Date:")
        self.end.prompt_user()

    def display_dates(self):
        print("Assignment: {}".format(self.name))
        print("Start Date:")
        self.start.display()
        print("Due Date:")
        self.due.display()
        print("End Date:")
        self.end.display()


