class evenodds:

    def __init__(self):
        self.even_Numbers = []
        self.odd_Numbers = []

    def prompt_user(self):
        user_input = 1

        while user_input != 0:
            for n in range(1):
                user_input = int(input("Enter a number (0 to quit): "))
            
                if (user_input % 2) == 0:
                    self.even_Numbers.append(user_input)
                
                elif (user_input % 2) == 1:
                    self.odd_Numbers.append(user_input)                   
                                       
    def display_even(self):
        for even in self.even_Numbers:
            print(even)

    def display_odd(self):
        for odd in self.odd_Numbers:
            print(odd) 

def main():
    numbers = evenodds()
    numbers.prompt_user()
    print("Even numbers: ")
    numbers.display_even()
    print()
    print("Odd numbers: ")
    numbers.display_odd()
    
if __name__ == "__main__":
    main()