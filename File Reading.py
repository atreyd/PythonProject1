from sys import argv

script, filename = argv

print("we are going to erase %r. " %filename)
print("If you don't want that, hit CTRL-C ")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w+',)

print("Truncate the file. Goodbye!!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these lines to the file ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it")
target.close()
print("Okay.. now this is how it looks like \n")

target1 = open(filename)
print(target1.read())


'''
txt = open(filenassme)
print("here's your file %r: " %filename)
print(txt.read())
print("Type the filename again")
file_again = input(" > ")

txt_again = open(filename)
print(txt_again.read())
txt.close()
'''