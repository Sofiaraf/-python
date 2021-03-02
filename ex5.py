import random

rows = int(input('Give me rows:'))
col = int(input('Give me columns:'))
tr = 0
list_pos = rows*col
S = list_pos//2
O = list_pos//2
if list_pos % 2 != 0:
    S = S + 1
ch=list()
for i in range(S):
    ch.append('S')
for i in range(O):
    ch.append('O')

for i in range(100):
    my_list=[]
    for k in range(rows):
        my_list.append([])
    for j in range(col):
            my_list[k].append([])

    for k in range(rows):
        for j in range(col):
            elem=random.choice(ch)
            my_list[k].append(elem)

            
    
    for k in range(rows):
        for j in range(col):
            if j <= col-3:
                if my_list[k][j] == 'S' and my_list[k][j+1] == 'O' and my_list[k][j+2] == 'S':
                    tr = tr + 1
            if i <= rows-3:
                if my_list[k][j] == 'S' and my_list[k+1][j] == 'O' and my_list[k+2][j] == 'S':
                    tr = tr + 1
            if i <= rows-3 and j <= col-3:
                if my_list[k][j] == 'S' and my_list[k+1][j+1] == 'O' and my_list[k+2][j+2] == 'S':
                    tr = tr + 1

av = tr/100
print("The average is :",av)

                
                
    
        
            
            
    