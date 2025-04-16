a = input()
b= list(map(int,input().split()))
d= set(b) # 중복 제거
max1=0
for i in range(12):
    
    # numbers
    if(a[i]=='Y' and i==0 and max1<b.count(1)+2):
        max1 = b.count(1)+2
    elif(a[i]=='Y' and i==1 and max1<b.count(2)*2+4):
        max1 = b.count(2)*2+4
    elif(a[i]=='Y' and i==2 and max1<b.count(3)*3+6):
        max1 = b.count(3)*3+6
    elif(a[i]=='Y' and i==3 and max1<b.count(4)*4+8):
        max1 = b.count(4)*4+8
    elif(a[i]=='Y' and i==4 and max1<b.count(5)*5+10):
        max1 = b.count(5)*5+10
    elif(a[i]=='Y' and i==5 and max1<b.count(6)*6+12):
        max1 = b.count(6)*6+12
        
    # four of a kind
    elif(a[i]=='Y' and i==6 and (b[0]==b[1] or b[1]==b[2] or b[0]==b[2])):
        if(b[0]==b[1] and max1<b[0]*4):
            max1 = b[0]*4
        elif(b[1]==b[2] and max1<b[2]*4):
            max1 = b[2]*4
        elif(b[0]==b[2] and max1<b[2]*4):
            max1 = b[0]*4
            
    # full house
    elif(a[i]=='Y' and i==7 and (b[0]==b[1]==b[2] or b[0]==b[1] or b[0]==b[2] or b[1]==b[2])):
        if(b[0]==b[1]==b[2] and b[0]==6 and max1<28):
            max1 = 28
        elif(b[0]==b[1]==b[2] and b[0]!=6 and max1<b[0]*3+12):
            max1 = b[0]*3+12
            
        elif(b[0]==b[1]):
            if(b[0]>b[2] and max1<b[0]*3+b[2]*2):
                max1=b[0]*3+b[2]*2
            elif(b[0]<b[2] and max1<b[0]*2+b[2]*3):
                max1 = b[0]*2+b[2]*3
            
        elif(b[0]==b[2]):
            if(b[0]>b[1] and max1<b[0]*3+b[1]*2):
                max1=b[0]*3+b[1]*2
            elif(b[0]<b[1] and max1<b[0]*2+b[1]*3):
                max1 = b[0]*2+b[1]*3
            
        elif(b[1]==b[2]):
            if(b[1]>b[0] and max1<b[1]*3+b[0]*2):
                max1=b[1]*3+b[0]*2
            elif(b[1]<b[2] and max1<b[1]*2+b[0]*3):
                max1 = b[1]*2+b[0]*3
                
    # small straight
    elif(a[i]=='Y' and i==8 and len(d)>=3 and 6 not in d and max1<30):
        max1=30
        
    # large straight
    elif(a[i]=='Y' and i==9 and len(d)>=3 and 1 not in d and max1<30):
        max1=30
        
    # yacht
    elif(a[i]=='Y' and i==10 and b[0]==b[1]==b[2]):
        max1 = 50
        break
        
    # choice
    elif(a[i]=='Y' and i==11 and sum(b)+12>max1):
            max1 = sum(b)+12
            
print(max1)