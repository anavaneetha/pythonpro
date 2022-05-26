# Program to check if a string is palindrome or not

my_str='madam'
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("The string is polindrome")
else:
    print("The string is not polindrome")

    

