


t=int(input())
for t in range(t):
    n,m=map(int,input().split())

    if n<m:
       n,m=m,n
    elif n>2*m:
        print("NO")
    else:
        n%=3
        m%=3
        if n<m:
            n,m=m,n
        elif (n==2 and m==1 ) or (n==m and m==0):
            print("YES")
        else:
            print("NO")
