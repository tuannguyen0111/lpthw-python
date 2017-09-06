def break_words(stuff):
    "This function will break up words for us!"
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    """print first word after popping it off """
    word = words.pop(0)  # pop = remove item from it position in the list, and return it to var.
    print(word)

def print_last_word(words):
    word = words.pop()
    print(word)

def sort_sentence(sentence):
    "Takes in a full sentence and return the sorted words"
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence):
    "Print first and last word"
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    "Print sorted 1st and last word "
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
