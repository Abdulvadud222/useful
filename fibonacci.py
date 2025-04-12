first_num = int(input("Input your first number in fibonacci sequence: "))
second_num = int(input("Input your second number in fibonacci sequence: "))
length_of_sequence = int(input("Input the length of the sequence: "))
def next_num(num1, num2):
    return num1 + num2

sequence = [first_num, second_num]
for i in range(0, length_of_sequence):
    next_one = next_num(num1=first_num, num2=second_num)
    sequence.append(next_one)
    first_num = second_num
    second_num = next_one

print(sequence)