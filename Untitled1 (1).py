
# coding: utf-8

# In[1]:


Smp_Brd = []
Smp_Brd.append(['X','-','-','-','-','-','-','X'])
Smp_Brd.append(['-','-','-','-','-','-','-','-'])
Smp_Brd.append(['-','-','-','O','O','@','-','-'])
Smp_Brd.append(['-','-','O','-','-','@','-','-'])
Smp_Brd.append(['-','O','-','-','@','-','-','-'])
Smp_Brd.append(['-','-','@','-','O','@','-','-'])
Smp_Brd.append(['-','-','O','O','-','-','O','-'])
Smp_Brd.append(['X','-','-','-','-','-','-','X'])
Smp_Brd


# In[59]:


import copy
# Setup the board with relevant sub-data to go with it
def Initialise_Board(Board, Player):
    print_brd(Board)
    # define the edges of the board
    min_edge=0
    max_edge=7
    # Larger list to store the extra data
    big_brd=[]
    big_brd.append(Board)
    big_brd.append([])
    # Fill in a blank board, which we'll use to keep track of capture threats on each given square
    for i in range(8):
        big_brd[1].append([])
        for j in range(8):
            big_brd[1][i].append('-')
    big_brd.append([])
    for i in range(8):
        big_brd[2].append([])
        for j in range(8):
            big_brd[2][i].append('-')
    # Lists of pieces for each player
    Enemy_list=[]
    Our_list=[]
    i=0
    for row in big_brd[0]:
        j=0
        for col in row:
            # If we're black, for simplicity, rewrite the board so that we're white (we'll change it back later)
            if col == '@':
                if Player=='@':
                    Our_list.append([i, j])
                    col='O'
                else:    
                    Enemy_list.append([i, j])
            if col == 'O':
                if Player=='@':
                    col='@'
                    Enemy_list.append([i, j])
                else:
                    Our_list.append([i, j])
            j+=1
        i+=1
    # write in threat positions for each square, based off of the relative positions of each enemy piece
    # for the threat positions, the formatting has the final value of the string as a number, which indicates how many turns
    # (up to 1), it takes for the capture to be made
    # the letters encapsulate what kind of capture it is
    # If there's only 1 letter, that means both capturing pieces are directly above and below, or directly left and right
    # If the there's one letter, but it takes a move, that means the piece that needs to move has to move in that direction
    # If there's 2 letters, the first letter indicates that there is a piece one square in that direction of the capture square
    # and the second indicates that there is a piece one square in that direction, and one square in the opposite direction
    # to the first letter
    for piece in Enemy_list:
        for piece2 in Enemy_list:
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])==0:
                big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]="u0"
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])==0:
                big_brd[1][int((piece2[1]+piece[1])/2)][piece[0]]="l0"
                
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])==1:
                if piece2[0]>piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]][-1]!='0':
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]="ur1"
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]][-1]!='0':    
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]="dl1"
                if piece2[0]<piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]][-1]!='0':
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]="dr1"
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]][-1]!='0':    
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]="ul1"

                        
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])==1:
                if piece2[1]>piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]="lu1"
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]="rd1"
                if piece2[1]<piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]="ru1"
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]="ld1"       
                    
            if abs(piece[0]-piece2[0])==3 and abs(piece[1]-piece2[1])==0:
                if big_brd[0][int((piece2[0]+piece[0]-1)/2)][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0]+1)/2)][piece[1]][-1]!='0':
                    big_brd[1][int((piece2[0]+piece[0]+1)/2)][piece[1]]="d1"
                if big_brd[0][int((piece2[0]+piece[0]+1)/2)][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0]-1)/2)][piece2[1]][-1]!='0':    
                    big_brd[1][int((piece2[0]+piece[0]-1)/2)][piece2[1]]="u1"
                    
            if abs(piece[1]-piece2[1])==3 and abs(piece[0]-piece2[0])==0:
                if big_brd[0][piece[0]][int((piece2[1]+piece[1]-1)/2)]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1]+1)/2)][-1]!='0':
                    big_brd[1][piece[0]][int((piece2[1]+piece[1]+1)/2)]="r1"
                if big_brd[0][piece2[0]][int((piece2[1]+piece[1]+1)/2)]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1]-1)/2)][-1]!='0':
                    big_brd[1][piece2[0]][int((piece2[1]+piece[1]-1)/2)]="l1"
                    
    # Repeat the same process for our pieces too, but to store in a different list                
    for piece in Our_list:
        for piece2 in Our_list:
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])=="u0":
                big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]=0
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])=="l0":
                big_brd[2][int((piece2[1]+piece[1])/2)][piece[0]]=0
                
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])==1:
                if piece2[0]>piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]][-1]!='0':
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]="ur1"
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]][-1]!='0':    
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]]="dl1"
                if piece2[0]<piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]][-1]!='0':
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]="dr1"
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]][-1]!='0':    
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]]="ul1"

                        
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])==1:
                if piece2[1]>piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)]="lu1"
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)]="rd1"
                if piece2[1]<piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)]="ru1"
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)][-1]!='0':
                        big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)]="ld1"       
                    
            if abs(piece[0]-piece2[0])==3 and abs(piece[1]-piece2[1])==0:
                if big_brd[0][int((piece2[0]+piece[0]-1)/2)][piece[1]]!='@' and big_brd[2][int((piece2[0]+piece[0]+1)/2)][piece[1]][-1]!='0':
                    big_brd[2][int((piece2[0]+piece[0]+1)/2)][piece[1]]="d1"
                if big_brd[0][int((piece2[0]+piece[0]+1)/2)][piece2[1]]!='@' and big_brd[2][int((piece2[0]+piece[0]-1)/2)][piece2[1]][-1]!='0':    
                    big_brd[2][int((piece2[0]+piece[0]-1)/2)][piece2[1]]="u1"
                    
            if abs(piece[1]-piece2[1])==3 and abs(piece[0]-piece2[0])==0:
                if big_brd[0][piece[0]][int((piece2[1]+piece[1]-1)/2)]!='@' and big_brd[2][piece[0]][int((piece2[1]+piece[1]+1)/2)][-1]!='0':
                    big_brd[2][piece[0]][int((piece2[1]+piece[1]+1)/2)]="r1"
                if big_brd[0][piece2[0]][int((piece2[1]+piece[1]+1)/2)]!='@' and big_brd[2][piece2[0]][int((piece2[1]+piece[1]-1)/2)][-1]!='0':
                    big_brd[2][piece2[0]][int((piece2[1]+piece[1]-1)/2)]="l1"                 
    #print_brd(big_brd[1])
    # Store data on playable moves
    move_list=[]
    # Store data on pieces which we can capture, or that our opponent can capture
    priority_targets=[]
    # Fill out move_list by checking for valid moves that won't immediately kill us
    for piece in Our_list:
        if piece[0]>min_edge:
            if big_brd[1][piece[0]-1][piece[1]]=='-' and big_brd[0][piece[0]-1][piece[1]]=='-':
                move_list.append(list(piece))
                move_list[-1].append("u1")
            if big_brd[0][piece[0]-1][piece[1]]=='@' or big_brd[0][piece[0]-1][piece[1]]=='O':
                if piece[0]>min_edge+1:
                    if big_brd[1][piece[0]-2][piece[1]]=='-' and big_brd[0][piece[0]-2][piece[1]]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("u2")
                        
        if piece[1]>min_edge:
            if big_brd[1][piece[0]][piece[1]-1]=='-' and big_brd[0][piece[0]][piece[1]-1]=='-':
                move_list.append(list(piece))
                move_list[-1].append("l1")
            if big_brd[0][piece[0]][piece[1]-1]=='@' or big_brd[0][piece[0]][piece[1]-1]=='O':
                if piece[1]>min_edge+1:
                    if big_brd[1][piece[0]][piece[1]-2]=='-' and big_brd[0][piece[0]][piece[1]-2]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("l2")
                        
        if piece[0]<max_edge:
            if big_brd[1][piece[0]+1][piece[1]]=='-' and big_brd[0][piece[0]+1][piece[1]]=='-':
                move_list.append(list(piece))
                move_list[-1].append("d1")
            if big_brd[0][piece[0]+1][piece[1]]=='@' or big_brd[0][piece[0]+1][piece[1]]=='O':
                if piece[0]<max_edge-1:
                    if big_brd[1][piece[0]+2][piece[1]]=='-' and big_brd[0][piece[0]+2][piece[1]]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("d2")
                        
        if piece[1]<max_edge:
            if big_brd[1][piece[0]][piece[1]+1]=='-' and big_brd[0][piece[0]][piece[1]+1]=='-':
                move_list.append(list(piece))
                move_list[-1].append("r1")
            if big_brd[0][piece[0]][piece[1]+1]=='@' or big_brd[0][piece[0]][piece[1]+1]=='O':
                if piece[1]<max_edge-1:
                    if big_brd[1][piece[0]][piece[1]+2]=='-' and big_brd[0][piece[0]][piece[1]+2]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("r2")
        # Fill out priority targets, by checking if the opponent has any moves which allow them to take our piece                
        if big_brd[1][piece[0]][piece[1]][-1]=='1':
            
            priority_targets.append(list(piece))
            priority_targets[-1].append('S')
    # And if we have any moves that allow us to take their piece        
    for piece in Enemy_list:
        if big_brd[2][piece[0]][piece[1]][-1]=='1':
            priority_targets.append(list(piece))
            priority_targets[-1].append('K')
    
    #print_brd(big_brd[2])
    # Add in our extra data to the big board
    big_brd.append(priority_targets)
    big_brd.append(move_list)
    big_brd.append(Our_list)
    big_brd.append(Enemy_list)
    #print(priority_targets)
    #print(move_list)
    return big_brd
    
