# Python program to get factorial of any number

n=int(input("enter a number of which you want factorial :"))
n=n+1
j=1
for i in range(1,n):
    i=i+1
    j=j*(i-1)
print(f"factorial of {n-1} is :{j}")
