
def factorial_c():
    number = int(input("Enter the number to be factorised: "))
    result = 1
    for i in range(1, number +1):
        result *= i
    return f"The factorial of {number} is {result}"
print(factorial_c())
































