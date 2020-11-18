


from collections import Counter
s=input()
d=Counter(s)
# print(d)
count=0
oddchar=""
for key,val in d.items():
    if val%2!=0:
        count+=1
        oddchar=key
# print(oddchar)
# print(count)
s=""
first=""
second=""
if ((count>1) or (count==1 and len(s)%2==0)):
    print("NO SOLUTION")
else:
    for keey,vaal in d.items():
        s=keey*(vaal//2)
        first=first+s
        second=s+second

    print(first+oddchar+second if count==1 else first+second)