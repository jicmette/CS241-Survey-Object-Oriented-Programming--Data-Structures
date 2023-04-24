def prompt_number():
    nm1 = -1 

    while nm1 < 0:
        x = input("Enter a positive number: ")
        nm1 = int(x)

        if nm1 < 0: 
            print("Invalid entry. The number must be positive.")
    print()
    return nm1

def compute_sum(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3)

def main():
    n1 = prompt_number()
    n2 = prompt_number()
    n3 = prompt_number()
    sumtot = compute_sum(n1, n2, n3)
    print("The sum is: {}".format(sumtot))

if __name__ == "__main__":
    main()
