# # OPEN FILE
# from sys import argv
# script, filename = argv
#
# txt = open(filename)
# print("Your file information is here : ")
# print(txt.read())


#ALTERNATIVE WAY
print("What's file you want to open ?")
filename = input('> ')
txt = open(filename)

print("Your file information is : ")
print(txt.read())
