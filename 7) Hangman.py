import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["apple", "banana", "camel", "dog", "elephant"]
lives = 6
chosen_word = random.choice(word_list)
print("Welcome to Hangman!!!")
#test word 
print(f"solution is {chosen_word}")
###
display = []
for letter in chosen_word:
    display.append("_")
print(display)
end_game = False
while not end_game:
    guess = input("Guess a letter: ")
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess 
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1 
        print(f"You chose {guess}, thats not in the word. You lose one life.")
        if lives == 0:
            end_game = True
            print("You lost")
    if "_" not in display:
        end_game = True
        print("You win")
    print(stages[lives])
