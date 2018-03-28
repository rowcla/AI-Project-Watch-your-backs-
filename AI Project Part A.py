
# coding: utf-8

# In[77]:


# Counts available moves for pieces of colour a, with the opposing team being represented by b
def Moves(brd, a, b):
    count=0
    i=0
    # Loop through the board, checking for pieces we want to check the moves for
    for row in brd:
        j=0
        for space in row:
            if space==b:
                # Once we've found a valid piece, check in each direction, but only if there's board left in that direction
                if i!=0:
                    # We know we can't move if the piece to our side is a cornor
                    if brd[i-1][j]!="X":
                        if brd[i-1][j]!="-":
                            #  If there's no valid space on the other side of the piece we want to jump, we deincrement
                            if i==1 or brd[i-2][j]!="-":
                                count-=1
                        # Increment in all cases except for the first test case, since we deincrement if it's invalid anyway        
                        count+=1
                # Repeat for each direction        
                if i!=7:
                    if brd[i+1][j]!="X":
                        if brd[i+1][j]!="-":
                            if i==6:
                                count-=1
                            elif brd[i+2][j]!="-":
                                    count-=1
                        count+=1
                if j!=0:
                    if brd[i][j-1]!="X":
                        if brd[i][j-1]!="-":
                            if j==1 or brd[i][j-2]!="-":
                                count-=1
                        count+=1
                if j!=7:
                    if brd[i][j+1]!="X":
                        if brd[i][j+1]!="-":
                            if j==6:
                                count-=1
                            elif brd[i][j+2]!="-":
                                    count-=1
                        count+=1
            j+=1
        i+=1
    # finally, print out the result    
    print(count)

#Finds and then solves sequence of moves required for the White player to eliminate all the Black pieces
def Massacre(board):

#Makes sure position is valid
def isValid(board, row, column):
    if row>7 or row<0 or column>7 or column<0:
        return False
    potential = board[row][column]
    if potential == "X" or potential == "@" or potential == "O":
        return False
    else:
        return True


#Finds the number of available adjacent spaces of a piece
def numAdj(board, row, column):
    num = 0
    available = []
    if isValid(board, row+1, column):
        num += 1
        available.append((row+1, column))
    if isValid(board, row-1, column):
        num += 1
        available.append((row-1, column))
    if isValid(board, row, column+1):
        num += 1
        available.append((row, column+1))
    if isValid(board, row, column-1):
        num += 1
        available.append((row, column-1))
    return [num, available]

#Checks if two positions are in the same row or column
def sameRowCol(space1, space2):
    if (space1[0] == space2[0]) or (space1[1] == space2[1]):
        return True
    else:
        return False
#Places the White piece in the correct spot
def placeWhite(board, row, column):
    if board[row][column] == "O":
        return 0
    else:
        board[row][column] = "O"
        return 1

#Finds whether a black position has another adjacent black
def adjBlack(board, row, column):
    if board[row+1][column] == "@":
        return (row-1, column)
    if board[row-1][column] == "@":
        return (row+1, column)
    if board[row][column+1] == "@":
        return (row, column-1)
    if board[row][column-1] == "@":
        return (row, column+1)
    else:
        #tuple symbolising none
        return (0,0)

#Finds whether a black position alread has an adjacent white
def adjWhite(board, row, column):
    if board[row+1][column] == "O":
        return (row-1, column)
    if board[row-1][column] == "O":
        return (row+1, column)
    if board[row][column+1] == "O":
        return (row, column-1)
    if board[row][column-1] == "O":
        return (row, column+1)
    else:
        #tuple symbolising none
        return (0,0)

