n=int(input("enter digit"))
def sum_of_digit(n):
    return sum(int(d) for d in str(n))
print("sum of digit is:", sum_of_digit(n))