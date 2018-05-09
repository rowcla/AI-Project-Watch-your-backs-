
# coding: utf-8

# In[31]:


Smp_Brd = []
Smp_Brd.append(['X','-','-','-','-','-','-','X'])
Smp_Brd.append(['-','-','-','-','-','-','-','-'])
Smp_Brd.append(['-','-','-','O','O','@','-','-'])
Smp_Brd.append(['-','-','O','-','-','@','-','-'])
Smp_Brd.append(['-','O','-','-','@','-','-','-'])
Smp_Brd.append(['-','-','@','-','O','@','-','-'])
Smp_Brd.append(['-','-','O','@','-','-','-','-'])
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
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])==0:
                big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]=0
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])==0:
                big_brd[1][int((piece2[1]+piece[1])/2)][piece[0]]=0
                
            if abs(piece[0]-piece2[0])==2 and abs(piece[1]-piece2[1])==1:
                if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]!=0:
                    big_brd[1][int((piece2[0]+piece[0])/2)][piece[1]]=1
                if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]!=0:    
                    big_brd[1][int((piece2[0]+piece[0])/2)][piece2[1]]=1
                    
            if abs(piece[1]-piece2[1])==2 and abs(piece[0]-piece2[0])==1:
                if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]!=0:
                    big_brd[1][piece[0]][int((piece2[1]+piece[1])/2)]=1
                if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]!=0:
                    big_brd[1][piece2[0]][int((piece2[1]+piece[1])/2)]=1
                    
            if abs(piece[0]-piece2[0])==3 and abs(piece[1]-piece2[1])==0:
                if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][int((piece2[0]+piece[0]+1)/2)][piece[1]]!=0:
                    big_brd[1][int((piece2[0]+piece[0]+1)/2)][piece[1]]=1
                if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][int((piece2[0]+piece[0]-1)/2)][piece2[1]]!=0:    
                    big_brd[1][int((piece2[0]+piece[0]-1)/2)][piece2[1]]=1
                    
            if abs(piece[1]-piece2[1])==3 and abs(piece[0]-piece2[0])==0:
                if big_brd[0][piece[0]][piece2[1]]!='O' and big_brd[1][piece[0]][int((piece2[1]+piece[1]+1)/2)]!=0:
                    big_brd[1][piece[0]][int((piece2[1]+piece[1]+1)/2)]=1
                if big_brd[0][piece2[0]][piece[1]]!='O' and big_brd[1][piece2[0]][int((piece2[1]+piece[1]-1)/2)]!=0:
                    big_brd[1][piece2[0]][int((piece2[1]+piece[1]-1)/2)]=1 
                    
                    
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
                if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][int((piece2[0]+piece[0]+1)/2)][piece[1]]!=0:
                    big_brd[2][int((piece2[0]+piece[0]+1)/2)][piece[1]]="d1"
                if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][int((piece2[0]+piece[0]-1)/2)][piece2[1]]!=0:    
                    big_brd[2][int((piece2[0]+piece[0]-1)/2)][piece2[1]]="u1"
                    
            if abs(piece[1]-piece2[1])==3 and abs(piece[0]-piece2[0])==0:
                if big_brd[0][piece[0]][piece2[1]]!='@' and big_brd[2][piece[0]][int((piece2[1]+piece[1]+1)/2)]!=0:
                    big_brd[2][piece[0]][int((piece2[1]+piece[1]+1)/2)]="r1"
                if big_brd[0][piece2[0]][piece[1]]!='@' and big_brd[2][piece2[0]][int((piece2[1]+piece[1]-1)/2)]!=0:
                    big_brd[2][piece2[0]][int((piece2[1]+piece[1]-1)/2)]="l1"                 
    print_brd(big_brd[1])
    move_list=[]
    priority_targets=[]
    for piece in Our_list:
        if piece[0]>min_edge:
            if big_brd[1][piece[0]-1][piece[1]]=='-' and big_brd[0][piece[0]-1][piece[1]]=='-':
                move_list.append(list(piece))
                move_list[-1].append("l1")
            if big_brd[0][piece[0]-1][piece[1]]=='@' or big_brd[0][piece[0]-1][piece[1]]=='O':
                if piece[0]>min_edge+1:
                    if big_brd[1][piece[0]-2][piece[1]]=='-' and big_brd[0][piece[0]-2][piece[1]]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("l2")
                        
        if piece[1]>min_edge:
            if big_brd[1][piece[0]][piece[1]-1]=='-' and big_brd[0][piece[0]][piece[1]-1]=='-':
                move_list.append(list(piece))
                move_list[-1].append("u1")
            if big_brd[0][piece[0]][piece[1]-1]=='@' or big_brd[0][piece[0]][piece[1]-1]=='O':
                if piece[1]>min_edge+1:
                    if big_brd[1][piece[0]][piece[1]-2]=='-' and big_brd[0][piece[0]][piece[1]-2]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("u2")
                        
        if piece[0]<max_edge:
            if big_brd[1][piece[0]+1][piece[1]]=='-' and big_brd[0][piece[0]+1][piece[1]]=='-':
                move_list.append(list(piece))
                move_list[-1].append("r1")
            if big_brd[0][piece[0]+1][piece[1]]=='@' or big_brd[0][piece[0]+1][piece[1]]=='O':
                if piece[0]>max_edge-1:
                    if big_brd[1][piece[0]+2][piece[1]]=='-' and big_brd[0][piece[0]+2][piece[1]]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("r2")
                        
        if piece[1]<max_edge:
            if big_brd[1][piece[0]][piece[1]+1]=='-' and big_brd[0][piece[0]][piece[1]+1]=='-':
                move_list.append(list(piece))
                move_list[-1].append("d1")
            if big_brd[0][piece[0]][piece[1]+1]=='@' or big_brd[0][piece[0]][piece[1]+1]=='O':
                if piece[1]>max_edge-1:
                    if big_brd[1][piece[0]][piece[1]+2]=='-' and big_brd[0][piece[0]][piece[1]+2]=='-':
                        move_list.append(list(piece))
                        move_list[-1].append("d2")
        if big_brd[1][piece[0]][piece[1]]==1:
            for piece in Enemy_list:
                print()
                #if piece[0]
            priority_targets.append(list(piece))
            priority_targets[-1].append('S')
    for piece in Enemy_list:
        if big_brd[2][piece[0]][piece[1]][-1]=='1':
            priority_targets.append(list(piece))
            priority_targets[-1].append('K')
    print_brd(big_brd[1])
    print_brd(big_brd[2])
    print(priority_targets)
    print(move_list)

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
    for piece in big_brd[3]:
        if piece[2]='S':
            for move in big_brd[4]:
                

