def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x


sumOfDigits = sum(int(digit) for digit in str(factorial(100))) # gets the number of digits in string 


print("The sum of digits for factorial 100 is " +str(sumOfDigits))   # Prints answer 

