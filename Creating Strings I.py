#
# def permutations(string):
#     if len(string) == 1:
#         return string
#
#     revursive_perms = []
#     for c in string:
#         for perm in permutations(string.replace(c,'',1)):
#             revursive_perms.append(c+perm)
#
#     return set(revursive_perms)
# string=input()
# print(len(permutations(string)))
# print("\n".join(permutations(string)))


from itertools import permutations

def stringPermutate(s1):
    perm=sorted(''.join(chars) for chars in permutations(s1))
    l=[]
    for x in set(perm):
        #l.append(x)
        print(x)
s1=input()
stringPermutate(s1)
# print(len(stringPermutate(s1)))
# print("\n".join(stringPermutate(s1)))
