people = 30
cars = 20
trucks = 15

if cars > people:
    print("We'd take the cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("ppl = cars ... I have no idea!")


if trucks > cars:
    print("Wow, that's too many trucks")
elif trucks < cars:
    print("We should take cars instead trucks!")
else:
    print("Still can't decide")

if people > trucks:
    print("We should take on trucks!")
else:
    print("Fine, now we're home")
