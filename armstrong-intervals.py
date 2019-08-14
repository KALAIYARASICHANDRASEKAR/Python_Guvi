#armstrong intervals
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
for num in range(a,b+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num)
