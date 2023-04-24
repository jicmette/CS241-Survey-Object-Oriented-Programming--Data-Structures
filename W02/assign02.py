#Asks the user to enter a file.
def user_file():
    file_in = input("Please enter the data file: ")
    return file_in

#Read the file and search for the highest and lowest rate.
def read_file(file_in):
    with open(file_in, "r") as file:
        average = 0.0
        low_com = 50000
        max_com = 0.0
        total = 0
        lineMax = ""
        lineMin = ""
        
#Search inside every line the common rate.      
        for line in file:
            if total > 0:
                comm_rate = float(line.split(",")[6])
                average += comm_rate
                if (low_com > comm_rate):
                    low_com = comm_rate
                    lineMin = line
                if (max_com < comm_rate):
                    max_com = comm_rate
                    lineMax = line
            total += 1
            return 0.0, "Bad", "Bad", "", ""
        average = average / float(total-1)
        file.close()
        return average, low_com, max_com, lineMin, lineMax

#Displays the results to the user.          
def display(utility_name,zip,state,comm_rate):
    print("{} ({}, {}) - ${}".format(utility_name, zip, state, comm_rate))

#It calls every functions.
def main():
    file_in = user_file()
    print()
    average, low_com, max_com, lineMin, lineMax = read_file(file_in)
    print("The average commercial rate is: {}".format(average))
    print()
    print("The highest rate is:")
    lineMaxA = lineMax.split(",")
    display(lineMaxA[2], lineMaxA[0], lineMaxA[3], float(lineMaxA[6]))
    print()
    print("The lowest rate is:")
    lineMinA = lineMin.split(",")
    display(lineMinA[2], lineMinA[0], lineMinA[3], float(lineMinA[6]))

if __name__ == "__main__":
    main()