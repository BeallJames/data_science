def main():

    test_array_unsorted = [1, 0, 2, 3, -3, 3, 250, 4, -1000, 5, 6, 7, 8, 9, -100]

    # find_smallest()
    smallest_index, smallest_value = find_smallest(test_array_unsorted)
    print("\n\n<<<<<<<< Smallest Value:", smallest_value, ">>>>>>>>")
    print("<<<<<<<< At Index:", smallest_index, ">>>>>>>>\n\n\n")

    # slection_sort()
    sorted_list = selection_sort(test_array_unsorted)
    print("\n\n<<<<<<<< Sorted Selection:", sorted_list, " >>>>>>>>\n\n\n")

    # binary_search()
    print("<<<<<<<< At Index: ", binary_search(sorted_list, int(input("Target: "))), " >>>>>>>>\n\n")

    # test_array_unsorted = [1, 0, 2, 3, 3.33, -3, 3, 4, -1000, 5, 6, 7, 8, 9, -100]
    # smallest_index, smallest_value = find_smallest(test_array_unsorted)
    # print("\n\n<<<<<<<< Smallest Index:", smallest_index, ">>>>>>>>")
    # print("<<<<<<<< Smallest Value:", smallest_value, ">>>>>>>>\n\n\n")
    # print("Sorted Selection: ", selection_sort(test_array_unsorted))

    # unsorted_list = (input("Enter a list of numbers: ").split(" "))
    # smallest_index, smallest_value = find_smallest(unsorted_list)
    # print("\n\n<<<<<<<< Smallest Index:", smallest_index, ">>>>>>>>")
    # print("<<<<<<<< Smallest Value:", smallest_value, ">>>>>>>>\n\n\n")
    # print("Sorted Selection: ", selection_sort(unsorted_list))

    #####

def find_smallest(arr):
    smallest = int(arr[0])
    smallest_index = 0
    for i in range(len(arr)):
        # print("index i: ", i)
        # print("value arr[i]: ", int(arr[i]))
        # print("smallest: ", smallest)
        # print("")
        if int(arr[i]) < smallest:
            smallest = int(arr[i])
            smallest_index = i
            # print("smallest: ", smallest)
            # print("smallest_index: ", smallest_index)
            # print("")
        # else:
            # print("smallest: ", smallest)
            # print("smallest_index: ", smallest_index)
            # print()
    # print(smallest_index, smallest)
    return int(smallest_index), int(smallest)

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index, smallest_value = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    # print(new_arr)
    return new_arr

def binary_search(list, target):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2 # // is floor division
        guess = list[mid]

        if guess == target:
            # print("Low is " + str(list[low]) + " at index " + str(low))
            # print("High is " + str(list[high]) + " at index " + str(high))
            # print("Mid is " + str(list[mid]) + " at index " + str(mid))
            print("\n\n\n<<<<<<<< Target:", target, ">>>>>>>>")
            return mid
        elif guess > target:
            # print("Low is " + str(list[low]) + " at index " + str(low))
            # print("High is " + str(list[high]) + " at index " + str(high))
            # print("Mid is " + str(list[mid]) + " at index " + str(mid))
            high = mid - 1 # guess is too high
            # print("Guess is " + str(guess) + " at index " + str(mid) + " and target is " + str(target))
            # print("High is now " + str(high))
        else:
            # print("Low is " + str(list[low]) + " at index " + str(low))
            # print("High is " + str(list[high]) + " at index " + str(high))
            # print("Mid is " + str(list[mid]) + " at index " + str(mid))
            low = mid + 1 # guess is too low
            # print("Guess is " + str(guess) + " at index " + str(mid) + " and target is " + str(target))
            # print("Low is now " + str(low))
    return None # target does not exist

# test_list = [-1,1,3,5,7,9,11,13,15,-100]
# print(binary_search(test_list, int(input("test int "))))

# LIST MUST BE ORDERED


if __name__ == "__main__":
    main()
