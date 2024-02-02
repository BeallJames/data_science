def quicksort(arr, count=0):
    if len(arr) < 2:
        return arr, count
    else:
        pivot = arr[1]
        print(pivot)
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        count += 1
        result_less, count_less = quicksort(less, count)
        result_greater, count_greater = quicksort(greater, count)
        return result_less + [pivot] + result_greater, count_less + count_greater + count


input_list = [1,2,3,4,5,6,7,8,9,10]
sorted_list, count = quicksort(input_list)
print(f'{sorted_list}')
print(f'{count}')