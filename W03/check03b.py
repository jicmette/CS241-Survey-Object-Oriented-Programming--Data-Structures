class Complex: 

    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def prompt_user(self):
        self.real = int(input("Please enter the real part: "))
        self.imaginary = int(input("Please enter the imaginary part: "))
                  
    def displaynumbers(self):
        print("{} + {}i".format(self.real, self.imaginary))    
        
def main():
    complex1 = Complex()
    complex2 = Complex()
    print("The values are:")
    complex1.displaynumbers()
    complex2.displaynumbers()
    print()
    complex1.prompt_user()
    print()
    complex2.prompt_user()
    print()
    print("The values are:")
    complex1.displaynumbers()
    complex2.displaynumbers()

if __name__ == "__main__":
   main()