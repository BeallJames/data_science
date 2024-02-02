# calculate the nth number in the Fibonacci sequence

def fibonacci(n):
    for i in range(n+1):
        print('i:', i)
        if i == 0:
            a, b = 0, 1
        else:
            a, b = b, a + b
            print(a)
    return a

print(fibonacci(int(input('input:'))))