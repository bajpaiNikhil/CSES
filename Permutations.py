

n=int(input())
odd=[]
even=[]
if n==1:
    print(1)
elif n<4:
    print("NO SOLUTION")
else:
    for i in range(1,n+1):
        if i%2!=0:
            odd.append(i)
        else:
            even.append(i)
    print(str(even+odd)[1:-1].replace(", "," "))