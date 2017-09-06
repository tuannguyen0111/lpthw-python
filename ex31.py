print("You're enter a dark room with two doors/")
print("Do you go throught door '1' or door '2'?")
door = input('> ')

if door == "1":
    print("Go throught door 1.\nYou see a big bear sleeping here.\nWhat would you do?")
    print("'1': take his cheese")
    print("'2': try kill bear when he's sleeping")
    option = input('> ')
    if option == "1":
        print("The bear eat your legs off. Good job!")
    elif option == "2":
        print("The bear eat your face off.\nNot a good choice!")
    else:
        print("You must choose between 1 or 2")
elif door == "2":
    print("Go throught door 2.\nYou see big bad monster Cthulhu's cave.\nWhat would you do?")
    print("'1': eat berries growing here!")
    print("'2': take yellow jacket hanging on the rock")
    option2  = input('> ')
    if option2 == "1":
        print("Ate berries and posioned.\nYou fukin done, don't eat anything you see boys.")
    elif option2 == "2":
        print("Big ass monster appear and tearing you off.")
else:
    print("You're fall off while walking around like fukin idiot!\nMake a right choice next time!")
