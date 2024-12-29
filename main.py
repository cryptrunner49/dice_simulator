import random

def roll_dice():
    roll = input("Roll the dice? (y/n): ")

    C='o '
    while roll.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"dice rolled: {dice1} and {dice2}")

        number_to_draw = dice1-1
        dice1_ascii='-----\n|'+C[number_to_draw<1]+' '+C[number_to_draw<3]+'|\n|'+C[number_to_draw<5]
        print(dice1_ascii+C[number_to_draw&1]+dice1_ascii[::-1])

        number_to_draw = dice2-1
        dice2_ascii='-----\n|'+C[number_to_draw<1]+' '+C[number_to_draw<3]+'|\n|'+C[number_to_draw<5]
        print(dice2_ascii+C[number_to_draw&1]+dice2_ascii[::-1])

        roll = input("Roll again? (y/n): ")

roll_dice()