def binary_search(list, target):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2 # // is floor division
        guess = list[mid]

        if guess == target:
            print("Low is " + str(list[low]) + " at index " + str(low))
            print("High is " + str(list[high]) + " at index " + str(high))
            print("Mid is " + str(list[mid]) + " at index " + str(mid))
            print("Target", target, "found at index", str(mid))
            return mid
        elif guess > target:
            print("Low is " + str(list[low]) + " at index " + str(low))
            print("High is " + str(list[high]) + " at index " + str(high))
            print("Mid is " + str(list[mid]) + " at index " + str(mid))
            high = mid - 1 # guess is too high
            print("Guess is " + str(guess) + " at index " + str(mid) + " and target is " + str(target))
            print("High is now " + str(high))
        else:
            print("Low is " + str(list[low]) + " at index " + str(low))
            print("High is " + str(list[high]) + " at index " + str(high))
            print("Mid is " + str(list[mid]) + " at index " + str(mid))
            low = mid + 1 # guess is too low
            print("Guess is " + str(guess) + " at index " + str(mid) + " and target is " + str(target))
            print("Low is now " + str(low))
    return None # target does not exist    

test_list = [-1,1,3,5,7,9,11,13,15,-100]
print(binary_search(test_list, int(input("test int "))))

# LIST MUST BE ORDERED