# Implement the selection sort algorithm that is sorting in descending order.

def selection_sort(arr: list):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


list1 = [2, 5, 19, 21, 10, 74]
print(selection_sort(list1))

def bubble_sort_descending(arr:list):
    for i in range(len(arr)):
        for j in range(len(arr) -1 -i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
                print(test_list)
    return arr

test_list = [14, 5, 6, 2, 12]
print(test_list)
print(bubble_sort_descending(test_list))



# Insertion Sort

def insertion_sort_descending(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


test_data = [5, 3, 2, 1, 6, 4]
print(test_data)
print(insertion_sort_descending(test_data))




