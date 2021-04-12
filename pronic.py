## Problem Statement

## Given a integer we should divide the total number into substrings and 
## we should verify each num is pronic num or not if pronic we should print that nums in the sorted order

Sample Input 0

272
Sample Output 0

2 72 272

## CODE

## Function to check if the number is pronic or not
def pronic(num):
    for i in range(1,num):
        if i*(i+1)==num:
           return True
    return False
## Taking input
n=input()
l=[]
for i in range(1,len(n)+1):
    for j in range(0,len(n)-i+1):
        k=j+i
        if pronic(int(n[j:k])) or int(n[j:k])==0:
           if int(n[j:k]) not in l:
              l.append(int(n[j:k]))
l.sort()
for i in l:
     print(i,end=" ")
    