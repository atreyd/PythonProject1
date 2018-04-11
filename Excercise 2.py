def break_words(stuff):
    # This function will break up words
    words = stuff.split(' ')
    return words


def sort_words(stuff):
    # This function will sort the words
    return sorted(stuff)


def print_first_word(words):
    '''This function will print the first word after popping it off'''
    word = words.pop(0)
    print(words)


def print_last_word(words):
    ''' Prints the last word after popping it off '''
    word = words.pop(-1)
    print(words)

def sort_sentence(sentence):
    ''' Sorts the sentences for us '''
    words = break_words(sentence)
    sort_words(words)
    return words


def print_first_and_last_sentence(sentence):
    ''' Prints first and last sentence '''
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Prints first and last sentence after sorting"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


words = break_words("broken words - Deepak Atrey")
print(words)
words = sort_words("Sorted words - Deepak Atrey")
print(words)
print_first_and_last_sentence("first and last deepak atrey")
print_first_and_last_sorted("first and last sorted surname atrey")