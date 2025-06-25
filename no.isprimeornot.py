n=int(input("enter the no."))
if(n<=1):
    print("no. is not prime no.")
else:
    is_prime = True
    for i in range(2,int(n**0.5 + 1)):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        print("no. is prime no.")
    else:
        print("no. is not prime no.")        
