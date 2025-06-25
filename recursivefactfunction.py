def fact(n):
    
    
      return fact(n-1) * n

n = int(input("enter the number"))
print(fact(n))