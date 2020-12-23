def get_word():
    while True:
        word = input("Word Here : ")
        word = word.lower()
        if word == "quit":
            print("THANK YOU for holding up!")
            quit()
        if not word.isalpha():
            print("Word should be deprived of special characters or numerics or NULL!\nEnter again.\n")
            continue
        if len(word) > 10:
            print("Please reduce your alphabet count!\nEnter again.\n")
            continue
        return word

def get_guesses():
    while True:
        guesses = input("Number of Guesses Here : ")
        if guesses == "quit":
            print("THANK YOU for holding up!")
            quit()
        try:
            guesses = int(guesses)
            if guesses > 10 or guesses < 1:
                print("Please enter the number of guesses in range,i.e [1-10]\n")
                continue
        except:
            print("You did not enter a number!\nEnter again.\n")
            continue
        return guesses

def validity():
    while True:
        alpha = input("\n\nEnter alphabet : ")
        if alpha == "quit":
            print("THANK YOU for holding up!")
            quit()
        if not alpha.isalpha():
            print("You did not enter any alphabet!\nEnter again.\n")
            continue
        if len(alpha) > 1 or len(alpha) < 1:
            print("Seems like you have mistakenly entered MORE THAN ONE alphabets!\nEnter again.\n")
            continue
        return alpha

def the_game(word, guesses, blobword):
    words = word
    for guess in range(1, guesses+1):
        alpha = validity()
        try:
            found = word.index(alpha)
            blobword = blobword[:found] + alpha + blobword[found+1:]
            word = word[:found] + "*" + word[found+1:]
            print("Guessed Right!\t\t\t\t", blobword)
            if blobword.find("*") == -1:
                print("CONGO!.. YOU WON!")
                break
        except:
            print("OOOPS!.. Guessed Wrong!")
        print("\t\tChances remaining -->", (guesses-guess))
        if guess == guesses:
            print("SORRY!.. YOU LOST!")
            print("RIGHT WORD WAS : ",words)
            quit()
    quit()

import time
print("\n\n<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")
print("\nHELLO and WELCOME to HANGMAN.\n")
time.sleep(2)
print('''Rules >>> ~ 2 players at a time.
          ~ Player 1 gets to choose a word.
          ~ Player 2 gets to guess the word chosen by 1.
          ~ Guess can be made an alphabet at a time.
          ~ Number of guesses to be made can be chosen by 2.\n''')
time.sleep(8)
print("PS : If at any point of time you wanna quit, just press \"quit\" and enter.\n\n=========   Let's BEGIN!  ===========\n\n")
time.sleep(2)
print("PLAYER 1 --> Think of a word and enter. [Not More Than 10 Alphabet Long]")
word = get_word()
print("\nPLAYER 2 --> Think of the number of guesses you would like to take. [Not More Than 10 Chances]")
guesses = get_guesses()
if guesses < len(word):
    print("<<<<<<<<<<  SORRY You Cannot Proceed. Your Number of Guesses are Less Than the Length of the Word  >>>>>>>>>>>")
    quit()
blobword = ""
for rant in word:
    blobword += "*"
print("\nWord chosen by 1 is -->", blobword)
print("Number of guesses chosen by 2 is -->", guesses)
the_game(word, guesses, blobword)
