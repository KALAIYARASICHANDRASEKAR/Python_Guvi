#sum of natural numbers upto N
n=int(input("Enter a number:"))
sum=0
for num in range(0,n+1,1):
    sum=sum+num
print("sum of first",n,"number is:",sum)
