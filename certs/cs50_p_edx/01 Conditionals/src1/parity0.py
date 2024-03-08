# # Demonstrates modulo operator

# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")


def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    return n % 2 == 0

main()