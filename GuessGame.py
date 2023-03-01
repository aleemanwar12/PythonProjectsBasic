secret_number = 19  # This will be the number that has to be guessed by the user
guess_count = 0  # this is the number of attempts the user has made
guess_limit = 5 #number of guesses
guess = ""
while guess_count < guess_limit:
    guess = int(input("GUESS THE NUMBER:"))
    guess_count += 1
    if guess == secret_number:
        print("YAY you won")
        break

if guess_count >= guess_limit:
    print("you lose")

