
board = [" " for x in range(10)]
# player = "X"
# computer = "O"

def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == " "


def printBoard(board):
    spacing = 50            # only for aesthetics
    print('\t\t|\t\t|')
    print('\t' + board[1] + '\t|' + '\t' + board[2] + '\t|' + '\t' + board[3] )
    print('\t\t|\t\t|')
    print('-' * spacing)
    print('\t\t|\t\t|')
    print('\t' + board[4] + '\t|' + '\t' + board[5] + '\t|' + '\t' + board[6] )
    print('\t\t|\t\t|')
    print('-' * spacing)
    print('\t\t|\t\t|')
    print('\t' + board[7] + '\t|' + '\t' + board[8] + '\t|' + '\t' + board[9] )
    print('\t\t|\t\t|')


def isWinner(board, letter):
    # for i in range(3):

    # checking in each row
    for i in range(3):
        if board[3 * i + 1] == board[3 * i + 2] and board[3 * i + 2] == board[3 * i + 3] and board[3 * i + 2] == letter:
            return True

    # checking in each column
    for j in range(3):
        if board[1 + j] == board[4 + j] and board[4 + j] == board[7 + j] and board[7 + j] == letter:
            return True

    # checking in \ diagonal
    if board[1] == board[5] and board[5] == board[9] and board[9] == letter:
        return True

    # checking in / diagonal
    if board[3] == board[5] and board[5] == board[7] and board[7] == letter:
        return True

    # if no one won return false and a dummy value
    return False



def playerMove():
    run = True
    while run:
        move = input(" X \'s turn. Which position do you want(1-9):  ")
        try:
            move = int(move)
            if 0< move<10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X',move)

                else:
                    print("Already occupied")
            else:
                print("not valid number, should be between 1 and 9")
        except:
            print("Not a valid number. use integer values b/w 1 and 9")




def compMove():
    global board
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x!= 0]
    move = 0
    print("possible moves: " + str(possibleMoves))

    for lett in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = lett
            if isWinner(boardCopy, lett):     # " O "
                move = i
                return move

    openCorners = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            openCorners.append(i)

    if len(openCorners)> 0:
        move = selectRandom(openCorners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    openEdges = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            openEdges.append(i)
    if len(openEdges)> 0:
        move = selectRandom(openEdges)
    return move





def selectRandom(list):
    import random
    return list[random.randint(0,len(list))]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("TIC TAC TOE")
    printBoard(board)

    while not(isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print(" O won the game")
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("tie")
            else:
                insertLetter('O', move)
                printBoard(board)
                print("computer placed in position " + str(move))
                print("next is players move:")
        else:
            print(" O won the game")
            break

    if(isBoardFull(board)):
        print("Game finished")


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
        board = [" " for x in range(10)]
    else:
        break
