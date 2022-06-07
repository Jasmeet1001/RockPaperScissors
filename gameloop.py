import actions
from time import sleep
import os

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def play(p1, p2):
    rounds = 1

    while p1.get_lives() > 0 and p2.get_lives() > 0:
        print(f"\nRound: {rounds}")
        print(f"Lives Remaining:\n\t{p1.get_name()}\t {p2.get_name()}\n\t {p1.get_lives()}\t  {p2.get_lives()}\n")
        sleep(1)

        action1 = p1.get_action()
        action2 = p2.get_action()

        if (action1 == action2):
            print("It's a tie!!")
            rounds += 1
            sleep(1.5)
            clrscr()
            continue

        elif (action1 == actions.Rps.rock):
            print(f"{p1.get_name()}: \U0000270A")
            if (action2 == actions.Rps.paper):
                print(f"{p2.get_name()}: \U0000270B")
                print(f"Paper covers rock. {p2.get_name()} wins this round!!")
                p1.lives -= 1
            else:
                print(f"{p2.get_name()}: \U0000270C")
                print(f"Rock crushes scissors. {p1.get_name()} wins this round!!")
                p2.lives -= 1

        elif (action1 == actions.Rps.paper):
            print(f"{p1.get_name()}: \U0000270B")
            if (action2 == actions.Rps.rock):
                print(f"{p2.get_name()}: \U0000270A")
                print(f"Paper covers rock. {p1.get_name()} wins this round!!")
                p2.lives -= 1
            else:
                print(f"{p2.get_name()}: \U0000270C")
                print(f"Scissor cuts paper. {p2.get_name()} wins this round!!")
                p1.lives -= 1
    
        elif (action1 == actions.Rps.scissors):
            print(f"{p1.get_name()}: \U0000270C")
            if (action2 == actions.Rps.paper):
                print(f"{p2.get_name()}: \U0000270B")
                print(f"Scissor cuts paper. {p1.get_name()} wins this round!!")
                p2.lives -= 1
            else:
                print(f"{p2.get_name()}: \U0000270A")
                print(f"Rock crushes scissors. {p2.get_name()} wins this round!!")
                p1.lives -= 1
        
        rounds += 1
        sleep(1.5)
        clrscr()

    else:
        print(f"\nRound: {rounds - 1}")
        print(f"Lives Remaining:\n\t{p1.get_name()}\t {p2.get_name()}\n\t {p1.get_lives()}\t  {p2.get_lives()}\n")
        sleep(0.5)
        if (p1.get_lives() == 0):
            print(f"{p2.get_name()} wins!!")
        else:
            print(f"{p1.get_name()} wins!!")