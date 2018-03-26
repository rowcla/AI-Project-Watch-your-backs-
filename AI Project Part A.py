
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

