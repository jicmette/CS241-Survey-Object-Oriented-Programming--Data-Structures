def prompt_filename():
    the_file = input("Enter a file: ")
    print("Opening file {}".format(the_file))
    return the_file

def parse_file(the_file):
    count = 0
    with open(the_file) as rfile:
        for line in rfile:
            words = line.split()
            for word in words:
                if word.lower() == "pride":
                    count += 1
    return count
       
def main():
    the_file = prompt_filename()
    count = parse_file(the_file)
    print("The word pride ocurrs {} times in this file.".format(count))

if __name__ == "__main__":
    main()