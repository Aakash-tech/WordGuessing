import random

# List of words
word_list = ["python", "developer", "programming", "algorithm", "function", "variable", "debugging", "compiler", "codechef", "machine", "bitcoin", "operation"]

def scramble_word(word):
    """Scramble the letters of a word randomly"""
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_game():
    # Pick a random word
    original_word = random.choice(word_list)
    scrambled = scramble_word(original_word)

    print("\nWelcome to the Word Scramble Game! ")
    print(f"Scrambled word: {scrambled}")

    attempts = 3
    while attempts>0:
        guess = input("Guess the word: ").lower()

        if guess==original_word :
            print("Correct! You guessed it!\n")
            return
        else:
            # update while loop condition
            attempts-=1
            print(f"Wrong guess. Attempts left: {attempts}")

# Run the game
if __name__ == "__main__":
    play_game()
