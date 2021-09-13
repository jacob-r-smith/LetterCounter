
word = ''

def word_input():

    print('Please enter any word: ')
    
    word = input()
    
    return word

def letter_count(word):
    print(word + ' has ' + str(len(word)) + ' letters in it.')


word = word_input()

letter_count(word)


#look into incorporating fstrings
#look into beep boop
