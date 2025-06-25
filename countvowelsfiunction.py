#s=str(input("enter the string"))
def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')
#print("vowels in string are:", count_vowels(s))