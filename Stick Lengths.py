#
# t=int(input())
# n=list(map(int,input().split()))
# d=len(n)
# e=d//2
# print(n[e:],n[:e])
#
#

# if d%2==0:
#     print(((sum(n[e:])-sum(n[:e]))))
# else:
#     print((sum(n[e-1:])-sum(n[e+1:])))



t=int(input())
for t in range(t):
    a=int(input())
    n=list(map(int,input().split()))[:a]
    m=list(map(int,input().split()))[:a]

    minn=min(n)
    minm=min(m)
    dec=0
    for i in range(a):
        dec+=max(n[i]-minn,m[i]-minm)

    print(dec)





# n=[1, 2, 3, 4, 5]
# m=[5, 4, 3, 2, 1]
# l=5
# n.sort()
# m.sort()
# print(n)
# print(m)
# # print(m)
# midn=l//2
# midm=l//2
#
# ansn=sum(n[midn+l%2:])-sum(n[:midn])
# print(ansn)
# ansm=sum(m[midm + l%2:])-sum(m[:midm])
# print(ansm)
#
# print(ansn+ansm)












