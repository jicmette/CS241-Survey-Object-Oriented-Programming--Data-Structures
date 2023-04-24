numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]

#Insert a number
numbers.insert(0, 5)
print(numbers)

#Remove an item in the list
numbers.remove(2348)
print(numbers)

#Add a list to a list
newNumbers = [5, 3, 6, 7, 4]
numbers += newNumbers
print(numbers)

#Sort the items in the list
numbers.sort()
print(numbers)

#Print backward a list
numbers.sort(reverse = True)
print(numbers)

#Print the times that a item is in the list
print(numbers.count(12))

#Shows the index in the list
print(numbers.index(96))

#Divide the list in two
middle = len(numbers) // 2
middle1 = numbers[:middle]
middle2 = numbers[middle:]
print(middle1)
print(middle2)

#Skips the amount of numbers selected
skipped_list = numbers[::3]
print(skipped_list)

#It prints the last numbers of the list
last_five_numbers = numbers[-5:]
print(last_five_numbers)