#Finds a winning goal state for the White player
def findGoalState(board):
    #number of White pieces on the board
    numWhite = 0
    numBlack = 0
    coorBlack = []
    #iterate through the board and count the number of White pieces and then remove them and also save the coor of any
    #of the Black pieces
    for row in range(7):
        for column in range(7):
            if board[row][column] == "O":
                board[row][column] = "-"
                numWhite += 1
            elif board[row][column] == "@":
                coorBlack.append((row, column))
                numBlack += 1
    #iterate through the coordinates of the Black pieces and place the White pieces to create a winning state
    for coor in coorBlack:
        if numWhite > 0:
            numFree = numAdj(board, coor[0], coor[1])[0]
            spacesFree = numAdj(board, coor[0], coor[1])[1]
            #Case 1, 1 free spot
            if numFree == 1 and numWhite >= 0:
                numWhite -= placeWhite(board, spacesFree[0][0], spacesFree[0][1])
            #Case 2, 2 free spots
            elif numFree == 2 and numWhite >= 0:
                if adjBlack(board, coor[0], coor[1]) != (0, 0):
                    numWhite -= placeWhite(board, adjBlack(board, coor[0], coor[1])[0],
                                           adjBlack(board, coor[0], coor[1])[1])
                elif adjWhite(board, coor[0], coor[1]) != (0, 0):
                    numWhite -= placeWhite(board, adjWhite(board, coor[0], coor[1])[0],
                                           adjWhite(board, coor[0], coor[1])[1])
                elif sameRowCol(spacesFree[0], spacesFree[1]):
                    numWhite -= placeWhite(board, spacesFree[0][0], spacesFree[0][1]) + \
                                placeWhite(board, spacesFree[1][0], spacesFree[1][1])
                elif spacesFree[0][0] == 0 or spacesFree[0][0] == 7 or spacesFree[0][1] == 0 or spacesFree[0][1] == 7:
                    numWhite -= placeWhite(board, spacesFree[0][0], spacesFree[0][1])
                else:
                    numWhite -= placeWhite(board, spacesFree[1][0], spacesFree[1][1])
            #Case 3, 3 free spots
            elif numFree == 3 and numWhite >= 0:
                if adjBlack(board, coor[0], coor[1]) != (0, 0):
                    numWhite -= placeWhite(board, adjBlack(board, coor[0], coor[1])[0],
                                           adjBlack(board, coor[0], coor[1])[1])
                elif adjWhite(board, coor[0], coor[1]) != (0, 0):
                    numWhite -= placeWhite(board, adjWhite(board, coor[0], coor[1])[0],
                                           adjWhite(board, coor[0], coor[1])[1])
                elif sameRowCol(spacesFree[0], spacesFree[1]):
                    numWhite -= placeWhite(board, spacesFree[0][0], spacesFree[0][1]) + \
                                placeWhite(board, spacesFree[1][0], spacesFree[1][1])
                elif sameRowCol(spacesFree[0], spacesFree[2]):
                    numWhite -= placeWhite(board, spacesFree[0][0], spacesFree[0][1]) + \
                                placeWhite(board, spacesFree[2][0], spacesFree[2][1])
                else:
                    numWhite -= placeWhite(board, spacesFree[1][0], spacesFree[1][1]) + \
                                placeWhite(board, spacesFree[2][0], spacesFree[2][1])
            #final case, 4 free spots
            elif numFree == 4 and numWhite >= 0:
                numWhite -= placeWhite(board, spacesFree[0][0], spacesFree[0][1]) + \
                            placeWhite(board, spacesFree[1][0], spacesFree[1][1])
            numBlack -= 1
    return board

#print board function
def printBoard(board):
    print board[0]
    print board[1]
    print board[2]
    print board[3]
    print board[4]
    print board[5]
    print board[6]
    print board[7]
    return

# In[79]:


# Open the board state file, based on the user input
file=open(input(),"r")
board=file.read()
# Split each line into rows, then each row into spaces
board=board.splitlines()
i=0
for line in board:
    board[i]=line.split()
    i+=1
# Record the desired action to take on the board    
action=board[8][0]
# Remove the action line, so the board is only the board
del board[-1]
# Run commands as required
if action=="Massacre":
    Massacre(board)
if action=="Moves":
    # Since the Moves function takes each side individually, run it for both sides
    Moves(board, "O", "@")
    Moves(board, "@", "O")

