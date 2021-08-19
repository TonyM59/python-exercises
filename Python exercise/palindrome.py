#Write a method is_palindrome(word) that takes in a string word and returns the true if the word is a palindrome,
#false if otherwise. A is a word that is spelled the same forwards and backwards.  

def is_palindrome(word):
    if word==word[::-1]:
        print("True")
    else:
        print("False")
is_palindrome("eve")