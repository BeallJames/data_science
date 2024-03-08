# Compares multiple strings with if/elif/else

name = input("What's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# # elif name == "Hermione":
# #     print("Gryffindor")
# # elif name == "Ron":
# #     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermoine" | "Ron": 
        print("Gry")
    case "Hermoine":
        print("Gryyyyffff")
    case _:
        print("---------------")