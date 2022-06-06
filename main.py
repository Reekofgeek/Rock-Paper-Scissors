import random
# Instruction for the game
# performstring concatenation of string
print('''
Winning Rules of the Rock paper scissor game as follows:
Rock vs paper->Paper wins
Rock vs scissor->Rock wins
Paper vs scissor->Scissor wins
R => Rock
P => Paper
S => Scissor
''')

#loop meant to restart the game is there is a tie from both players at the end
while True:

    #dictionary which stores option for both players
    options = {
        'R':'rock',
        'P':'paper',
        'S':'scissors'
    }
    #inputting user choice
    player_Choice = input('Pick your option R, P or S: ')

    while player_Choice not in options:
        player_Choice = input('Error! Enter valid option: ')

    #assigning randomly an option for CPU
    cpu_choice = random.choice(list(options))
    print(f"CPU Choice is {cpu_choice}")
    print(f'Player {options.get(player_Choice)} : CPU {options.get(cpu_choice)}')

    #Checking move of both players
    #Determining the winner
    if ((player_Choice == 'R') and (cpu_choice == 'P') or (player_Choice == 'P') and (cpu_choice == 'S')):
        print('CPU Wins!')
    elif ((player_Choice == 'R') and (cpu_choice == 'S') or (player_Choice == 'S') and (cpu_choice == 'P')):
        print('Player Wins!')
    elif (player_Choice == 'S') and (cpu_choice == 'R'):
        print('CPU wins!')

    #Loop restarts game if there is a tie or end if there isn't
    if player_Choice == cpu_choice:
        print('It\'s a Tie! ...restarting game.')
    else:
        break







