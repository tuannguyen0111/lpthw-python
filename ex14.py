from sys import argv
script, user_name = argv
prompt = '>'

print(f"Hi {user_name},i'm the {script} script")
print("I like to ask you some questions.")
print(f"Do you like me {user_name} ?")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print(f"""
    Alright, so you said '{likes}' about liking me.
    You live in {lives}.
    Not sure where is it.
    Thanks anyway.
""")
