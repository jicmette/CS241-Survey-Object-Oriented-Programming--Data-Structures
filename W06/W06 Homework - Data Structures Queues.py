from collections import deque

waiting_list = deque()


class Student:

    
    def __init__(self):
        self.name = ""
        self.course = ""

    def prompt(self):
        self.name = ("Enter name: ")
        self.course = ("Enter course: ")

    def display(self):
        print("Now helping {} with {}".format(self.name, self.course))

class HelpSystem(Student):
    

    def __init__(self):
        super().__init__()
        
    def is_student_waiting(self):
        if len(waiting_list) < 1:
            return True
        
        elif len(waiting_list) == 0:
            return False
      
    def add_to_waiting_list(Student):
        super().prompt()
        waiting_list.append(st)
        

    def help_next_student(self):
        if len(waiting_list) == 0:
            print("No one to help.")
        elif len(waiting_list) > 1:
            waiting_list.popleft()
            print()
            super().display()
            
def main():
    helpstudent = HelpSystem()
    sel_user = 0

    while sel_user != 3:
        print()
        print("Options:")
        print("1. Add a new student")
        print("2. Help next student")
        print("3. Quit")
        sel_user = int(input("Enter selection: "))
        print()

        if sel_user == 1:
            helpstudent.add_to_waiting_list()
        
        elif sel_user == 2:
            helpstudent.help_next_student()

        elif sel_user == 3:
            print("Goodbye")   

if __name__ == "__main__":
   main()