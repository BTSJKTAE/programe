import random

print("There are totally 21 sticks who take's the last stick they lose")

total_sticks = 21
player=0

def calculate():
    global total_sticks, player
    print("computer: ", computer)
    print("player: ", player)
    total_sticks = total_sticks - player - computer
    print("Total stick", total_sticks)

while total_sticks > 0:
    choices = [1,2, 3, 4, 5]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = int(input("1, 2 , 3, 4, or 5?: "))
        if player > 0 and player < 6:
            calculate()

        else:
            print("Enter the number between 1 to 5")

else:

    print("Game END")