#Initialise_Board(Smp_Brd, 'O')    
determine_move(Initialise_Board(Smp_Brd, 'O') )


# In[13]:


# funtion to print out the board in a readable format
# mostly just for testing purposes
def print_brd(Board):
    for line in Board:
        for col in line:
            # In order to make it readable, we only print out the final value in the string
            # Meaning on our capturable squares boards, we only print out the number of turns it takes to do so
            print(str(col)[-1], end=' ')
        print()    
    print()    


# In[58]:


# function to determine the best move from the board and accompanying data
def determine_move(big_brd):
    # List of moves that are particularly valuable (as they save or kill a piece (or both!))
    plus_point_moves=[]
    # Fill in the plus_point_moves list, by checking each priority target for options to capatilise on them
    for piece in big_brd[3]:
        if piece[2]=='S':
            kill_option=big_brd[1][piece[0]][piece[1]]
            for move in big_brd[4]:
                
                temp=[0, 0]
                if move[2][0]=='u':
                    
                    temp[0]=move[0]-int(move[2][1])
                    temp[1]=move[1]
                if move[2][0]=='d':
                    temp[0]=move[0]+int(move[2][1])
                    temp[1]=move[1]    
                if move[2][0]=='l':
                    temp[1]=move[1]-int(move[2][1])
                    temp[0]=move[0] 
                if move[2][0]=='r':
                    temp[1]=move[1]+int(move[2][1])
                    temp[0]=move[0]       
                if move[0]==piece[0] and move[1]==piece[1]:
                    plus_point_moves.append(move)
                if kill_option[0]=='d':
                    if temp[0]==piece[0]-1 and temp[1]==piece[1]:
                        plus_point_moves.append(move)
                if kill_option[0]=='u':
                    if temp[0]==piece[0]+1 and temp[1]==piece[1]:
                        plus_point_moves.append(move)
                if kill_option[0]=='r':
                    if temp[0]==piece[0] and temp[1]==piece[1]-1:
                        plus_point_moves.append(move)
                if kill_option[0]=='l':
                    if temp[0]==piece[0] and temp[1]==piece[1]+1:
                        plus_point_moves.append(move)   
            for piece2 in big_brd[3]:
                # Keeps track of if we can kill this particular piece
                kill_it=0
                if piece2[2]=='K':
                    if kill_option[0]=="d1":
                        if piece2[0]==piece[0]+1 and piece2[1]==piece[1]:
                            kill_it=1  
                        
                    elif kill_option[1]=="dl1":
                        if piece2[0]==piece[0]-1 and piece2[1]==piece[1]-1:
                            kill_it=1
                    elif kill_option[1]=="dr1":
                        if piece2[0]==piece[0]-1 and piece2[1]==piece[1]+1:
                            kill_it=1
                    elif kill_option[0]=="u1":
                        if piece2[0]==piece[0]-1 and piece2[1]==piece[1]:
                            kill_it=1  
                        
                    elif kill_option[1]=="ul1":
                        if piece2[0]==piece[0]+1 and piece2[1]==piece[1]-1:
                            kill_it=1
                    elif kill_option[1]=="ur1":
                        if piece2[0]==piece[0]+1 and piece2[1]==piece[1]+1:
                            kill_it=1        
                    elif kill_option[0]=="r1":
                        if piece2[0]==piece[0] and piece2[1]==piece[1]+1:
                            kill_it=1  
                        
                    elif kill_option[1]=="ru1":
                        if piece2[0]==piece[0]-1 and piece2[1]==piece[1]-1:
                            kill_it=1
                    elif kill_option[1]=="rd1":
                        if piece2[0]==piece[0]+1 and piece2[1]==piece[1]-1:
                            kill_it=1    
                    elif kill_option[0]=="l1":
                        if piece2[0]==piece[0] and piece2[1]==piece[1]-1:
                            kill_it=1  
                        
                    elif kill_option[1]=="dl1":
                        if piece2[0]==piece[0]+1 and piece2[1]==piece[1]+1:
                            kill_it=1
                    elif kill_option[1]=="dr1":
                        if piece2[0]==piece[0]-1 and piece2[1]==piece[1]+1:
                            kill_it=1
                    if kill_it!=0:
                        if big_brd[2][piece2[0]][piece2[1]][2]=="d1":
                            plus_point_moves.append([piece2[0]-2, piece2[1], "d1"])
                        if big_brd[2][piece2[0]][piece2[1]][2]=="u1":
                            plus_point_moves.append([piece2[0]+2, piece2[1], "u1"])
                        if big_brd[2][piece2[0]][piece2[1]][2]=="l1":
                            plus_point_moves.append([piece2[0], piece2[1]+2, "l1"])   
                        if big_brd[2][piece2[0]][piece2[1]][2]=="r1":
                            plus_point_moves.append([piece2[0], piece2[1]-2, "r1"])  

                        if big_brd[2][piece2[0]][piece2[1]][2]=="dl1":
                            plus_point_moves.append([piece2[0]-1, piece2[1]-1, "r1"])
                        if big_brd[2][piece2[0]][piece2[1]][2]=="dr1":
                            plus_point_moves.append([piece2[0]-1, piece2[1]+1, "l1"])
                        if big_brd[2][piece2[0]][piece2[1]][2]=="ul1":
                            plus_point_moves.append([piece2[0]+1, piece2[1]-1, "r1"])   
                        if big_brd[2][piece2[0]][piece2[1]][2]=="ur1":
                            plus_point_moves.append([piece2[0]+1, piece2[1]+1, "l1"])  

                        if big_brd[2][piece2[0]][piece2[1]][2]=="ld1":
                            plus_point_moves.append([piece2[0]+1, piece2[1]+1, "u1"])
                        if big_brd[2][piece2[0]][piece2[1]][2]=="ru1":
                            plus_point_moves.append([piece2[0]-1, piece2[1]-1, "d1"])
                        if big_brd[2][piece2[0]][piece2[1]][2]=="lu1":
                            plus_point_moves.append([piece2[0]-1, piece2[1]+1, "d1"])   
                        if big_brd[2][piece2[0]][piece2[1]][2]=="rd1":
                            plus_point_moves.append([piece2[0]+1, piece2[1]-1, "u1"])          
        if piece[2]=='K':
            kill_option=big_brd[2][piece[0]][piece[1]]
            for move in big_brd[4]:
                temp=[0, 0]
                if move[2][0]=='u':
                    temp[0]=move[0]-int(move[2][1])
                    temp[1]=move[1]
                if move[2][0]=='d':
                    temp[0]=move[0]+int(move[2][1])
                    temp[1]=move[1]    
                if move[2][0]=='l':
                    temp[1]=move[1]-int(move[2][1])
                    temp[0]=move[0] 
                if move[2][0]=='r':
                    temp[1]=move[1]+int(move[2][1])
                    temp[0]=move[0]       
                if kill_option[0]=='d':
                    if temp[0]==piece[0]-1 and temp[1]==piece[1]:
                        plus_point_moves.append(move)
                        
                if kill_option[0]=='u':
                    if temp[0]==piece[0]+1 and temp[1]==piece[1]:
                        plus_point_moves.append(move)
                        
                if kill_option[0]=='r':
                    if temp[0]==piece[0] and temp[1]==piece[1]-1:
                        plus_point_moves.append(move)
                        
                if kill_option[0]=='l':
                    if temp[0]==piece[0] and temp[1]==piece[1]+1:
                        plus_point_moves.append(move) 
                        
    print(plus_point_moves)
    # For each of our shortlisted moves, simulate making that move, and score them
    best_score=-1
    if len(plus_point_moves)!=0:
        for move in plus_point_moves:
            temp=copy.deepcopy(big_brd)
            if move[2][0]=='u':
                tup_move=((move[0], move[1]), (move[0]-int(move[2][1]), move[1]))
            if move[2][0]=='d':
                tup_move=((move[0], move[1]), (move[0]+int(move[2][1]), move[1]))   
            if move[2][0]=='l':
                tup_move=((move[0], move[1]), (move[0], move[1]-int(move[2][1])))
            if move[2][0]=='r':       
                tup_move=((move[0], move[1]), (move[0], move[1]+int(move[2][1])))
            temp[0][tup_move[0][0]][tup_move[0][1]]='-'
            temp[0][tup_move[1][0]][tup_move[1][1]]='O'
            # Check each direction to see if we can take a piece
            # Use try here to avoid index errors
            try:
                if temp[0][tup_move[1][0]-1][tup_move[1][1]]=='@':
                    if temp[0][tup_move[1][0]-2][tup_move[1][1]]=='O':
                        temp[0][tup_move[1][0]-1][tup_move[1][1]]='-'
            except:
                pass
            try:        
                if temp[0][tup_move[1][0]+1][tup_move[1][1]]=='@':
                    if temp[0][tup_move[1][0]+2][tup_move[1][1]]=='O':
                        temp[0][tup_move[1][0]+1][tup_move[1][1]]='-'
            except:
                pass
            try:      
                
                if temp[0][tup_move[1][0]][tup_move[1][1]-1]=='@':
                    if temp[0][tup_move[1][0]][tup_move[1][1]-2]=='O':
                        temp[0][tup_move[1][0]][tup_move[1][1]-1]='-'
            except:
                pass
            try:        
                if temp[0][tup_move[1][0]][tup_move[1][1]+1]=='@':
                    if temp[0][tup_move[1][0]][tup_move[1][1]+2]=='O':
                        temp[0][tup_move[1][0]][tup_move[1][1]+1]='-'
            except:    
                pass        
            # Once we have a proper board, initialise the board, then score it        
            temp=Initialise_Board(temp[0], 'O')
            temp_score=score_position(temp)
            # If the score is the highest yet, mark that, and store the move
            if temp_score>best_score:
                
                best_move=tup_move
                best_score=temp_score
                print("best=")
                print_brd(temp[0])
                print_brd(temp[1])
                print_brd(temp[2])
            #update(temp, tup_move)
