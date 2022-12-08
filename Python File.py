n=int(input("enter number: "))
#prime check
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print(n,"is not a prime")
else:
    print(n,"is prime")
    #PALINDROME CHECK
    x=n
    sum=0
    while x>0:
        r=x%10
        sum=sum*10+r
        x=x//10
    if sum==n:
        print(n,"is a prime palindrome")
    else:
        print(n,"is not a prime palindrome")
