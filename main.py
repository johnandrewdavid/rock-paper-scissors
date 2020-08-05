# Rock, Paper, Scissors Game

# Example
# rock - rock = 0
# rock - paper = -1
# rock - scissors = -2

import random

hands = ['rock', 'paper', 'scissors']


def game():
    player = int(input("1.Rock 2.Paper 3.Scissors\n"))
    cpu = random.randint(1, 3)

    try:
        compare(player, cpu)
    except IndexError:
        print("Please input a valid number.")
        game()


def compare(h1, h2):
    score = h1 - h2

    print("You chose " + hands[h1 - 1])
    print("CPU chose " + hands[h2 - 1])

    if score == 0:
        print("Try Again")
        game()
    elif score in (1, -2):
        print("You Win!")
        retry()
    else:
        print("You Lose!")
        retry()


def retry():
    try:
        leave = input("Would you like to play again?\nPress enter to play again, [0] to exit.\n")
        if int(leave) == 0:
            print("Thank you for playing!")

    except ValueError:
        print("New Game")
        game()


if __name__ == '__main__':
    game()