print("ready!")            


# In[17]:


# funtion to score the centre control of the player
# Does so by increasing the score based on how close they are to the centre
def analyse_centre_control(big_brd):
    
    score=0
    for piece in big_brd[5]:
        temp=piece[0]
        temp2=piece[1]
        if temp>3:
            temp=7-temp
        if temp2>3:
            temp2=7-temp2
        score+=(temp+temp2)**2
    for piece in big_brd[6]:
        temp=piece[0]
        temp2=piece[1]
        if temp>3:
            temp=7-temp
        if temp2>3:
            temp2=7-temp2
        score-=(temp+temp2)**2
        
    return score    
        


# In[48]:


# function to score the quality of the structures within the board (the general formation)
# Does so by checking for proximity of pieces, and increasing score based off of how close they are, and how many other pieces
# are close by
def analyse_structure_quality(big_brd):
    score=0
    for piece in big_brd[5]:
        mod=0
        for piece2 in big_brd[5]:
            if abs(piece[0]-piece2[0])+abs(piece[1]-piece2[1])<3:
                score+=(3-abs(piece[0]-piece2[0]))**2+(3-abs(piece[1]-piece2[1]))**2+mod
                mod+=1
    for piece in big_brd[6]:
        mod=0
        for piece2 in big_brd[5]:
            if abs(piece[0]-piece2[0])+abs(piece[1]-piece2[1])<3:
                score-=(3-abs(piece[0]-piece2[0])+abs(piece[1]-piece2[1])+mod)**2
                mod+=1            
    return score            


