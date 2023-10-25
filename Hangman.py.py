import random
import HangmanStage
import HangmanWord

#guess list
word_list = HangmanWord.word_list
#alphabet list to check
alphabet = list("abcdefghijklmnopqrstuvwxyz")
#check if users input ard
#outer loop to start a new game
while True:
    previousGuess = " "

    #Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    answer = random.choice(word_list)
    #creat a blank answer list
    blank = ["_"]*len(answer)
    #initiate life of 6
    life = 6
    #create boolean of game condition
    endGame = False

    print(HangmanStage.logo)
    print("Welcome to Hangman Game")
    #guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    while not endGame:
    
        guess = input("Guess a letter:").lower()
        while len(guess) > 1:
            guess = input("Please enter only one letter! Try again:")
        while guess in previousGuess:
            guess = input("You've guess the letter ard! Try again:")
        while guess not in alphabet:
            guess = input("Please enter letter between a to z! Try again:")
        
        
        #if passed the condition, add the letter to previous guess
        previousGuess += guess

        #compare letter with guess
        if guess not in answer:
            if life > 0:
                print(HangmanStage.stages[life])
                life -= 1
            elif life == 0:
                print(HangmanStage.stages[life])
                endGame = True
                previousGuess = " "
                blank.clear()
                print(f"\nYou lose the game.The word is {answer}")
            print(" ".join(blank)) 
            
        else:
            for i in range (len(answer)):
                letter = answer[i]
                if guess == letter:
                    blank[i] = letter
            print(" ".join(blank)) 
            if "_" not in blank:
                print(f"You won the game. The word is {answer}.")
                endGame = True
                previousGuess = " "
                blank.clear()
 # ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again != "y":
        break

    



    