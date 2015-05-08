import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
word = choose_word(wordlist)
# your code begins here!
def partial_word(word, letter):
    result = ''

    for enter_letter in word:
        if enter_letter in letter:
            result = result + enter_letter
        else:
            result = result + '-'
    return result


# print partial_word('mark', 'a')
# 1. reload a word and initial guess time
# 1.1 have an available letters list
# 2. user enter a letter to check if it match
# 2. 1 keep checking as long as the guess times is bigger than 0 , and condition is False
# 3. if not match , return false and guess time - 1
# 4. if right, stay true and guess time
# 5. lose when guess time = 0
# 6 win when the word is achieved, and return the word

def hangMan(answer_word):
    guess_times = 8
    word_guessed = False
    guessed_letter = ''

    available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while guess_times > 0 and not word_guessed:
        print '-------------------'
        print 'you have ' + str(guess_times) + ' left'
        print 'available letters: ' + ''.join(available_letters)
        enter_letter = raw_input('Please guess a letter: ')

        if enter_letter not in answer_word:
            guess_times -= 1
            available_letters.remove(enter_letter)
            print 'Oops, that letter is not in my word ', partial_word(answer_word, enter_letter)
        elif enter_letter not in available_letters:
            print 'you have already guessed that letter ', partial_word(answer_word, enter_letter)
        else:
            available_letters.remove(enter_letter)
            guessed_letter += enter_letter
            print 'Good guess ', partial_word(answer_word, guessed_letter)
            # check asnwer equals to the function, not the function to the word
        if answer_word == partial_word(answer_word, guessed_letter):
            word_guessed = True

    if word_guessed:
        print 'Congratulations ! You win !!'
    else:
        print 'sorry you lose'


print word
hangMan(word)










