"""
Python basics, Problem Set, hangman.py
Name: TODO
Collaborators: TODO
Time spent: TODO
"""

# ---------------------------------------------------------------------------- #
#                                 Hangman Game                                 #
# ---------------------------------------------------------------------------- #


# -------------------------------- Helper code ------------------------------- #
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    with open(WORDLIST_FILENAME, "r") as inFile:
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

choose_word(load_words())


# ---------------------------- end of helper code ---------------------------- #


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

# check đáp án
def is_word_guessed(secret_word, letters_guessed):
    # gia su secret_word da nhap
    """
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far, assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed, False otherwise
    """
    for i in range(len(letters_guessed)):
        letters_guesseds = letters_guesseds + letters_guessed[i]

    if (letters_guesseds == secret_word):
        returns = True
    else:
        returns = False
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

# các chữ đoán được
def get_guessed_word(secret_word, letters_guessed):
    a = len(secret_word)
    returns = ""
    for i in range(a):
        returns = returns + "_"
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
    """
    # giả sử mình đã có chuỗi đó
    for i in letters_guessed:
        for j in range(len(secret_word)):
            if(i == secret_word[j]):
                returns[j]= secret_word[j]
        
    print(returns)
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

# các chữ chưa đoán đc
def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    """
    b= " a, b, c, d, e, f, g, h ,i ,k , l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
    b = b.replace(",","")
    for i in letters_guessed:
        for j in b:
            if(i ==j):
                b = b.replace(i,"")
    return b
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
pass


def hangman(secret_word):

    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    print(secret_word)
    health =6   #số máu
    hea =0 # máu = 0
    a=0 # số lần trả lời
    letters_guessed = []  #câu trả lời đã thêm vào
    b= " a, b, c, d, e, f, g, h ,i ,k , l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
    b = b.replace(",","")
#số lần đoán

    returns = []   #câu trả lời hiện tại vd: _ a _
    print("There are "+ str(len(secret_word))+" word")
    for i in range(len(secret_word)):
        returns.append("_ ")
    returnss = ""  #là cái returns nhg mà là string
    for i in returns:
        returnss = returnss + i
    print(returnss)
    returnss = ""
    while hea < health:
    
        correct = 0 
        print("Please choose 1 word to guess: ")
        answer = input()

        for i in letters_guessed:
            while(answer == i):
                print("choose again")
                answer = input()
        letters_guessed.append(answer)
        for i in letters_guessed:
            for j in b:
                if(i ==j):
                    b = b.replace(i,"")
        a = a +1
        for i in range(len(secret_word)):
            if(answer == secret_word[i]):
            
                returns[i] = secret_word[i]
                correct =1
        if (correct == 1):
            for j in returns:
                returnss = returnss + j
            print("correct")
            print(returnss)
            if(returnss == secret_word):
                print("Congratulations")
                print("bạn trả lời "+ str(a)+" lần")
                break
            returnss=""
            print(b)
        if (correct == 0):
            print("wrong")
            print(b)
            health = health-1
            print("you have "+ str(health)+ " health left ")
        if(health == 0):
            print("try again")
            print("bạn trả lời "+ str(a)+" lần")
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# ---------------------------------------------------------------------------- #


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    if (my_word == other_word):
        returns = True
    else:
        returns = False
    return returns
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word

    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    """
    matching_words = []
    match_found = True

    for word in wordlist:
        if match_with_gaps(my_word, word):
            matching_words.append(word)
            match_found = True

    if match_found:
        all_matching_worlds = ' '.join(matching_words)
        print('Possible words matched are:', all_matching_worlds)
    else:
        print('No matches found')
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
    matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    print(secret_word)
    health =6   #số máu
    hea =0 # máu = 0
    a=0 # số lần trả lời
    letters_guessed = []  #câu trả lời đã thêm vào
    b= " a, b, c, d, e, f, g, h ,i ,k , l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
    b = b.replace(",","")
#số lần đoán

    returns = []   # câu trả lời hiện tại vd: _ _ a _
    print("There are "+ str(len(secret_word))+" word")
    for i in range(len(secret_word)):
        returns.append("_ ")
    returnss = "" # là cái returns nhg mà là string
    for i in returns:
        returnss = returnss + i
    print(returnss)
    returnss = ""
    while hea < health:
    
        correct = 0 
        print("Please choose 1 word to guess: ")
        answer = input()
        for i in letters_guessed:
            while(answer == i):
                print("choose again")
                answer = input()
        letters_guessed.append(answer)
        for i in letters_guessed:
            for j in b:
                if(i ==j):
                    b = b.replace(i,"")
        a = a +1
        for i in range(len(secret_word)):
            if(answer == secret_word[i]):
            
                returns[i] = secret_word[i]
                correct =1
        if (correct == 1):
            for j in returns:
                returnss = returnss + j
            print("correct")
            print(returnss)
            if(returnss == secret_word):
                print("Congratulations")
                print("bạn trả lời "+ str(a)+" lần")
                break
            returnss=""
            print(b)
        if (correct == 0):
            print("wrong")
            print(b)
            health = health-1
            print("you have "+ str(health)+ " health left ")
        if(health == 0):
            print("try again")
            print("bạn trả lời "+ str(a)+" lần")
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.




# ---------------------------------------------------------------------------- #

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
