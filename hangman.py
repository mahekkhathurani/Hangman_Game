
import random
HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
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
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']

with open("words.txt","r") as f:
    content=f.read()
words = content.split("\n")
f.close()
alphabet_set="abcdefghijklmnopqrstuvwxyz"
alphabet=alphabet_set
print("Lets Play H A N G M A N")

player=""

def wordtoguess():

    guess_word=random.choice(words).lower()
    return guess_word

def guess(alphabet):

    while True:
        guess=input("Guess the letter: ").lower()

        if len(guess) != 1:
            print("Guess only single letter..")
            guess = input("Guess the letter: ").lower()
            return guess

        elif guess not in alphabet:
            print("Letter is already done guess a different letter..")
            guess=input("Guess the letter: ").lower()
            return guess

        else:
            return guess

def guesscheck(wrong,alphabet,correctletter,partblank):

    if wrong < len(HANGMANPICS):
        print(HANGMANPICS[wrong])
    print("Letters to guess from: "+alphabet)

    for i in range(len(guess_word)):
        if guess_word[i] in correctletter:
            partblank=partblank[:i]+guess_word[i]+partblank[i+1:]
    return partblank

guess_word=wordtoguess()
partblank="_"*len(guess_word)
print("Word length to guess "+partblank+" Length of word: ",len(partblank))
wrong = 0
again1=False
correctletter=""

def playagain():

     playagain=input("Do you want to play again ? Type Y/N: ").lower()

     if playagain=='y':
        global guess_word,partblank,wrong,correctletter,alphabet
        guess_word=wordtoguess()
        partblank="_"*len(guess_word)
        print("Word length to guess "+partblank+" Length of word: ",len(partblank))
        wrong = 0
        correctletter=""
        alphabet=alphabet_set
        partblank=guesscheck(wrong,alphabet,correctletter,partblank)

     else:
         return 0

while True:

    if wrong == len(HANGMANPICS):
        print("You ran out of attempts try next time..")
        print("Correct word was: "+guess_word)
        choice=playagain()
        if choice ==0:
            print("Thanks for Playing Hangman !")
            break

    elif(partblank==guess_word):
        print("You won!!")
        choice=playagain()
        if choice ==0:
            print("Thanks for Playing Hangman !")
            break

    else:
        player=guess(alphabet)

        left=[]
        for char in guess_word:
            left.append(char)
        if player in guess_word:
            print("Correct Guess ! Keep going..")
            correctletter=correctletter+player
        else:
            wrong+=1
            print("Oops ! You guessed a wrong letter..")
        correct=[]
        for m in correctletter:
            correct.append(m)
        length=len(left)
        i=0
        while i<length:
            if left[i] in correct:
                left.remove(left[i])
                length=length-1
                continue
            i=i+1
       
        alphabet=alphabet.replace(player,"")
        partblank=guesscheck(wrong,alphabet,correctletter,partblank)
        print("Word guessed till now: ")
        for i in range(len(partblank)):
            print(partblank[i])
            
        if len(HANGMANPICS)-wrong == 2:
            hint=left[0]
            print("Here's a HINT for you...The word contains the letter: "+hint)
            wrong+=1
            x=len(HANGMANPICS)-wrong
        
            print("Using Hint, deducts a chance. You have",x," chance left..")

        else:
            print("You have",len(HANGMANPICS)-wrong," chances left..")
