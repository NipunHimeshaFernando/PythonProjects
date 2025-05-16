import random
import hangman_stages
word_list = ["apple", "potato", "beautiful"]
word_chosen = random.choice(word_list)
print(word_chosen)
display = []
for letter in word_chosen:
    display += "_"
print(display)
lives = 6
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(len(word_chosen)):
        if word_chosen[position] == guess:
            display[position] = guess
    print(display)
    if guess not in word_chosen:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")
    #print(lives)
    if "_" not in display:
        game_over = True
        print("You Won")
    print(hangman_stages.stages[lives])
