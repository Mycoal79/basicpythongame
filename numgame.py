
import random

def welcome_message():
    print("Welcome to 'Guess the Number' game!\nYou have to guess the secret number within a limited number of attempts.\nLets start!")

def play_game():
    secret_number = random.randint(1,10)
    attempts = 5 
    wrong_guesses = []
    
    welcome_message()

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        player_guess = get_guess_input()
        attempts = check_guess(guess, secret_number, attempts, wrong_guesses)
        
        if player_guess == secret_number:
            break
        elif attempts == 0:
            print(f"Game Over! The secret number was {secret_number}. Better luck next time...")

def get_guess_input():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
              print("Please guess a number between 1 and 10.")
            else:
                return guess
        except ValueError:
            print("Invalid Input! Please enter a valid number.")

def check_guess(guess, secret_number, attempts, wrong_guesses):
    if guess > secret_number:
        print("You guessed too high")
        attempts -= 1
        wrong_guesses.append(guess)
    elif guess < secret_number:
        print("You guessed too low")
        attempts -= 1
        wrong_guesses.append(guess)
    else:
        print("Congratulations! You guessed the secret number!")
    return attempts
    
play_game()