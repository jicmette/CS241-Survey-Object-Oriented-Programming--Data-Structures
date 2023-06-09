class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)

def get_inverse(n):
    n_float = float(n) 

    if n_float < 0:
        raise NegativeNumberError("Error: The value cannot be negative")

    return 1 / n_float

def main():

    n = input("Enter a number: ")
    try:
        result = get_inverse(n)
        print("The result is: {}".format(result))

    except ValueError:
        print("Error: The value must be a number")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        
    except NegativeNumberError as e:
        print(e)

if __name__ == "__main__":
    main()
