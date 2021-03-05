# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

import random
import sys

NUMBER_SPACES = 10
PLAYER_LETTER = ''
COMPUTER_LETTER = ''
NEXT_MOVE = 0
VERBOSE = False
BORDER = False


# !! Board Functionality
def drawBoard(board):
    """This function prints out the board that it was passed."""
    # "board" is a list of 10 strings representing the board (ignore index 0)
    if BORDER:
        print('_______')
        print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')
        print('-------')
        print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
        print('-------')
        print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
        print('-------')
    else:
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')


def getBoardCopy(board):
    """Make a duplicate of the board list and return it."""
    dupeBoard = []
    for space in range(len(board)):
        dupeBoard.append(board[space])
    return dupeBoard


def isSpaceFree(board, move):
    """Return True if the move is free on the provided board."""
    return board[move] == ' '


def isBoardFull(board):
    """Return True if every space on the board has been taken. Otherwise return False."""
    for i in range(1, NUMBER_SPACES):
        if isSpaceFree(board, i):
            return False
    return True


# !! Move Functionality
def makeMove(board, letter, move):
    board[move] = letter


def getPlayerMove(board):
    """Let the player type in their move."""
    temp = 0
    while str(temp) not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, temp):
        if VERBOSE and not isSpaceFree(board, temp):
            print("Space Already Taken, Please Choose Another!")
        print('What is your next move? (1-9)')
        temp = int(input())
    return temp


def chooseRandomMoveFromList(board, movesList):
    """
    Returns a valid move from the passed list on the passed board. \n
    Returns None if there is no valid move.
    """
    possibleMoves = []

    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    return None


def getComputerMove(board):
    """
    Given a board and the computer's letter, determine where to move and return that move. \n
    Here is our algorithm for our Tic Tac Toe AI:
    """
    copy = getBoardCopy(board)

    for i in range(1, NUMBER_SPACES):
        if isSpaceFree(copy, i):
            # Play out the next move on a new copy of the board so we don't affect the actual game
            makeMove(copy, COMPUTER_LETTER, i)
            # Check if the computer could win on their next move, and take it.
            if isWinner(copy, COMPUTER_LETTER):
                if VERBOSE:
                    print("Computer Decison 1: Best Move For Computer")
                return i

            # Check if the player could win on their next move, and block them.
            makeMove(copy, PLAYER_LETTER, i)
            if isWinner(copy, PLAYER_LETTER):
                if VERBOSE:
                    print("Computer Decison 2: Block Players Best Move")
                return i

    # Try to take one of the corners, if they are free.
    computer_next_move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if computer_next_move is not None:
        if VERBOSE:
            print("Computer Decison 3: Go For A Corner")
        return computer_next_move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        if VERBOSE:
            print("Computer Decison 4: Take The Center")
        return 5

    # Move on one of the sides.
    if VERBOSE:
        print("Computer Decison 5: Take A Side")
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# !! Game Paly Functionslity
def inputPlayerLetter():
    """Lets the player type which letter they want to be."""
    global PLAYER_LETTER
    global COMPUTER_LETTER
    while not (PLAYER_LETTER == 'X' or PLAYER_LETTER == 'O'):
        print('Do you want to be X or O?')
        PLAYER_LETTER = input().upper()
    COMPUTER_LETTER = 'O' if PLAYER_LETTER == 'X' else 'X'


def whoGoesFirst():
    """Randomly choose the player who goes first."""
    return 'computer' if random.randint(0, 1) == 0 else 'player'


def isWinner(board, letter):
    """Given a board and a player’s letter, this function returns True if that player has won."""
    return (
        # across the top
        (board[7] == board[8] == board[9] == letter) or
        # across the middle
        (board[4] == board[5] == board[6] == letter) or
        # across the bottom
        (board[1] == board[2] == board[3] == letter) or
        # down the left side
        (board[7] == board[4] == board[1] == letter) or
        # down the middle
        (board[8] == board[5] == board[2] == letter) or
        # down the right side
        (board[9] == board[6] == board[3] == letter) or
        # diagonals
        (board[7] == board[5] == board[3] == letter) or
        (board[9] == board[5] == board[1] == letter)
    )


def playAgain():
    """This function returns True if the player wants to play again, otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def playGame():
    """This Function Runs The Game!!"""
    while True:
        # Reset the board
        theBoard = [' '] * NUMBER_SPACES

        # Set The Global Variable for PLAYER_LETTER & COMPUTER_LETTER.
        inputPlayerLetter()

        # Do A 'Coin Toss' To See Who Goes First.
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')

        while True:
            # Check If There Is A Winner OR The Board Is Full,
            # If So State Witch One And End The Game.
            if isWinner(theBoard, PLAYER_LETTER):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                break
            elif isWinner(theBoard, COMPUTER_LETTER):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                break
            elif isBoardFull(theBoard):
                drawBoard(theBoard)
                print('The game is a tie!')
                break

            # The Board Is Not Full And There is No Winner Yet,
            # We Still Have Spots To Fill, So Whos Turn Is It?
            if turn == 'player':
                # Player’s turn.
                NEXT_MOVE = getPlayerMove(theBoard)
                makeMove(theBoard, PLAYER_LETTER, NEXT_MOVE)
                turn = 'computer'
            else:
                # Computer’s turn.
                NEXT_MOVE = getComputerMove(theBoard)
                makeMove(theBoard, COMPUTER_LETTER, NEXT_MOVE)
                turn = 'player'

            # Display The Updated Board And Whos Turn Is Next
            drawBoard(theBoard)
            print("\n" + turn.capitalize() + " will go next")

        if not playAgain():
            break


if __name__ == "__main__":
    VERBOSE = (len(sys.argv) > 1 and sys.argv[1] == '-v')
    BORDER = (len(sys.argv) > 2 and sys.argv[2] == '-b')
    print('Welcome to Tic Tac Toe!')
    playGame()
