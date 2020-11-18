



n=int(input())
arrival=[]
leave=[]

for i in range(n):
    x,y=map(int,input().split())
    arrival.append(x)
    leave.append(y)
arrival.sort()
leave.sort()
ii,j=0,0
count=0
maxcount=0
while(ii<n and j<n):
    if arrival[ii]<leave[j]:
        count+=1
        ii+=1
    else:
        count-=1
        j+=1
    if maxcount<count:
        maxcount=count
print(maxcount)
