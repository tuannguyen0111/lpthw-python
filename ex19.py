# Khai bao functions cheese_and_cracker
def cheese_and_cracker(boxs_cheese,boxs_cracker):
    print(f"You have {boxs_cheese} cheese.")
    print(f"And you have {boxs_cracker} box crackers")
    print("That's enough for party!!")
    print("------------------------------------------")


print("You can put direct numbers to functions like this : ")
cheese_and_cracker(20,30) # Dua gia tri 20,30 vao functions cheese_and_cracker

print("Or you can put numbers through var like this : ")
amount_cheese = 15
amount_cracker = 35
cheese_and_cracker(amount_cheese,amount_cracker) # Dua 2 bien amount_cheese,amount_cracker vao fucntions

print("We can even do math in functions : ")
cheese_and_cracker(10+2,22+2)

print("And we can combine var and numbers like this : ")
cheese_and_cracker(amount_cheese+3,amount_cracker+3)

print("Nguoi dung tu nhap du lieu : ")
print("Bạn có bao nhiêu cheese ? ")
cheese = input("> ")
print("Bạn có bao nhiêu crackers ? ")
crackers = input("> ")
cheese_and_cracker(cheese,crackers)
