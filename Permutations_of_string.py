## Problem Statement

## Print all the possibilities of the given string of length of the string

Sample Input 0

abc
Sample Output 0

abc
acb
bac
bca
cab
cba

##CODE

input_string=input()
l=[]
answer=[]
for i in input_string:
     l.append(i)
def permutate(start,l,length):
     if start==length:
        answer.append(''.join(map(str,l)))
        return
     for i in range(start,len(l)):
        n=l[start]
        l[start]=l[i]
        l[i]=n
        permutate(start+1,l,length)
        n=l[start]
        l[start]=l[i]
        l[i]=n
permutate(0,l,len(s))
ans.sort()
for i in ans:
     print(i)