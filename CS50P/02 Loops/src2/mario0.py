def main():
    print_square(int(input("Size: ")))

def print_square(size):
    # for each row in suqare
    for i in range(size):
        # for each column in row
        for j in range(size):
            # print a star
            print("*", end="")
        # print a newline
        print()

main()