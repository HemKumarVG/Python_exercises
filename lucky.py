lucky = 9
guess = int(input("Guess any random number between 1 to 25:"))

if guess >= lucky + 3:
    print("your guess is too high")

if guess <= lucky - 3:
    print("your guess is too low")

if guess == lucky:
    print("congratulations you guessed it right")
elif (guess >= lucky + 2) and (guess <= lucky + 2):
    print("you are almost there")
