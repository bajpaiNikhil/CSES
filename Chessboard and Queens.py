

reserved = [[c == '*' for c in input()]for _ in range(8)]
diagnol_1=[0]*15
diagnol_2=[0]*15
cols=[0]*8
count=0

def queenCheck(y):

    global diagnol_1,diagnol_2,count,cols

    if y==8:
        count+=1
        return
    for x in range(8):
        if cols[x] or diagnol_1[x+y] or diagnol_2[x-y+7] or reserved[y][x]:
            continue
        cols[x]=diagnol_1[x+y]=diagnol_2[x-y+7]=1
        queenCheck(y+1)
        cols[x]=diagnol_1[x+y]=diagnol_2[x-y+7]=0

queenCheck(0)
print(count)

