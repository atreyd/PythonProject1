from sys import argv

script, input_file = argv

def print_all(input_file):
    print(input_file.read())

def rewind(input_file):
    input_file.seek(0)

def print_a_line(line_count, input_file):
    print(line_count, input_file.readline())

current_file = open(input_file)

print("first let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape")
rewind(current_file)

print("Let's print the file into lines:")
for i in range (1, 6):
    print_a_line(i, current_file)
    continue
