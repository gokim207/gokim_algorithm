chess = []
queens = 0
for i in range(8):
    chess.append(list(input()))
    
for i in range(8):
    if chess[i].count('*') >= 2:
        print('invalid')
        exit()
    cross = [0,0,0,0,0,0,0,0]
    for j in range(8):
        cross[j] = chess[j][i]
        
    if cross.count('*')>=2:
        print('invalid')
        exit()

for i in range(8):
    for j in range(8):
        if chess[i][j] == '*':
            queens += 1
            dia = [0,0,0,0,0,0,0,0]
            dia2 = [0,0,0,0,0,0,0,0]            
            x = i+1
            y = j+1
            count = 0
            while x < 8 and y < 8:
                dia[count] = chess[x][y]
                x += 1
                y += 1
                count += 1
            
            if dia.count('*') >= 1:
                print('invalid')
                exit()
            x = i+1
            y = j-1
            count = 0
            while x < 8 and y >= 0:
                dia2[count] = chess[x][y]
                x+=1
                y -= 1
                count += 1
            if dia2.count('*') >=1:
                print('invalid')
                exit()
if queens != 8:
    print('invalid')
    exit()
print('valid')