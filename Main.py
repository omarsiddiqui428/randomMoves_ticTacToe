# Tic Tac Toe Program
print("Welcome to Tic Tac Toe")

from Helpers import draw_board, check_turn, check_win
import json
import random

spots = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

playing = True
complete = False
turn = 0
last_turn = -1
move_number = 0
integer_choices = [1,2,3,4,5,6,7,8,9]
while playing: #explain here
    move_number += 1
    draw_board(spots)
    print("__________\n")
    if last_turn == turn:
        print("That spot is taken, pick an open spot")
    last_turn = turn

    #print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press Q to quit" )
    random_play = random.choice(integer_choices)
    #Exclude plays that have already been made
    integer_choices.remove(random_play)
    choice = str(random_play)
    if choice == 'Q':
        playing = False
    elif choice in ['1','2','3','4','5','6','7','8','9']:
        choice = int(choice)
        row = (choice - 1) // 3
        column = (choice - 1) % 3
        if spots[row][column] not in ["X","O"]:
            turn += 1
            spots[row][column] = check_turn(turn)
            # with open('game_record.json','r') as file:
            #     game_records = json.load(file)
            #     current_state = (spots[0][0], spots[0][1], spots[0][2], spots[1][0], spots[1][1], spots[1][2], spots[2][0], spots[2][1], spots[2][2],)
            #     x['Game 1']["move number " + str(move_number)] = current_state #How to add a new title for each game, with move numbers under it
            #     with open('game_record.json', 'w') as file:
            #         json.dump(game_records, file, indent=4)
                    #When you add the json, only update after the game ends, keep local dictionary of game states

    if check_win(spots) == True:
        playing = False
        complete = True

    if turn > 8:
        playing = False

draw_board(spots)

if complete == True:
    if check_turn(turn) == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

else:
    print("The game is tied. No winner.")

print("Thanks for playing!")

#every single other program requries a main function, so that's why we have this specific syntax
#Add computer player using rand
#Machine learning creates AI. Machine learning is creating a program in a way that it gets better/smarter as the program runs
#Machine learning to make this smarter- know this program inside and out to optimize it with Machine learning
