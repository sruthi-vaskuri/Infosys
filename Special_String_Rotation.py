## Problem Statement

Every string is associated with the number separated by colon(:).
Task is to rotate the string based on the number. 
If the sum of square of digits is even then rotate the string right by 1 position else 
rotate the string left by 2 position.

Sample Input 0

rhdt:246,ghftd:1246

Sample Output 0

trhd ftdgh

## CODE

input_string=input()
l=list(input_string.split(","))
for i in l:
    index=i.find(':')
    string1=i[0:index]
    string2=i[index+1:]
    sum=0
    for k in string2:
        sum+=int(k)*int(k)
    if sum%2==0:
        print(string1[-1]+string1[:-1],end=" ")
    else:
        print(string1[2:]+string1[0:2],end=" ")
