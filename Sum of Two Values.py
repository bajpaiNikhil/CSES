

a,b=map(int,input().split())

n=list(map(int,input().split()))[:a]

d={}


for i in range(a):
    if b-n[i] in d:
        print(i+1,d[b-n[i]]+1)
        quit()
    else:
        d[n[i]]=i
print("IMPOSSIBLE")

