# main method referencing all other methods
def game(pos, player: int):

    count = 0 # count is to limit to 9 inputs
    players = ['X', 'O']
    board(pos)      # print the board in initial state
    filled = []     # mapping all filled positions to prevent overwriting
    #

    # for further improvement of code
    # if player == 1:
    #    pass
    # else:
    #    players[1],players[0] = players[0],players[1]

    while True:

        # checking if any player won
        won, winner = checkifwon(pos)
        if not won:
            if count% 2 == 0:
                print("O's turn")
            else:
                print("X's turn")

            # for limiting to 9 entries
            if count > 8:
                print("No-one won, t'was a draw")
                break
            
            # players input position
            inp = input("Please enter the position: ")

            # try and except to make sure not to recieve any non-integer value
            try:
                inp = int(inp)

                # Make sure not to overwrite
                if inp not in filled:
                    if inp > 9 or inp <1 :
                        print("Not Valid")
                        continue
                    if count % 2 == 1:
                        pos[inp - 1] = players[0]
                        board(pos)
                        
                    elif count % 2 == 0:
                        pos[inp - 1] = players[1]
                        board(pos)
                        
                    filled.append(inp)
                    
                    count += 1
                else:
                    print("That position is already filled")
                    continue
            except:
                print("Please enter a valid position between 1 and 9")
                continue
        else:
            print("Ggame Finished")
            print("{} won the game".format(winner))
            
            # print(filled)      # for debugging
            break


# method to print the board
def board(pos):

    print("\n")
    print("="* 80)
    for i in range(3):

        print(("|" + "\t"* 2 + "|") * 3)
        print("|" + "\t" + str(pos[3*i + 0]) +  "\t" +"|" +"|" + "\t" + str(pos[3*i + 1]) +  "\t" + "|" +"|" + "\t" + str(pos[3*i + 2]) +  "\t" + "|")
        print(("|" + "\t"* 2 + "|") * 3)
        print("="* 80)
        
    print("\n")


# Method to check if any player won 
def checkifwon(pos):

    # checking in each row
    for i in range(3):
        if pos[3*i+0] == pos[3*i+1] and pos[3*i+1] == pos[3*i+2]:
            return True,pos[3*i+0]

    # checking in each column
    for j in range(3):
        if pos[0+j] == pos[3 + j] and pos[3+j] == pos[6 + j]:
            return True,pos[3 + j]

    # checking in \ diagonal
    if pos[0] == pos [4] and pos[4] == pos [8]:
        return True,pos [4]

    # checking in / diagonal
    if pos[2] == pos [4] and pos[4] == pos [6]:
        return True,pos [4]

    # if no one won return false and a dummy value
    return False, '_'
    

# initialise position array
pos = []

for i in range(3):
    for j in range(3):

        # entering the values for positioning (1,2,3,...9)
        pos.append(i * 3 + j+1)
        # print("pos [{}, {}] is {}".format(i, j, pos[3*i + j] ))       #for debugging


while True:
    play = input("press y to continue playing: ")

    if play == 'y' or play == 'Y':
        for i in range(3):
            for j in range(3):

                # entering the values for positioning (1,2,3,...9)
                pos[3*i+j] = 3*i+j+1
                # print("pos [{}, {}] is {}".format(i, j, pos[3*i + j] ))       #for debugging
                # calling the main function
        game(pos, 0)
    else:
        print("thanks for playing")
        break

