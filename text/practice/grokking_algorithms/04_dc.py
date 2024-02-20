def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
print(sum([1, 2, 3, 4]))

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])
print(sum([1, 2, 3, 5]))

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])
print(count([1, 2, 3, 4, 100]))