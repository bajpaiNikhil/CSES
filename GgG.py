
"""

    to find occurance of a element in a sorted array using binary search

"""
# n=[5,10,10,10,20,30]
# x=10
# low=0
# high=len(n)
# def fobs(n,x,low,high):
#
#     if low>high:
#         return -1
#     mid=(high-low)//2
#
#     if x>n[mid]:
#         return fobs(n,x,mid+1,high)
#     elif x<n[mid]:
#         return fobs(n,x,low,mid-1)
#     else:
#         if mid==0 or n[mid-1]!=n[mid]:
#             return mid
#         else:
#             return fobs(n,x,low,mid-1)
# print(fobs(n,x,low,high))



# while (low<=high):
#     mid=(high+low)//2
#
#     if n[mid]>x:
#         high=mid-1
#     elif n[mid]<x:
#         low=mid+1
#     else:
#         if mid==0 or n[mid-1]!=n[mid]:
#             print(mid)
#             break
#         else:
#             high=mid-1
#










"""
    to find the last occurance of the element in the array using binary search both recursive // itterative approch 
     
"""


# n=[5,10,10,10,20,20,30]
# x=5
# low=0
# high=len(n)

# def lobs(n,x,low,high):
#     mid=(high+low)//2
#
#     if x>n[mid]:
#         return lobs(n,x,mid+1,high)
#     elif x<n[mid]:
#         return lobs(n,x,low,mid-1)
#     else:
#         if mid==(len(n)-1) or n[mid]!=n[mid+1]:
#             return mid
#         else:
#             return lobs(n,x,mid+1,high)
# print(lobs(n,x,low,high))
#
# def lois(n,x,low,high):
#
#
#     while low<=high:
#         mid=(low+high)//2
#         if x>n[mid]:
#             low=mid+1
#         elif x<n[mid]:
#             high=mid-1
#         else:
#             if mid==(len(n)-1) or n[mid+1]!=n[mid]:
#                 return mid
#             else:
#                 low=mid+1
#
# print(lois(n,x,low,high))






"""to count the occuranse of a element in an array using binary search in a smart way instead of
 1 binary search we gonna use to binary searchs one to find the first occurance of a element and
  one to count the last occurance of the element then we will substract them and +1 to them to find our answer"""



#
# n=[5,10,10,10,10,20,20,30]
# #n=[0,0,0,1,1,1]
# x=10
# low=0
# s=len(n)
# high=s-1
# def fobs(n,x,low,high):
#     mid=(high+low)//2
#     if low>high:
#         return -1
#     if x>n[mid]:
#         return fobs(n,x,mid+1,high)
#     elif x<n[mid]:
#         return fobs(n,x,low,mid-1)
#     else:
#         if mid==0 or n[mid-1]!=n[mid]:
#             return mid
#         else:
#             return fobs(n,x,low,mid-1)
# # print(fobs(n,x,low,high))
# def lois(n,x,low,high):
#     while(low<=high):
#         mid=(high+low)//2
#         if n[mid]>x:
#             high=mid-1
#         elif n[mid]<x:
#             low=mid+1
#         else:
#             if mid==s or n[mid+1]!=n[mid]:
#                 return mid
#             else:
#                 low=mid+1
# # print(lois(n,x,low,high))
#
# def count(n,x):
#     first=fobs(n,x,low,high)
#
#     if first==-1:
#         return 0
#     else:
#         return (lois(n,x,low,high)-first+1)
# print(count(n,x))







"""

    count the number of ones in the array containing 0 and 1 in the array.
    
"""

# n=[0,0,0,1,1,1,1]
# low=0
# x=1
# s=len(n)
# high=s-1
#
# def counnt(n,x,low,high):
#
#     while low<=high:
#         mid=(low+high)//2
#
#         if n[mid]>x:
#             high=mid-1
#         elif n[mid]<x:
#             low=mid+1
#         else:
#             if mid==0 or n[mid-1]!=n[mid]:
#                 return s-mid
#             else:
#                 low=mid-1
# print(counnt(n,x,low,high))







