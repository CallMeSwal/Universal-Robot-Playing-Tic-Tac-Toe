import numpy as np
import cv2
import random

def isSpaceFree(board, position):
    # Return true if the passed move is free on the passed board.
    return board[position] == '-'

def makeMove(board, letter, position):
    board[position] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the top
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[0] == le and bo[1] == le and bo[2] == le) or # across the bottom
    (bo[6] == le and bo[3] == le and bo[0] == le) or # down the left side
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the middle
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the right side
    (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
    (bo[8] == le and bo[4] == le and bo[0] == le)) # diagonal

def chooseRandomMoveFromList(board, positionList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possiblePositions = []
    for i in positionList:
        if isSpaceFree(board, i):
            possiblePositions.append(i)

    if len(possiblePositions) != 0:
        return random.choice(possiblePositions)
    else:
        return None

def getNextMove(board):
    # First, check if we can win in the next move
    for i in range(9):
        copy = board[:]
        if isSpaceFree(copy, i):
            makeMove(copy, "X", i)
            if isWinner(copy, "X"):
                return i
    # Check if the player could win on his next move, and block them.
    for i in range(9):
        copy = board[:]
        if isSpaceFree(copy, i):
            makeMove(copy, "O", i)
            if isWinner(copy, "O"):
                return i
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if isSpaceFree(board, 4):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [1, 3, 5, 7])
    
def isBoardNotFull(board):
    return "-" in board
 
cap = cv2.VideoCapture(0)

OFFSET = 25

TicTacToe_Board_Val=[255, 255, 255, 255, 255, 255, 255, 255, 255]
TicTacToe_Board_Bin=["-", "-", "-", "-", "-", "-", "-", "-", "-"]


RECT_LG = {
    "x1":100,
    "y1":40,
    "x2":540,
    "y2":440
    }
RECT_1 = {
    "x1":100+OFFSET,
    "y1":40+OFFSET,
    "x2":247-OFFSET,
    "y2":173-OFFSET
    }
RECT_2 = {
    "x1":247+OFFSET,
    "y1":40+OFFSET,
    "x2":393-OFFSET,
    "y2":173-OFFSET
    }
RECT_3 = {
    "x1":393+OFFSET,
    "y1":40+OFFSET,
    "x2":540-OFFSET,
    "y2":173-OFFSET
    }
RECT_4 = {
    "x1":100+OFFSET,
    "y1":173+OFFSET,
    "x2":247-OFFSET,
    "y2":307-OFFSET
    }
RECT_5 = {
    "x1":247+OFFSET,
    "y1":173+OFFSET,
    "x2":393-OFFSET,
    "y2":307-OFFSET
    }
RECT_6 = {
    "x1":393+OFFSET,
    "y1":173+OFFSET,
    "x2":540-OFFSET,
    "y2":307-OFFSET
    }
RECT_7 = {
    "x1":100+OFFSET,
    "y1":307+OFFSET,
    "x2":247-OFFSET,
    "y2":440-OFFSET
    }
RECT_8 = {
    "x1":247+OFFSET,
    "y1":307+OFFSET,
    "x2":393-OFFSET,
    "y2":440-OFFSET
    }
