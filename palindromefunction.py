word =input("enter word")
def is_palindrome(s):
    return  s[::-1]

print("palindrome" if is_palindrome(word) else "not palindrome")
