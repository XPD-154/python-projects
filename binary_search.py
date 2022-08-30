from random import *

#function to implement binary search
def findValue(list_of_numbers, number_to_find):

    #'low' represent the lower index
    low = 0

    #'high' represent the highest index
    high = len(list_of_numbers) - 1

    while low <= high:

        #'middle' represent the index of the middle number
        middle = low + (high - low) // 2

        if list_of_numbers[middle] == number_to_find:
            return middle
        elif list_of_numbers[middle] < number_to_find:
            low = middle + 1
        elif list_of_numbers[middle] > number_to_find:
            high = middle - 1
    return -1

#initialize empty list
ex_list = list()

#initialize the lenght of list
length_of_list = int(input("input the length of list: "))

#add values from computer via randint
while len(ex_list)<length_of_list:
    value = randint(-3*length_of_list, 3*length_of_list)
    ex_list.append(value)
    print(ex_list, len(ex_list))

#sort the list
new_list = sorted(ex_list)

#collect number to find from user
number_to_find = int(input("input the number to find: "))

final = findValue(new_list, number_to_find)

if final == -1:
    print("This item was not found in the list.")
else:
    print(f"The number {number_to_find} was found at index position {final}.")
