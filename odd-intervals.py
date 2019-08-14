#odd-intervals
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
for num in range(a,b+1):
    if num%2!=0:
        print(num,end=" ")
