



nlen,k=map(int,input().split())

n=list(map(int,input().split()))

n.sort()

count=0

m=len(n)-1
i=0
while(i <= m):
    #print(n[l],n[m])
    if n[i]+n[m]>k:
        m-=1
    else:
        i+=1
        m-=1
    count+=1
print(count)