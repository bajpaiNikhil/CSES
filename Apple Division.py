


n=int(input())
l=list(map(int,input().split()))
s=sum(l)
def mindiff(s,l):
    if len(l)==1:
        return abs(s-2*l[0])
    else:
        m=abs(s-2*l[0])
        for i in range(1,len(l)):
            m=min(m,abs(mindiff(s-2*l[i],l[:i])))
        return m
print(mindiff(s,l))