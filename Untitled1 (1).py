
# coding: utf-8

# In[31]:


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


# In[65]:




def Initialise_Board(Board, Player):
    print_brd(Board)
    min_edge=0
    max_edge=7
    
    big_brd=[]
    big_brd.append(Board)
    big_brd.append([])
    for i in range(8):
        big_brd[1].append([])
        for j in range(8):
            big_brd[1][i].append('-')
    big_brd.append([])
    for i in range(8):
        big_brd[2].append([])
        for j in range(8):
            big_brd[2][i].append('-')
    
    Enemy_list=[]
    Our_list=[]
    i=0
    for row in big_brd[0]:
        j=0
        for col in row:
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
    for piece in Enemy_list:
        for piece2 in Enemy_list:
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])=="u0":
                big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]=0
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])=="l0":
                big_brd[1][int((piece2[1]+piece[1])/2)][piece[0]]=0
                
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])==1:
                if piece2[0]>piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]!=0:
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]="ur1"
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]!=0:    
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]="dl1"
                if piece2[0]<piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]!=0:
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]="dr1"
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]!=0:    
                        big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]="ul1"

                        
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])==1:
                if piece2[1]>piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]="lu1"
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]="rd1"
                if piece2[1]<piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]="ru1"
                    if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]="ld1"       
                    
            if abs(piece[0]-piece2[0])==3 and abs(piece[1]-piece2[1])==0:
                if big_brd[0][int((piece2[0]+piece[0]-1)/2)][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0]+1)/2)][piece[1]]!=0:
                    big_brd[1][int((piece2[0]+piece[0]+1)/2)][piece[1]]="d1"
                if big_brd[0][int((piece2[0]+piece[0]+1)/2)][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0]-1)/2)][piece2[1]]!=0:    
                    big_brd[1][int((piece2[0]+piece[0]-1)/2)][piece2[1]]="u1"
                    
            if abs(piece[1]-piece2[1])==3 and abs(piece[0]-piece2[0])==0:
                if big_brd[0][piece[0]][int((piece2[1]+piece[1]-1)/2)]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1]+1)/2)]!=0:
                    big_brd[1][piece[0]][int((piece2[1]+piece[1]+1)/2)]="r1"
                if big_brd[0][piece2[0]][int((piece2[1]+piece[1]+1)/2)]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1]-1)/2)]!=0:
                    big_brd[1][piece2[0]][int((piece2[1]+piece[1]-1)/2)]="l1"
                    
                    
    for piece in Our_list:
        for piece2 in Our_list:
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])=="u0":
                big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]=0
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])=="l0":
                big_brd[2][int((piece2[1]+piece[1])/2)][piece[0]]=0
                
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])==1:
                if piece2[0]>piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]!=0:
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]="ur1"
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]]!=0:    
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]]="dl1"
                if piece2[0]<piece[0]:
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]!=0:
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece[1]]="dr1"
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]]!=0:    
                        big_brd[2][int((piece2[0]+piece[0])/2)][piece2[1]]="ul1"

                        
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])==1:
                if piece2[1]>piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)]="lu1"
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)]="rd1"
                if piece2[1]<piece[1]:
                    if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[2][piece[0]][int((piece2[1]+piece[1])/2)]="ru1"
                    if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)]!=0:
                        big_brd[2][piece2[0]][int((piece2[1]+piece[1])/2)]="ld1"       
                    
            if abs(piece[0]-piece2[0])==3 and abs(piece[1]-piece2[1])==0:
                if big_brd[0][int((piece2[0]+piece[0]-1)/2)][piece[1]]!='@' and big_brd[2][int((piece2[0]+piece[0]+1)/2)][piece[1]]!=0:
                    big_brd[2][int((piece2[0]+piece[0]+1)/2)][piece[1]]="d1"
                if big_brd[0][int((piece2[0]+piece[0]+1)/2)][piece2[1]]!='@' and big_brd[2][int((piece2[0]+piece[0]-1)/2)][piece2[1]]!=0:    
                    big_brd[2][int((piece2[0]+piece[0]-1)/2)][piece2[1]]="u1"
                    
            if abs(piece[1]-piece2[1])==3 and abs(piece[0]-piece2[0])==0:
                if big_brd[0][piece[0]][int((piece2[1]+piece[1]-1)/2)]!='@' and big_brd[2][piece[0]][int((piece2[1]+piece[1]+1)/2)]!=0:
                    big_brd[2][piece[0]][int((piece2[1]+piece[1]+1)/2)]="r1"
                if big_brd[0][piece2[0]][int((piece2[1]+piece[1]+1)/2)]!='@' and big_brd[2][piece2[0]][int((piece2[1]+piece[1]-1)/2)]!=0:
                    big_brd[2][piece2[0]][int((piece2[1]+piece[1]-1)/2)]="l1"                 
    print_brd(big_brd[1])
    move_list=[]
    priority_targets=[]
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
        if big_brd[1][piece[0]][piece[1]][-1]=='1':
            
            priority_targets.append(list(piece))
            priority_targets[-1].append('S')
    for piece in Enemy_list:
        if big_brd[2][piece[0]][piece[1]][-1]=='1':
            priority_targets.append(list(piece))
            priority_targets[-1].append('K')
    
    print_brd(big_brd[2])
    big_brd.append(priority_targets)
    big_brd.append(move_list)
    print(priority_targets)
    print(move_list)
    make_move(big_brd)
    print("done!")
