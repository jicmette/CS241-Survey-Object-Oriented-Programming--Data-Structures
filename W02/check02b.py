def user_file():
    ufile = input("Enter file: ")
    return ufile

def count_words(ufile):
    r_file = open(ufile, "r")
    data = r_file.read()
    numWords = data.split()
    numLines = data.splitlines()
    return numLines, numWords
    
def main():
    ufile = user_file()
    (numLines, numWords) = count_words(ufile)
    print("The file contains {} lines and {} words.".format(len(numLines), len(numWords)))

if __name__ == "__main__":
    main()