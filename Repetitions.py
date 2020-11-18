


s=input()

count=0
current=''
maxi=0
for i in s:
    if i==current:
        count+=1
    else:
        count=1
        current=i
    maxi=max(count,maxi)
print(maxi)