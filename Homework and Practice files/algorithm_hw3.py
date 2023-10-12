# Task 1. Two Lowest Elements

def find_two_lowest(arr: list):
    list1.sort()
    return [list1[0], list1[1]]


list1 = [10, 21, 3, 4, 5]
print(find_two_lowest(list1))

# Given a list of numbers, return the inverse of each. Each positive becomes a negative, and the negatives become positives.

def invert_list(arr: list):
    for i in range(len(list2)):
        list2[i] = -list2[i]
    return list2


list2 = [1, 2, 3, 4, 5]
print(invert_list(list2))


# Task 3
# Implement a function that returns the difference between the largest and the smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.

def max_diff(arr: list):
    list3.sort()
    return list3[-1] - list3[0]


list3 = [1, 2, 3, 4, 5]
print(max_diff(list3))

# Task 4
# Write a function that counts the number of elements in a given list larger than their adjacent neighbors.
def count_larger_neighbors(arr: list):
    count = 0
    for i in range(1, len(list4) - 1):
        if list4[i] > list4[i -1] and list4[i] > list4[i +1]:
            count += 1
    return count


list4 = [2, 56, 7, 21, 22, 19, 26]
print(count_larger_neighbors(list4))


# Task 5
def subtract_min(arr: list):
# Find the minimum element in the list using the 'min' function and store it in 'min_element'.
    min_element = min(list5)

    for i in range(len(list5)):
        list5[i] = arr[i] - min_element
    return list5


list5 = [9, 2, 5, 4, 7, 6, 1]
print(subtract_min(list5))