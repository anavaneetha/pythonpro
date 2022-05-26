def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x


sumOfDigits = sum(int(digit) for digit in str(factorial(10)))  


print("The sum of digits for factorial 10 is " +str(3+6+2+8+8+0+0))   

