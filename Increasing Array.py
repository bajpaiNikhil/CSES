

a=int(input())
n=list(map(int,input().split()))

count=0
current=0
for i in range(len(n)):

    if current>n[i]:
        count+=current-n[i]
    else:
        current=n[i]
print(count)
