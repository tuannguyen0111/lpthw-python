print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do: ')
print('\nnew lines and \ttabs')

poem ="""
\tThis world is weird
and you don't need to make it harder.
\n\t\tDo you understand it ?
"""

print("---------------")
print(poem)
print("---------------")

five = 10 + 2 - 3 - 4
print(f"This is must be five : {five}")
print("Write in another way :",five)
print("---------------\n")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print("With a start point of : {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, {crates} crates")

start_point = start_point / 10

print("We can also do that this way with start point now is {}\n".format(start_point))
formula = secret_formula(start_point)
print("We'd have {} beans,{} jars, {} crates".format(*formula))
