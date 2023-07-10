secret_word = "Computer"
guess = ""
limit = 3
counter = 0
run_out_of_guesses = False
while secret_word != guess and not(run_out_of_guesses):
    if counter < limit:
        guess = input("Guess the word: ")
        counter += 1
    else:
        run_out_of_guesses = True
if run_out_of_guesses == True:
    print("You lose")
else:
    print("You won")