RECT_9 = {
    "x1":393+OFFSET,
    "y1":307+OFFSET,
    "x2":540-OFFSET,
    "y2":440-OFFSET
    }

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw rectangle grid
    cv2.rectangle(gray, (RECT_LG["x1"], RECT_LG["y1"]), (RECT_LG["x2"], RECT_LG["y2"]), (255,255,0), 2)
    cv2.rectangle(gray, (RECT_1["x1"], RECT_1["y1"]), (RECT_1["x2"], RECT_1["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_2["x1"], RECT_2["y1"]), (RECT_2["x2"], RECT_2["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_3["x1"], RECT_3["y1"]), (RECT_3["x2"], RECT_3["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_4["x1"], RECT_4["y1"]), (RECT_4["x2"], RECT_4["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_5["x1"], RECT_5["y1"]), (RECT_5["x2"], RECT_5["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_6["x1"], RECT_6["y1"]), (RECT_6["x2"], RECT_6["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_7["x1"], RECT_7["y1"]), (RECT_7["x2"], RECT_7["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_8["x1"], RECT_8["y1"]), (RECT_8["x2"], RECT_8["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_9["x1"], RECT_9["y1"]), (RECT_9["x2"], RECT_9["y2"]), (0,255,0), 2)
    
    # Display the result+++++++++++++++++++++++++++++++++++ing frame
    cv2.imshow('Camera Feed',gray)

    k = cv2.waitKey(1)
    
    if (k%256 == 27):
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print("Images taken.")
        #Save images
        RECT_1_img = "img/RECT_1.png"
        cv2.imwrite(RECT_1_img, gray[RECT_1["y1"]:RECT_1["y2"], RECT_1["x1"]:RECT_1["x2"]])
        RECT_2_img = "img/RECT_2.png"
        cv2.imwrite(RECT_2_img, gray[RECT_2["y1"]:RECT_2["y2"], RECT_2["x1"]:RECT_2["x2"]])
        RECT_3_img = "img/RECT_3.png"
        cv2.imwrite(RECT_3_img, gray[RECT_3["y1"]:RECT_3["y2"], RECT_3["x1"]:RECT_3["x2"]])
        RECT_4_img = "img/RECT_4.png"
        cv2.imwrite(RECT_4_img, gray[RECT_4["y1"]:RECT_4["y2"], RECT_4["x1"]:RECT_4["x2"]])
        RECT_5_img = "img/RECT_5.png"
        cv2.imwrite(RECT_5_img, gray[RECT_5["y1"]:RECT_5["y2"], RECT_5["x1"]:RECT_5["x2"]])
        RECT_6_img = "img/RECT_6.png"
        cv2.imwrite(RECT_6_img, gray[RECT_6["y1"]:RECT_6["y2"], RECT_6["x1"]:RECT_6["x2"]])
        RECT_7_img = "img/RECT_7.png"
        cv2.imwrite(RECT_7_img, gray[RECT_7["y1"]:RECT_7["y2"], RECT_7["x1"]:RECT_7["x2"]])
        RECT_8_img = "img/RECT_8.png"
        cv2.imwrite(RECT_8_img, gray[RECT_8["y1"]:RECT_8["y2"], RECT_8["x1"]:RECT_8["x2"]])
        RECT_9_img = "img/RECT_9.png"
        cv2.imwrite(RECT_9_img, gray[RECT_9["y1"]:RECT_9["y2"], RECT_9["x1"]:RECT_9["x2"]])

        #Get value of each image
        TicTacToe_Board_Val[0] = np.average(gray[RECT_1["y1"]:RECT_1["y2"], RECT_1["x1"]:RECT_1["x2"]])
        TicTacToe_Board_Val[1] = np.average(gray[RECT_2["y1"]:RECT_2["y2"], RECT_2["x1"]:RECT_2["x2"]])
        TicTacToe_Board_Val[2] = np.average(gray[RECT_3["y1"]:RECT_3["y2"], RECT_3["x1"]:RECT_3["x2"]])
        TicTacToe_Board_Val[3] = np.average(gray[RECT_4["y1"]:RECT_4["y2"], RECT_4["x1"]:RECT_4["x2"]])
        TicTacToe_Board_Val[4] = np.average(gray[RECT_5["y1"]:RECT_5["y2"], RECT_5["x1"]:RECT_5["x2"]])
        TicTacToe_Board_Val[5] = np.average(gray[RECT_6["y1"]:RECT_6["y2"], RECT_6["x1"]:RECT_6["x2"]])
        TicTacToe_Board_Val[6] = np.average(gray[RECT_7["y1"]:RECT_7["y2"], RECT_7["x1"]:RECT_7["x2"]])
        TicTacToe_Board_Val[7] = np.average(gray[RECT_8["y1"]:RECT_8["y2"], RECT_8["x1"]:RECT_8["x2"]])
        TicTacToe_Board_Val[8] = np.average(gray[RECT_9["y1"]:RECT_9["y2"], RECT_9["x1"]:RECT_9["x2"]])

        for i in range(len(TicTacToe_Board_Val)):
            if TicTacToe_Board_Bin[i]!="X":
                if TicTacToe_Board_Val[i] < 120:
                    TicTacToe_Board_Bin[i]="O"
                elif TicTacToe_Board_Val[i] > 120:
                    TicTacToe_Board_Bin[i]="-"
        '''
        print(TicTacToe_Board_Val[0:3])
        print(TicTacToe_Board_Val[3:6])
        print(TicTacToe_Board_Val[6:9])
        '''
        print("Detected 'O' move. (User)")
        print(TicTacToe_Board_Bin[0:3])
        print(TicTacToe_Board_Bin[3:6])
        print(TicTacToe_Board_Bin[6:9])
        print('')
        pos=getNextMove(TicTacToe_Board_Bin)
        if isWinner(TicTacToe_Board_Bin, "O"):
            print("'O' has won the game.")
            break
        elif not(isBoardNotFull(TicTacToe_Board_Bin)):
            print("Board is full. Game is tied.")
            break
        else:
            makeMove(TicTacToe_Board_Bin, "X", pos)
            print("Response 'X' move. (Computer)")
            print(TicTacToe_Board_Bin[0:3])
            print(TicTacToe_Board_Bin[3:6])
            print(TicTacToe_Board_Bin[6:9])
            print('')
            if isWinner(TicTacToe_Board_Bin, "X"):
                print("'X' has won the game.")
                break
            elif not(isBoardNotFull(TicTacToe_Board_Bin)):
                print("Board is full. Game is tied.")
                break
            
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
