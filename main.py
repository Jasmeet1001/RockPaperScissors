import cpu
import gameloop
import player

lives = 5
again = True

gameloop.clrscr()

while again:

    play_against = int(input("The Rock Paper Scissors game\n1. Player vs CPU\n2. CPU vs CPU\n3. Player vs Player\n"))

    match(play_against):
        case 1:
            player_name = input("Enter your name: ")
            cpu1 = cpu.Cpu(lives, "CPU")
            player1 = player.Player(lives, player_name)
        
            gameloop.clrscr()
            gameloop.play(cpu1, player1)

        case 2:
            cpu1 = cpu.Cpu(lives, "CPU1")
            cpu2 = cpu.Cpu(lives, "CPU2")
        
            gameloop.clrscr()
            gameloop.play(cpu1, cpu2)

        case 3:
            player1_name = input("Enter your name: ")
            player1 = player.Player(lives, player1_name)

            player2_name = input("Enter your name: ")
            player2 = player.Player(lives, player2_name)
        
            gameloop.clrscr()
            gameloop.play(player1, player2)

    play_again = input("Play again?(y/n): ")
    if (play_again.lower() not in ['y', 'yes']):
        again = False
    else:
        gameloop.clrscr()


# paper: \U0000270B
# rock:  \U0000270A
# sci: \U0000270C