
t=int(input())

for t in range(t):
    n,m=map(int,input().split())
    d=max(n,m)

    e=(n-m)*(-1)**d+d*d-d+1
    print(e)