from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledgeBase = And(
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight,CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    knowledgeBase,
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

#     # If A is a knight, then A is telling the truth
#     Implication(AKnight, Or(AKnight, AKnave)),
#     Implication(AKnight, Not(And(AKnight, AKnave))),
#     # If A is a knave, then A is lying
#     Implication(AKnave, Not(Or(AKnight, AKnave))),
#     Implication(AKnave, And(AKnight, AKnave)),
#     # If B is a knight, then B is telling the truth
#     Implication(BKnight, Or(BKnight, BKnave)),
#     Implication(BKnight, Not(And(BKnight, BKnave))),
#     # If B is a knave, then B is lying
#     Implication(BKnave, Not(Or(BKnight, BKnave))),
#     Implication(BKnave, And(BKnight, BKnave)),
#     # If C is a knight, then C is telling the truth
#     Implication(CKnight, Or(CKnight, CKnave)),
#     Implication(CKnight, Not(And(CKnight, CKnave))),
#     # If C is a knave, then C is lying
#     Implication(CKnave, Not(Or(CKnight, CKnave))),
#     Implication(CKnave, And(CKnight, CKnave)),
#     # If A is a knight, then B is a knave
#     Implication(AKnight, BKnave),
#     # If A is a knight, then C is a knave
#     Implication(AKnight, CKnave),
#     # If B is a knight, then A is a knave
#     Implication(BKnight, AKnave),
#     # If B is a knight, then C is a knave
#     Implication(BKnight, CKnave),
#     # If C is a knight, then A is a knight
#     Implication(CKnight, AKnight),
#     # If C is a knight, then B is a knight
#     Implication(CKnight, BKnight),
#     # If A is a knave, then B is a knight
#     Implication(AKnave, BKnight),
#     # If A is a knave, then C is a knight
#     Implication(AKnave, CKnight),
#     # If B is a knave, then A is a knight
#     Implication(BKnave, AKnight),
#     # If B is a knave, then C is a knight
#     Implication(BKnave, CKnight),
#     # If C is a knave, then A is a knave
#     Implication(CKnave, AKnave),
#     # If C is a knave, then B is a knave
#     Implication(CKnave, BKnave)    
# )

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    knowledgeBase,
    Implication(AKnight, And(AKnave,BKnave)),
    Implication(AKnave, Not(And(AKnave,BKnave)))
)

#     # A is either a knight or a knave, but not both
#     Or(AKnight, AKnave),
#     Not(And(AKnight, AKnave))

#     # B is either a knight or a knave, but not both
#     Or(BKnight, BKnave),
#     Not(And(BKnight, BKnave))

#     # C is either a knight or a knave, but not both
#     Or(CKnight, CKnave),
#     Not(And(CKnight, CKnave))

#     # If A is a knight, then A is telling the truth
#     Implication(AKnight, Or(AKnight, AKnave)),
#     Implication(AKnight, Not(And(AKnight, AKnave))),
#     # If A is a knave, then A is lying
#     Implication(AKnave, Not(Or(AKnight, AKnave))),
#     Implication(AKnave, And(AKnight, AKnave)),
#     # If B is a knight, then B is telling the truth
#     Implication(BKnight, Or(BKnight, BKnave)),
#     Implication(BKnight, Not(And(BKnight, BKnave))),
#     # If B is a knave, then B is lying
#     Implication(BKnave, Not(Or(BKnight, BKnave))),
#     Implication(BKnave, And(BKnight, BKnave)),
#     # If A is a knight, then B is a knave
#     Implication(AKnight, BKnave),
#     # If A is a knight, then C is a knave
#     Implication(AKnight, CKnave),
#     # If B is a knight, then A is a knave
#     Implication(BKnight, AKnave),
#     # If B is a knight, then C is a knave
#     Implication(BKnight, CKnave),
#     # If C is a knight, then A is a knight
#     Implication(CKnight, AKnight),
#     # If C is a knight, then B is a knight
#     Implication(CKnight, BKnight),
#     # If A is a knave, then B is a knight
#     Implication(AKnave, BKnight),
#     # If A is a knave, then C is a knight
#     Implication(AKnave, CKnight),
#     # If B is a knave, then A is a knight
#     Implication(BKnave, AKnight),
#     # If B is a knave, then C is a knight
#     Implication(BKnave, CKnight),
#     # If C is a knave, then A is a knave
#     Implication(CKnave, AKnave),
#     # If C is a knave, then B is a knave
#     Implication(CKnave, BKnave)
# )

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    knowledgeBase,
    Implication(AKnight, And(AKnight,BKnight)),
    Implication(AKnave, Not(And(AKnight,BKnight))),
    Implication(BKnight, And(BKnight,AKnave)),
    Implication(BKnave, Not(And(BKnight,AKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    knowledgeBase,
    # Implication(AKnight, ),
    # Implication(AKnave, ),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnight)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
