people = 20
cars_cap = 15
trucks_cap = 15

a = cars_cap != trucks_cap



if (cars_cap != trucks_cap):
    if ((people > cars_cap) and (people > trucks_cap)):
        print("Too many people here! We're doomed!")
    elif ((people < cars_cap) or (people <trucks_cap)):
        if people < cars_cap:
            print(f"We got {people} people and capacity of cars is: {cars_cap} ,trucks is : {trucks_cap}.\n==> Let's go in cars")
        else:
            print(f"We got {people} people and capacity of cars is: {cars_cap} ,trucks is : {trucks_cap}.\n==> Let's go in trucks")
else:
    if people <= cars_cap:
        print(f"We got {people} people and capacity of cars and trucks is same: {trucks_cap}.\n==> Let's go in cars for better")
    else:
        print(f"We got {people} people and capacity of cars and trucks is same: {trucks_cap}!\n==> We're stay home guys!")
