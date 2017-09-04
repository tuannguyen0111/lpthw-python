from sys import argv
scripts, input_file = argv

#Khai báo function in tất cả
def print_all(f):
    print(f.read())

#Khai báo hàm đưa dấu nhắc trở lại vị trí đầu tiên của file (rewind)
def rewind(f):
    f.seek(0)

#Khai báo hàm in từng line của file
def print_a_line(linecount,f):
    print(linecount,f.readline()+'\n')



### Sử dụng các hàm đã khai báo
# Mở file cần đọc
current_file = open(input_file)

# IN TẤT CẢ
print("Trước tiên là in tất cả nội dung trong file: ")
print_all(current_file)
print("---------------------------------------")

# REWIND
print("Now let's rewind, kind of like a tape")
rewind(current_file)

# In từng line
current_line = 1
print("In từng line : ")
print_a_line(current_line,current_file)
current_line = current_line +1
print_a_line(current_line,current_file)
current_line = current_line +1
print_a_line(current_line,current_file)
current_line = current_line +1
print_a_line(current_line,current_file)
current_line = current_line +1


current_file.close()
