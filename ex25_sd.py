from ex25 import *
sentence = "Chung ta la nhung con bo vui nhon"
print("We have this sentence: ",sentence)

print("Now we Break it: ")
words = break_words(sentence)
print(words)

print("Sorted words : ")
sorted_words = sort_words(words)
print(sorted_words)

print("Print first and last word :")
print_first_word(words)
print_last_word(words)


print("Print first and last word sorted : ")
print_first_word(sorted_words)
print_last_word(sorted_words)

print("Print sorted sentence")
sorted_sentence = sort_sentence(sentence)
print(sorted_sentence)

print("Print first and last unsort and sorted : ")
print("---- unsort ---- ")
print_first_and_last(sentence)
print("---- sorted ---- ")
print_first_and_last_sorted(sentence)
print("---------------- ")
