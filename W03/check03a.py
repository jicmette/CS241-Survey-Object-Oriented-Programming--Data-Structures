class Student:

    def __init__(self):
        self.first_Name = ""
        self.last_Name = ""
        self.id = 0

def prompt_user():
    new_student = Student()
    new_student.first_Name = input("Please enter your first name: ")
    new_student.last_Name = input("Please enter your last name: ")
    new_student.id = int(input("Please enter your id number: "))
    return new_student

def display_student(studinfo):
    print("{} - {} {}".format(studinfo.id, studinfo.first_Name, studinfo.last_Name))

def main():
    actStudent = prompt_user()
    print()
    print("Your information:")
    display_student(actStudent)

if __name__ == "__main__":
   main()