import unittest

def palindromex(palabra):
    alreves = palabra[::-1]
    return palabra == alreves

print(palindromex("reinier"))

"""def palindrome(word):
    if len(word) <= 1: 
        return True
    if word[0]== word[-1]:
        return palindrome(word[1:-1])
    else: 
        return False
    
print(palindrome("romenar"))"""