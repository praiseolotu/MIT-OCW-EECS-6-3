# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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
    inFile = open(WORDLIST_FILENAME, 'r')
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

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    counter = 0
    for index in range(len(secret_word)):
        if secret_word[index] in letters_guessed:
	    counter += 1
    if counter == len(secret_word):
	return True
    else:
	return False
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
def get_guessed_word(secret_word, letters_guessed):
    words = ""
    for index in range(len(secret_word)):
	if secret_word[index] in letters_guessed:
	    words += secret_word[index]
	else: 
	    words += "_ "
    return words
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   



def get_available_letters(letters_guessed):
    other_alpha = ""
    print(len(string.ascii_lowercase))
    for index in range(len(string.ascii_lowercase)):
	if string.ascii_lowercase[index] in letters_guessed:
	    pass  
	else:
	    other_alpha += string.ascii_lowercase[index]
    return other_alpha
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    

def hangman(secret_word):
    print("Welcome to the game Hangman! ")
    print("I am thinking of a word that is %d letters long." % len(secret_word))
    print("\n\n ****  Rule of the Game  ****")
    print("\t1. Guess one letter at a time.")
    print("\t2. Input only letter, numbers or symbol will result in loss of warnings")
    print("\t3. Incorrect consonant guess will result in loss of a guess")
    print("\t4. Incorrect vowel guess will result in loss of two guesses")
    print("\t5. Lose all three warnings and you will start losing guesses.")
    print("\t6. Repeating guess will result in lose of warnings")
    print("\t7. Total Score = Guess Left * Unique chracters")	
	
    #Initialize num_warnings and num_guesses
    num_warnings = 3 #3 warnings
    num_guesses = 6 #6 available guesses
    letters_guessed = [] # store letters guessed
	
    print("You have %d warnings left" %(num_warnings))
    print("_"*8)
	
# Games stops when:
# 1. Player runs out of guesses
# 2. Correctly guess secret word
	
     while (not is_word_guessed(secret_word, letters_guessed) and num_guesses != 0):
	print("You have %d guesses left" % num_guesses)
	print("Available letters: %s" % get_available_letters(letters_guessed))
	guess = input("Enter one guess: ")
	#convert guess to lowercase
	guess.lower()
		
		# Handle num_warnings
		str_num_warnings = str(num_warnings)
		
		# Handle for non alphabetic guess
		if not guess.isalpha():
			# Remove one warning when player still have warnings left
			if num_warnings > 1:
				num_warnings -= 1
				print("Oops! That is not a valid letter. You have " + str_num_warnings + " warnings left." + get_guessed_word(secret_word, letters_guessed))
			# Remove one guess when player have no warnings left
			else:
				num_guesses -= 1
				print("You have no warnings left      so you lose one guess: " + "\n" + get_guessed_word(secret_word, letters_guessed))
		# Handle for repeated guess
		elif guess in letters_guessed:
			if num_warnings > 1:
				num_warnings -= 1
				print("Oops! You've already guessed that letter. You have " + str_num_warnings + " warnings left." + "\n" +get_guessed_word(secret_word, letters_guessed))
			else:
				print("You have no warnings left      so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
		# Handle for correct guess
		elif guess in secret_word:
			letters_guessed.append(guess.lower())
			print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
		# Handle for incorrect guess
		else:
			print("Oops! That letter is not in my word. \nPlease guess a letter: " + get_guessed_word(secret_word, letters_guessed))
			if guess in ["a", "e", "i", "o", "u"]:
				# Subtract 2 guess for wrong vowel guess
				num_guesses -= 2
			else:
				num_guesses -= 1
				
		print("_"*8)
	# When players wins
	if is_word_guessed(secret_word, letters_guessed):
		print("Congratulations, you won! \nYour total score for this game is: %d " % (num_guesses * len(set(secret_word))))
	else:
		print("Sorry, you ran out of guesses. The word was %s" % secret_word)
    '''
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
