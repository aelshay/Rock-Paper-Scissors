import random
import os


def mainmenu():
    os.system('cls')
    menu = int(input("\nSelect your option:\n1) Play\n2) Quit\n\nSelection: ")) - 1
    if menu == 0:
        game()
    
    elif menu == 1:
        print("Thanks for playing!")

    else:
        mainmenu()
        

def game():

    playerlife = 3
    playerscore = 0

    while playerlife != 0:
        os.system('cls')
        rps = ['rock', 'paper', 'scissors']

        playerChoice = int(input(f"\nSelect your option:            Player Score: {playerscore} | Player lives: {playerlife}\n1) Rock\n2) Paper\n3) Scissors\n\nSelection: ")) - 1
        oppChoice = random.randint(0,2)

        print(f"\nPlayer chose: {rps[playerChoice]}\nOpponent chose: {rps[oppChoice]}")

        if (playerChoice == 2 and oppChoice == 1) or (playerChoice == 1 and oppChoice == 0) or (playerChoice == 0 and oppChoice == 2):
            print("\nplayer wins!\n")
            playerscore += 1
        elif playerChoice == oppChoice:
            print("\nIt's a draw!\n")
        else:
            print("\nOpponent wins!\n")
            playerlife -= 1

        if playerlife > 0:
            input("Press (Enter) to continue...")
        elif playerlife == 0:
            input("Better luck next time!\nGoing back to main menu...")
            mainmenu()

    


mainmenu()