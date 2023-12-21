#hangman game

import random
HANGMAN_PICS = ['''
+---+
    | 
    | 
    | 
   ===''', '''
+---+
O   | 
    | 
    | 
   ===''', '''
+---+
O   | 
|   | 
    | 
   ===''', '''
 +---+
 O   | 
/|   | 
     | 
    ===''', '''
 +---+
 O   | 
/|\  | 
     | 
    ===''', '''
 +---+
 O   | 
/|\  | 
/    | 
    ===''', '''
 +---+
 O   | 
/|\  | 
/ \  | 
    ==='''
]

words = '''ant babon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle farret fox fgfrong got goose hawk lion lizard lilama mole monkey moose mouse mule newt otter owl panda parrot pigeon
         pythong rabbit ram raven rhino salmon seal shark sheep
         skunk sloth snake spider stork swan tiger toad trout turkey turtle
         weasel whale wolf wombat zebra'''.split()

def getRandomWord(wordList):
    #This function returns a random string from the passed list of words.
    wordIndex = random.randint(0 , len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:    #Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed): 
    #Return the letter the player entered. This function makes rue the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')        
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')    
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #This function returns true if the player wants to play agian; otherwise, it returns false.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('HANGMAN')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameisDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if the payer has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is"' +secretWord +'"! You have won!')
            gameisDone = True
    else:
        missedLetters = missedLetters + guess
        
        #check if player has guess too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter '+ 
                str(len(missedLetters)) + ' missed gusses and '+
                str(len(correctLetters)) + ' correct gusses', 
                'the word was "' + secretWord + '"' )
            gameisDone = True

    #Ask the player if they want to play agian (but only if the game is done.)  
    if gameisDone:
        if playAgain():
            missedLetters= ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
