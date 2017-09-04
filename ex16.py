#READING AND WRITING FILE
from sys import argv
script, filename = argv

print(f"We're going to open {filename}")
print("If you don't want that press Ctrl+C")
print("If you want do that, hit RETURN")
input("?")

print("Opening file..")
# Open file and save to var name target
target = open(filename,'w')
print("Truncating the file")
target.truncate()
print("Now i'm going to ask you 3 lines")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")
print("Now i'm going to write 3 lines to the file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("Now close file")
target.close()