Initialise_Board(Smp_Brd, 'O')        


# In[64]:


def print_brd(Board):
    for line in Board:
        for col in line:
            print(str(col)[-1], end=' ')
        print()    
    print()    


# In[ ]:


def analyse_aggro(big_brd):
    


# In[ ]:


def make_move(big_brd):
    plus_point_moves=[]
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
                if piece2[2]=='K':
                    if kill_option[0]=='d':
                        if piece2[0]==piece[0]+1 and piece2[1]==piece[1]:
                            plus_point_moves.append(piece2)
                        if kill_option[1]=='l':
                            if piece2[0]==piece[0]-1 and piece2[1]==piece[1]-1:
                                plus_point_moves.append(piece2)
                        elif piece2[0]==piece[0]-1 and piece2[1]==piece[1]+1:
                            plus_point_moves.append(piece2)
                    if kill_option[0]=='u':
                        if piece2[0]==piece[0]-1 and piece2[1]==piece[1]:
                            plus_point_moves.append(piece2)
                        if kill_option[1]=='l':
                            if piece2[0]==piece[0]+1 and piece2[1]==piece[1]-1:
                                plus_point_moves.append(piece2)
                        elif piece2[0]==piece[0]+1 and piece2[1]==piece[1]+1:
                            plus_point_moves.append(piece2)        
                    if kill_option[0]=='r':
                        if piece2[0]==piece[0] and piece2[1]==piece[1]+1:
                            plus_point_moves.append(piece2)
                        if kill_option[1]=='u':
                            if piece2[0]==piece[0]-1 and piece2[1]==piece[1]-1:
                                plus_point_moves.append(piece2)
                        elif piece2[0]==piece[0]+1 and piece2[1]==piece[1]-1:
                            plus_point_moves.append(piece2)     
                    if kill_option[0]=='l':
                        if piece2[0]==piece[0] and piece2[1]==piece[1]-1:
                            plus_point_moves.append(piece2) 
                        if kill_option[1]=='u':
                            if piece2[0]==piece[0]-1 and piece2[1]==piece[1]+1:
                                plus_point_moves.append(piece2)
                        elif piece2[0]==piece[0]+1 and piece2[1]==piece[1]+1:
                            plus_point_moves.append(piece2)     
                            
    print(plus_point_moves)       


class Player:

    colour = ''
    opponent_colour = ''
    pieces_remaining = 0
    board = []
    board_coor = []

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
                    new_heuristic = place_heuristic(col, row)
                    if new_heuristic[0] > place_heuristic[0]:
                        # heuristic[0] = new_heuristic
                        # heuristic[1][0] = col
                        # heuristic[1][1] = row
                        move = new_heuristic
        # movement phase
        else:
            #where move = (heuristic value, next position, previous position)
            move = (0, (0, 0), (0, 0))
            for row in self.board_coor:
                for col in row:
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
            self.board[move[2][0]][move[2][1]] = '-'

        #once best move chosen, save it in internal board and return move
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
            # check if any pieces eaten
            pieces_eaten = adj_pieces_eaten(self, (x2, y2))
            if pieces_eaten != None:
                for piece in pieces_eaten:
                    self.board[piece[0]][piece[1]] = '-'

    def adj_pieces_eaten(self, position):

        board = self.board
        player = self.colour
        opponent = self.opponent_colour

        right = position[0] + 1
        left = position[0] - 1
        up = position[1] - 1
        down = position[1] + 1

        pieces_eaten = []

        # check position in bounds and occupied by opponent
        if right + 1 < len(board[0]):
            if (board(right, position[1]) == opponent) and (board(right + 1, position[1]) == player):
                pieces_eaten.append((right, position[1]))
        if left - 1 >= 0:
            if (board(left, position[1]) == opponent) and (board(left - 1, position[1]) == player):
                pieces_eaten.append((left, position[1]))
        if down + 1 < len(board):
            if (board(position[0], down) == opponent) and (board(position[0], down + 1) == opponent):
                pieces_eaten.append((position[0], down))
        if up - 1 >= 0:
            if (board(position[0], up) == opponent) and (board(position[0], up - 1) == opponent):
                pieces_eaten.append((position[0], up))
        return pieces_eaten


