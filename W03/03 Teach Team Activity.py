class RationalNumbers:

    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def prompt_user(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))

    def display(self):
        print("{}/{}".format(self.numerator, self.denominator))

    def display_decimal(self):
        print(self.numerator/self.denominator)

def main():
    num_den = RationalNumbers()
    num_den.display()
    num_den.prompt_user()
    num_den.display()
    num_den.display_decimal()

if __name__ == "__main__":
    main()