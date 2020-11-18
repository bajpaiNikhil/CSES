

#
# n,m,k=map(int,input().split())
#
# rooma=list(map(int,input().split()))
# room=list(map(int,input().split()))
#
# rooma.sort()
# room.sort()
#
# i=0
# j=0
# count=0
# # print(rooma)
# # print(room)
#
# while (i<n and j <m):
#     if rooma[i]+k<room[j]:
#         i+=1
#     elif rooma[i]-k>room[j]:
#         j+=1
#     else:
#         print(rooma[i],room[j])
#         i+=1
#         j+=1
#         count+=1
#

# print(count)

#
# print(count)









#
# n= [3]
# m= [3]
# q=4
#
# count=0
# if len(n)==1:
#     if n[0]<q<=m[0] or m[0]==q :
#         print(1)
#     else:
#         print(0)
# else:
#     for i,j in zip(n,m):
#         if i<=q<=j:
#             count+=1
#     print(count)

#
# n = [4,2,1,3]
# n.sort()
# min=float('inf')
# for i in range(len(n)-1):
#     current=n[i+1]-n[i]
#     #print(current)
#     if current<=min:
#         min=current
# ans=[]
# for i in range(len(n)-1):
#     if n[i+1]-n[i]==min:
#         ans.append([n[i],n[i+1]])
# print(ans)


# n=[9]
#
# res=int("".join(map(str,n)))
#
# print(res)
#
# d=res+1
# print(d)
#
# l=list(map(int,str(d)))
# print(l)

















































