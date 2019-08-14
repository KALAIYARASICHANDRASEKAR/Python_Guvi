#array of n integers ,sum of first k integers
n=int(input("Enter a size:"))
k=int(input("Enter index value:"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
sum=0
for i in range(0,k):
    sum=sum+int(arr[i])
print(sum)
      
