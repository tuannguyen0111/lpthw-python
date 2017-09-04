def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def sub(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b

def nhan(a,b):
    print(f"Multiplying {a} * {b}")
    return a * b

def chia(a,b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with functions !")

age = add(25,5)
height = sub(180,5)
weight = nhan(16,4)
iq = chia(200,2)

print(f"""
    Age : {age}
    Height : {height}
    Weight : {weight}
    IQ : {iq}
""")

print("Here is puzzle")
what = add(age,sub(height,nhan(weight,chia(iq,2))))
print(what)
