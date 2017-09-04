from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copy file from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file have {len(indata)} bytes long")
print(f"Does the output file exists? {exists(to_file)}")
print("Hit RETURN to continue, Ctrl+C to abort")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("All done!")
out_file.close()
in_file.close()

#### TU VIET TRONG 1 DONG
# f2data = open(file_dich,'w').write(open(file_nguon).read())
# open(file_dich).close()
# print("All done!")
####
