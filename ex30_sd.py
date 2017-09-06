people = 12
cars_cap = 15
trucks_cap = 17


# CODE LONG IF ELSE LONG VAO NHAU KHO DOC
if cars_cap > trucks_cap:
    print(f"We have cars capacity ({cars_cap}) > trucks capacity ({trucks_cap})." )
    if people >= cars_cap:
        print(f"Okay! We have {people} people but cars capacity only {cars_cap}.\n==> We shound stay home guys !!")
    else:
        print(f"We have {people} people and cars capacity is {cars_cap}.\n==> Get on cars ! We're choo choo.. ")
elif cars_cap < trucks_cap:
    print(f"Okay! We have cars capacity ({cars_cap}) < trucks capacity ({trucks_cap})." )
    if people <= trucks_cap:
        print(f"Okay! {people} people < trucks capacity {trucks_cap}.\n==> Let's jump in trucks guys!! Choo choo...")
    else:
        print("Ok! Cars and trucks can't take all of us. Let's stay home then.")
else:
    print(f"Cars capacity ({cars_cap}) same with trucks capacity ({trucks_cap})!")
    if people <= cars_cap:
        print ("Let's jump in whatever you like guys.\n Choo Choo...")
    else:
        print(f"We're only have {cars_cap} capacity but have {people} people here.\n==> Stay home guys! SAD BOYS!")



# CODE DUNG BOOLEAN DE DOC, CHI DAI DONG VI MUON PERFECT THEM DOAN ELSE
if (cars_cap != trucks_cap):
    if ((people > cars_cap) and (people > trucks_cap)):
        print("Too many people here! We're doomed!")
    elif ((people < cars_cap) or (people < trucks_cap)):
        if people < cars_cap:
            print(f"We got {people} people and capacity of cars is: {cars_cap} ,trucks is : {trucks_cap}.\n==> Let's go in cars")
        else:
            print(f"We got {people} people and capacity of cars is: {cars_cap} ,trucks is : {trucks_cap}.\n==> Let's go in trucks")
else:
    if people <= cars_cap:
        print(f"We got {people} people and capacity of cars and trucks is same: {trucks_cap}.\n==> Let's go in cars for better")
    else:
        print(f"We got {people} people and capacity of cars and trucks is same: {trucks_cap}!\n==> We're stay home guys!")
