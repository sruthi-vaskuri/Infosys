## PROBLEM STATEMENT
## A non empty string containing only alphabets. 
## Print length of longest prefix in the string which is same as suffix without overlapping.
## Else print -1 if no prefix or suffix exists.



## CODE


input_string=input()
maxlen=0
for i in range(0,len(input_string)//2):
    s1=input_string[0:i+1]
    s2=input_string[len(input_string)-i-1:]
    if s1==s2:
       maxlen=i+1
if maxlen==0:
   print(-1)
else:
   print(maxlen)