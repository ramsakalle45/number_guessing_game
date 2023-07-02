import random
import tkinter as tk

def play_game():
    number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!✌️")
    # print("I'm thinking of a number between 1 and 100.")

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = input("Enter your guess (or 'exit' to quit the game): ")

        if guess.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            return

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Your guess is out of range. Please enter a number between 1 and 100.")
            continue

        if guess == number:
            print("🎊Congratulations!🎊 You guessed the correct number!")
            return

        if guess < number:
            print("Too low!\nGuess again!")
        else:
            print("Too high!\nGuess again!")

        attempts -= 1

    print("Game over! You ran out of attempts.😕")
    print(f"The number I was thinking of was {number}.")


while True:
    play_game()
    choice = input("Would you like to play again? (yes/no): ")
    if choice.lower() != "yes":
        print("Thanks for playing!☺️")
        break
