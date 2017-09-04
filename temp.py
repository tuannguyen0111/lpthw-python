from sys import argv
script,input_file = argv

def print_all(f):
    print('\n' + f.read() +'\n')
    print('-----------------------------\n')

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(f.readline())

# Mo file
current_file = open(input_file)

# IN TAT CA
print_all(current_file)

# REWIND
rewind(current_file)

# IN 1 DONG
lines = 0
with open(input_file) as f:
    for line in f:
        lines = lines + 1
# print(lines)
current_line = 0
while (current_line < lines):
    print_a_line(current_line,current_file)
    current_line = current_line + 1
