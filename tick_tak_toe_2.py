import numpy as np

def Column_Check(lst):

    player1 = 0
    player2 = 0
    for i in lst:
        if i == 'O':
            player1+=1
        if i == 'X':
            player2+=1
    if player1 == 3:
        return 'O'
    if player2 == 3:
        return 'X'
    else:
        return None

def Check_Win(array):

    checker1_col = []
    checker2_col = []
    checker3_col = []
    checker1_row = []
    checker2_row = []
    checker3_row = []
    diagonal_1 = []
    diagonal_2 = []


    for i in range(len(array)):
        for j in range(len(array)):
            if j == 0:
                checker1_col.append(array[i][j])
            elif j == 1:
                checker2_col.append(array[i][j])
            elif j == 2:
                checker3_col.append(array[i][j])
            if i == 0 :
                checker1_row.append(array[i][j])
            elif i == 1 :
                checker2_row.append(array[i][j])
            elif i == 2 :
                checker3_row.append(array[i][j])
            if i==0 and j== 0:
                diagonal_1.append(array[i][j])
            elif i==1 and j==1:
                diagonal_1.append(array[i][j])
            elif i==2 and j ==2:
                diagonal_1.append(array[i][j])
            if i==0 and j ==2:
                diagonal_2.append(array[i][j])
            elif i ==1 and j == 1:
                diagonal_2.append(array[i][j])
            elif i==2 and j ==0:
                diagonal_2.append(array[i][j])


    x1 = Column_Check(checker1_col)
    if x1 == 'O':
        return '1'
    elif x1 == 'X':
        return '2'

    x2 = Column_Check(checker2_col)
    if x2 == 'O':
        return '1'
    elif x2 == 'X':
        return '2'

    x3 = Column_Check(checker3_col)
    if x3 == 'O':
        return '1'
    elif x3 == 'X':
        return '2'

    x4 = Column_Check(checker1_row)
    if x4 == 'O':
        return '1'
    elif x4 == 'X':
        return '2'

    x5 = Column_Check(checker2_row)
    if x5 == 'O':
        return '1'
    elif x5 == 'X':
        return '2'

    x6 = Column_Check(checker3_row)
    if x6 == 'O':
        return '1'
    elif x6 == 'X':
        return '2'

    x7 = Column_Check(diagonal_1)
    if x7 == 'O':
        return '1'
    elif x7 == 'X':
        return '2'

    x8 = Column_Check(diagonal_2)
    if x8 == 'O':
        return '1'
    elif x8 == 'X':
        return '2'
   
def tick_tak_toe():
    array = np.empty( shape=(3,3), dtype='str')
    for i in range(0,3):
        for j in range(0,3):
            array[i][j] = '-'

    print(array)
    draw = 0
    win = False
    while  win!= True:
        filled = False
        while filled != True:
            check = False
            while check != True:
                player1 = input('Player 1: Choose Your place \nEntre row and column: ')
                if player1 =='12'or player1 == '13' or player1 == '11' or player1 == '22' or player1== '21'or player1 == '23' or player1 == '33'or player1 == '32'or player1 == '31':
                    check = True
                else:
                    print('Invalid Try Again')
            
            i = int(player1[0])-1
            j = int(player1[1])-1
            if array[i][j] == '-':
                array[i][j] = 'O'
                draw += 1
                filled = True
            else:
                print('\n')
                print('choose another place, already filled')
                print('\n')
        print(array)
        if draw == 5:
            win = True
            continue
        
        X = Check_Win(array)

        if X == '1':
            print('\n')
            print('Player 1 Win')
            win = True
            continue

        elif X == '2':
            print('\n')
            print('Player 2 win')
            win = True
            continue

        filled2 = False
        while filled2 != True:
            check1 = False
            while check1 != True:
                player2 = input('Player 2: Choose Your place \n Entre row and column: ')
                if player2 =='12'or player2 == '13' or player2 == '11' or player2 == '22' or player2== '21'or player2 == '23' or player2 == '33'or player2 == '32'or player2 == '31':
                    check1 = True
                else:
                    print('Invalid Try Again')
            x = int(player2[0])-1
            y = int(player2[1])-1
            if array[x][y] == '-':
                array[x][y] = 'X'
                filled2 = True
            else:
                print('\n')
                print('choose another place, already filled')
                print('\n')
        print(array)
        Y = Check_Win(array)

        if Y == '1':
            print('\n')
            print('Player 1 Win')
            win = True
            continue
        
        elif Y == '2':
            print('\n')
            print('Player 2 win')
            win = True
            continue
    return 'Match end'

        


print(tick_tak_toe())

