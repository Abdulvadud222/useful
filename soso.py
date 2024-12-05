
h = 0

letters = input("write the word: ")

for letter in letters:
    n_letter = ord(letter)
    h = h*31 + n_letter
    if h > 2**32 -1:
        h = h % 2**32
    
print(hex(h))






































