## OTP Generation

Input Format: 13456
Output Format:1925
Explanation:
Take the string of numbers and generate a four digit OTP such that
1. 1f the number is odd square it.
2.If the number is even ignore it.

## CODE


n=input()
s=""
for i in n:
    if int(i)%2!=0:
        s+=str(int(i)**2)
print(s[:4])