def find_smallest(arr):
    smallest = int(arr[0])
    smallest_index = 0
    for i in range(len(arr)):
        print("index i: ", i)
        print("value arr[i]: ", int(arr[i]))
        # print("smallest: ", smallest)
        # print("")
        if int(arr[i]) < smallest:
            smallest = int(arr[i])
            smallest_index = i
            print("smallest: ", smallest)
            print("smallest_index: ", smallest_index)
            print("")
        else:
            print("smallest: ", smallest)
            print("smallest_index: ", smallest_index)
            print("")
    return int(smallest_index), int(smallest)

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index, smallest_value = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr



test_array_unsorted = [1, 0, 2, 3, 3.33, -3, 3, 4, -1000, 5, 6, 7, 8, 9, -100]
smallest_index, smallest_value = find_smallest(test_array_unsorted)
print("\n\n<<<<<<<< Smallest Index:", smallest_index, ">>>>>>>>")
print("<<<<<<<< Smallest Value:", smallest_value, ">>>>>>>>\n\n\n")
print("Sorted Selection: ", selection_sort(test_array_unsorted))

# unsorted_list = (input("Enter a list of numbers: ").split(" "))
# smallest_index, smallest_value = find_smallest(unsorted_list)
# print("\n\n<<<<<<<< Smallest Index:", smallest_index, ">>>>>>>>")
# print("<<<<<<<< Smallest Value:", smallest_value, ">>>>>>>>\n\n\n")
# print("Sorted Selection: ", selection_sort(unsorted_list))
