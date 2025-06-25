n=int(input("enter a number"))
a,b=0,1

print("fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c