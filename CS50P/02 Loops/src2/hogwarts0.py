# students = {"Hermoine": "Gryffindor", 
#             "Draco": "Slytherin", 
#             "Harry": "Gryffindor",
#             "Ron": "Gryffindor",
#             "luna": "Ravenclaw",
#             "cedric": "Hufflepuff",
#             "cho": "Ravenclaw",
#             "neville": "Gryffindor",
# }

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Draco", "house": "Slytherin", "patronus": "snake"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "dog"},
    {"name": "luna", "house": "Ravenclaw", "patronus": "hare"},
    {"name": "cedric", "house": "Hufflepuff", "patronus": "stag"},
    {"name": "cho", "house": "Ravenclaw", "patronus": "swan"},
    {"name": "neville", "house": "Gryffindor", "patronus": "hare"},
]

for s in students:
    print(s["name"], s["house"], s["patronus"]) 