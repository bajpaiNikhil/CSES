

n=int(input())
d=0
for i in range(1,n+1):
    #print(i)
    d=((i-1)*(i+4)*(i**2 - 3*i + 4))//2
    print(d)