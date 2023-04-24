
class Phone:

    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    def display(self):
        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))

class SmartPhone(Phone):
    
    def __init__(self):
        super().__init__()
        self.email = ""

    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        super().display()
        print("{}".format(self.email))


def main():
    print("Phone:")
    phone1 = Phone()
    phone1.prompt_number()
    print()
    phone1.display()
    print()
    print("Smart phone:")
    smartph = SmartPhone()
    smartph.prompt()
    print()
    smartph.display()

if __name__ == "__main__":
   main()