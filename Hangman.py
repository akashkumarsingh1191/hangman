from hangman_logo import hangman_stages,logo
from replit import clear

print(logo)
word_list=["UDEMY","APPMILLERS","PYTHON"]

import random
secret_word=random.choice(word_list)
length_word=len(secret_word)
blanks=[]

for _ in range(length_word):
    blanks.append("_")
print(" ".join(blanks))


# print(guess)
guess_letter = []
lives=6
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper()
    clear()
    if guess in guess_letter:
        print("You have already guessed this letter!")
        continue
    else:
        guess_letter.append(guess)
    print(guess_letter)

    for position in range(length_word):
        letter=secret_word[position]
        if letter == guess:
            blanks[position]=letter
    if guess not in secret_word:
        lives -= 1
    if lives == 0:
        end_game=True
        print("You lose")
    print(" ".join(blanks))
    print(hangman_stages[lives])

    if "_" not in blanks:
        end_game=True
        print("You Win")
    if end_game:
        ask=input("Do you want to play again? (Y/N)").upper()
        if ask == "Y":
            secret_word=random.choice(word_list)
            blanks.clear()
            length_word=len(secret_word)
            for _ in range(length_word):
                blanks.append("_")
            end_game=False
            guess_letter.clear()
            lives=6
        else:
            print("See you next Time!")