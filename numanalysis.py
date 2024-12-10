numbers_input = input("Enter a series of numbers separated by spaces: ") 
numind = numbers_input.split()
odd = 0
even = 0
for i in numind:
    i = int(i)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"In the input you provided, the number of odd numbers is {odd}, and the number of even numbers is {even}.")








