# In[37]:


# function to score the relative positioning of the player to the opponent, based off of their potential to threaten the
# opponent in meaningful ways
def analyse_aggro(big_brd):
    score=0
    for row in big_brd[2]:
        for piece in row:
            if piece!='-':
                score+=(3-int(piece[-1]))**2
    for row in big_brd[1]:            
        for piece in row:
            if piece!='-':
                score-=(3-int(piece[-1]))**2
    return score        


# In[45]:


# function to combine all the scoring functions, with tweakable mods which control the significance of each function
def score_position(big_brd):
    #print(big_brd)
    score=0
    centre_adjuster=3
    struct_adjuster=1
    aggro_adjuster=10
    print(analyse_centre_control(big_brd))
    print(analyse_structure_quality(big_brd))
    print(analyse_aggro(big_brd))
    score=analyse_centre_control(big_brd)*centre_adjuster+analyse_structure_quality(big_brd)*struct_adjuster    +aggro_adjuster*analyse_aggro(big_brd)
    return score


# In[ ]:









class Player:

    colour = ''
    opponent_colour = ''
    pieces_remaining = 0
    board = []
    allied_pieces = []
    enemy_pieces = []

    #creates empty board
    #8 can be changed with MAX_BOARD
    for row in range(8):
        board.append(['-','-','-','-','-','-','-','-'])

    #init function which sets up the player colour
    def __init__(self, colour):
        self.colour = colour
        if colour == '0':
            self.opponent_colour = '@'
        else:
            self.opponent_colour = '0'
        #maybe keep track of heuristic here and constantly update it within action()

    #action function which returns the next move
    def action(self, turns):
        #this function assumes that place_heuristic and row_heuristic return in the same form as their respective moves
        # placement phase
        if turns <= 24:
            #where move = (heuristic value, position)
            move = (0, (0, 0))
            for row in range(len(self.board)):
                for col in range(len(row)):
                    if self.board[col][row] == '-':
                        new_heuristic = place_heuristic(self, col, row)
                        if new_heuristic[0] > place_heuristic[0]:
                            # heuristic[0] = new_heuristic
                            # heuristic[1][0] = col
                            # heuristic[1][1] = row
                            move = new_heuristic
        # movement phase
        else:
            #where move = (heuristic value, next position, previous position)
            move = (0, (0, 0), (0, 0))
            for row in range(len(self.board)):
                for col in range(len(row)):
                    if self.board[col][row] == self.colour:
                        new_heuristic = move_heuristic(col, row)
                        if new_heuristic > move_heuristic[0]:
                            # heuristic[0] = new_heuristic[0]
                            # heuristic[1][0] = new_heuristic[2][0]
                            # heuristic[1][1] = new_heuristic[2][1]
                            # heuristic[2][0] = col
                            # heuristic[2][1] = row
                            move = new_heuristic
            #need to make sure to change piece that is being moved inside else
            update_kill_piece(self, self.colour, move[2][0], move[2][1])
            self.board[move[2][0]][move[2][1]] = '-'

        #once best move chosen, save it in internal board and return move
        update_place_piece(self, self.colour, move[1][0], move[1][1])
        self.board[move[1][0]][move[1][1]] = self.colour
        return (move[1][0], move[1][1])


    #update function which updates the self board with next action
    def update(self, action):
        # if turn has been made (not None)
        if isinstance(action, tuple):
            # if in movement phase
            if any(isinstance(i, tuple) for i in action):
                x1 = action[0][0]
                y1 = action[0][1]
                x2 = action[1][0]
                y2 = action[1][1]
                # update internal board with opponents movement
                self.board[x1][y1] = '-'
                self.board[x2][y2] = self.colour
            # else in placement phase
            else:
                x = action[0]
                y = action[1]
                # update internal board with opponents placement
                self.board[x][y] = self.colour
                update_place_piece(self, self.opponent_colour, x, y)
            # check if any pieces eaten
            pieces_eaten = adj_pieces_eaten(self, (x2, y2))
            if pieces_eaten:
                for piece in pieces_eaten:
                    update_kill_piece(self, self.board[piece[0]][piece[1]], piece[0], piece[1])
                    self.board[piece[0]][piece[1]] = '-'

    def adj_pieces_eaten(self, position):

        board = self.board
        players = [self.colour, self.opponent_colour]
        corner = 'X'

        right = position[0] + 1
        left = position[0] - 1
        up = position[1] - 1
        down = position[1] + 1

        pieces_eaten = []

        #iterate for 2 cases, player piece eaten or opponent
        for player in players:
            if player == self.colour:
                opponent = self.opponent_colour
            else:
                opponent = self.colour
            # check position in bounds and occupied by opponent
            if right + 1 < len(board[0]):
                if (board[right][position[1]] == opponent) and \
                        ((board[right + 1][position[1]] == player) or (board[right + 1][position[1]] == corner)):
                    pieces_eaten.append((right, position[1]))
            if left - 1 >= 0:
                if (board[left][position[1]] == opponent) and \
                        ((board[left - 1][position[1]] == player) or (board[left - 1][position[1]] == corner)):
                    pieces_eaten.append((left, position[1]))
            if down + 1 < len(board):
                if (board[position[0]][down] == opponent) and \
                        ((board[position[0]][down + 1]) == player) or (board[position[0]][down + 1]) == corner)):
                    pieces_eaten.append((position[0], down))
            if up - 1 >= 0:
                if (board[position[0]][up] == opponent) and \
                        ((board[position[0]][up - 1]) == player) or (board[position[0]][up - 1]) == corner)):
                    pieces_eaten.append((position[0], up))
        return pieces_eaten

    def adj_pieces_threatened(self, position):

        board = self.board
        players = [self.colour, self.opponent_colour]
        corner = 'X'
        empty = '-'

        right = position[0] + 1
        left = position[0] - 1
        up = position[1] - 1
        down = position[1] + 1

        pieces_threatened = []

        #iterate for 2 cases, player piece eaten or opponent
        for player in players:
            if player == self.colour:
                opponent = self.opponent_colour
            else:
                opponent = self.colour
            # check position in bounds and occupied by opponent
            if right + 1 < len(board[0]):
                if (board[right][position[1]] == opponent) and (board[right + 1][position[1]] == empty):
                    pieces_threatened.append((right, position[1]))
            if left - 1 >= 0:
                if (board[left][position[1]] == opponent) and (board[left - 1][position[1]] == empty):
                    pieces_threatened.append((left, position[1]))
            if down + 1 < len(board):
                if (board[position[0]][down] == opponent) and (board[position[0]][down + 1]) == empty):
                    pieces_threatened.append((position[0], down))
            if up - 1 >= 0:
                if (board[position[0]][up] == opponent) and (board[position[0]][up - 1]) == empty):
                    pieces_threatened.append((position[0], up))
        return pieces_threatened

    def place_heuristic(self, col, row):
        board = self.board
        player = self.colour
        opponent = self.opponent_colour
        big_brd = Initialise_Board(board, player)
        score = 0

        # check if any opponent pieces eaten in move
        pieces_eaten = adj_pieces_eaten(self, (col, row))
        if pieces_eaten:
            for piece in pieces_eaten:
                if board[piece[0]][piece[1]] == opponent:
                    score += 20
                elif board[piece[0]][piece[1]] == player:
                    score -= 30

        #check if any opponent pieces threatened by move
        pieces_threatened = adj_pieces_threatened(self, (col, row))
        if pieces_threatened:
            for piece in pieces_threatened:
                if board[piece[0]][piece[1]] == opponent:
                    score += 5
                elif board[piece[0]][piece[1]] == player:
                    score -= 10

        #suppose check if move endangers kills our piece but might be redundant because of elif in pieces eaten
        if move_unsafe(self, col, row):
            score -= 30

        #check if move aids center control
        cent_score = analyse_aggro(big_brd)
        #add factored cent_score into overall score
        score += cent_score / 8

        #check if move aids structure quality
        struct_score = analyse_structure_quality(big_brd)
        # add factored cent_score into overall score
        score += struct_score / 20

        move = (score, (col, row))
        return move