"""
to find the sqrt of a number  using binary search without use of sqrt() function.
"""
#
# n=30
#
# low=1
# high=n
# ans=0
# def srbs(n,low,high):
#
#     while(low<=high):
#         mid=(low+high)//2
#         midsqrt=mid*mid
#         if midsqrt==n:
#             return mid
#         elif midsqrt>n:
#             high=mid-1
#         else:
#             low=mid+1
#             ans=mid
#     return ans
#
#
# print(srbs(n,low,high))



"""

to find the largest element in the array such that its greater than it's neighhbour

"""
#
# n=[1,30,2,40,5,60,0]
#
# #low=0
# s=len(n)

#
# def lebs(n,s):
#     high=s-1
#     low=0
#     while (low<=high):
#         mid=(high+low)//2
#
#         if (mid==0 or (n[mid-1]<=n[mid])) and (mid==s-1  or (n[mid+1]<=n[mid])):
#             return n[mid]
#         else:
#             if mid>0 and n[mid-1]>=n[mid]:
#                 high=mid-1
#             else:
#                 low=mid+1
#     return -1
#
# print(lebs(n,s))



"""

to search in a sorted rotated array and we dont know the number of times the array is being rotated
this can be done using binary search .
with the following implementation.

"""
#
# n=[10,20,30,40,50,8,9,]
# #n=[8,9,10,20,30,40,50]
# s=len(n)
# x=200
# def rabs(n,s):
#     high=s-1
#     low=0
#     while low<=high:
#         mid=(low+high)//2
#
#         if n[mid]==x:
#             return mid,n[mid]
#         elif n[low]<n[mid]:
#             if x>=n[low] and x< n[mid]:
#                 high=mid-1
#             else:
#                 low=mid+1
#         else:
#             if x>=n[high] and x<n[mid]:
#                 low=mid+1
#             else:
#                 high=mid-1
#     return -1
# print(rabs(n,s))
#
#


"""
to find the pair of element iin a sorted array whose sum is equal to the target sum 

"""
# n=[1,2,3,4,5,6,7]
# x=10
# s=len(n)
# def sumEqual(n,x):
#     low=0
#     high=s-1
#
#     for i in range(s):
#         if n[low]+n[high]>x:
#             high-=1
#         elif n[low]+n[high]==x:
#             return n[low],n[high]
#         else:
#             low+=1
#     return -1
# print(sumEqual(n,x))



"""
to find the triplet of a element in a sortedd array whose sum is equal to the tarfet sum given 
"""

# n=[2,3,4,8,9,20,40]
# x=32
# s=len(n)
# def istriplet(n,low,high,target):
#     for j in range(s):
#         if n[low]+n[high]>target:
#             high-=1
#         elif n[low]+n[high]==target:
#             return target,n[low],n[high],n[i]
#         else:
#             low+=1
#     return -1
#
# for i in range(s-1):
#     print(istriplet(n,i+1,s-1,x-n[i]))
#     # if istriplet(n,i+1,s-1,x-n[i]):
#     #     print(i,1)
#     # else:
#     #     print(i)
#



"""
to find the majority element in the array usiing morre algorithm 
"""


# n=[8,8,6,6,6,4,6]
# s=len(n)
#
# def majority(n,s):
#     res=0
#     count=1
#     for i in range(s):
#         if n[res]==n[i]:
#             count+=1
#         else:
#             count-=1
#         if count==0:
#             res=i
#             count=1
#     count=0
#     for i in range(s):
#         if n[res]==n[i]:
#             count+=1
#     if count<=s//2:
#         res=-1
#     return n[res]
# print(majority(n,s))

"""
to find the intersection of two list intersection stands for to find the common elements in both the list 

"""
# n=[3,4,5,6,7,8]
# m=[3,5,7,9,10,12,15,15]
#
# l=[]
# def common(n,m):
#     d=len(n)
#     e=len(n)
#     i,j=0,0
#     while (i<d and j<e):
#         if i>0 and n[i-1]==n[i]:
#             i+=1
#             continue
#         elif n[i]<m[j]:
#             i+=1
#         elif n[i]>m[j]:
#             j+=1
#         else:
#             l.append(n[i])
#             i+=1
#             j+=1
#     return l
# print(common(n,m))






