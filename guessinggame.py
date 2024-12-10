import random
secret_number = random.randint(1, 100) 
gc = 0 #the user's guess count
print("Welcome to the Guessing Game!") 
print("I have selected a number between 1 and 100. Can you guess it?")
while True:
    guess = int(input("Enter your guess: "))
    gc += 1
    if guess == secret_number:
        print("Congratulations! You Guessed Correctly :)")
        break
    elif guess > secret_number:
        print("Your guess is too high. Try to guess a lower number.")
    elif guess < secret_number:
        print("Your guess is too low. Try to guess a higher number.")

print(f"It took you {gc} guesses to find the secret number")









































