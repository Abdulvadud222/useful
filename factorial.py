
def factorial_c():
    number = int(input("Enter the number to be factorised: "))
    result = 1
    if number == 0:
        print("The factorial of 0 is 1 - it is crazy, isn't it?")
    elif number < 0:
        print("It is not possible to factorise negative numbers!")
    else:
        for i in range(1, number +1):
         result *= i
        return f"The factorial of {number} is {result}"
print(factorial_c())
