def move_unsafe(self, col, row):
        board = self.board
        opponent = self.opponent_colour
        corner = 'X'

        right = col + 1
        left = col - 1
        up = row - 1
        down = row + 1

        if (right < len(board[0])) and (left >= 0):
            if ((board[right][row] == opponent) or (board[right][row] == corner)) and \
                    ((board[left][row] == opponent) or (board[left][row] == corner)):
                return True
        if (down < len(board[0])) and (up >= 0):
            if ((board[down][col] == opponent) or (board[down][col] == corner)) and \
                    ((board[up][col] == opponent) or (board[up][col] == corner)):
                return True
        else:
            return False

    def kill_move(self, col, row):
        board = self.board
        player = self.colour
        opponent = self.opponent_colour
        corner = 'X'

        right = col + 1
        left = col - 1
        up = row - 1
        down = row + 1

        if (right < len(board[0])) and (left >= 0):
            if ((board[right][row] == opponent) or (board[right][row] == corner)) and \
                    ((board[left][row] == opponent) or (board[left][row] == corner)):
                return True
        if (down < len(board[0])) and (up >= 0):
            if ((board[down][col] == opponent) or (board[down][col] == corner)) and \
                    ((board[up][col] == opponent) or (board[up][col] == corner)):
                return True
        else:
            return False

    def update_place_piece(self, player, col, row):
        if player == self.colour:
            self.allied_pieces.append((col, row))
        else:
            self.enemy_pieces.append((col, row))

    def update_kill_piece(self, player, col, row):
        if player == self.colour:
            self.allied_pieces.remove((col, row))
        else:
            self.allied_pieces.remove((col, row))
