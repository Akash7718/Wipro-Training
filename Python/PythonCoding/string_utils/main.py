"""
main function
"""
from string_utils.string_operations import reverse_string,to_uppercase,string_length
from string_utils.string_validations import is_palindrome,is_alpha

text = input("Enter a string : ")

print("Reversed: ",reverse_string(text))
print("uppercase: ", to_uppercase(text))
print("length: ",string_length(text))

print("Is Palindrome: ", is_palindrome(text))
print("Contains only alphabets:  ", is_alpha(text))
