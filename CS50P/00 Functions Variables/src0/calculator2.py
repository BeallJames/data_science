# # Demonstrates conversion from str to int

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# print("x + y = ", round((x / y),5))

def main():
    x = float(input("whats x? "))
    print("x square = ", square(x))

def square(n):
    return n * n

main()