import random

def hint_for_guess(secret_number, user_guess):
    difference = abs(secret_number - user_guess)
    if difference == 0:
        return "Congratulations! You guessed the correct number."
    elif difference <= 5:
        return "You are close. Try again."
    elif difference <= 20:
        return "Getting warmer, but still not quite there. Try again."
    elif user_guess < secret_number:
        return "Too low. Try again."
    else:
        return "Too high. Try again."

def guess_number():
    secret_number = random.randint(1, 150)
    
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"Can you guess the secret number between 1 and 150? You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.")
            break
        else:
            print(hint_for_guess(secret_number, guess))
        
        attempts += 1
        print(f"You have {max_attempts - attempts} attempts remaining.")
    
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_number()
