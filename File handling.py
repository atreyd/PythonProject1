from sys import argv

from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))
in_file = open(from_file).read()
#indata = in_file.read()

print("The input file is %d bytes long" % len(in_file))
print("Does the output file exists? %r" % exists(to_file))
try:
    if exists(to_file) == True:
        print("Ready, hit RETURN to continue")
        input()
        out_file = open(to_file, 'r+')  # .write(in_file)
        out_file.write(in_file)
#        out_file.close()
        print("Allright, all done")
        out_file1 = open(to_file)
        print(out_file1.read())
        print("Outfile closed")
#        out_file.close()
#       in_file.close()
except:
    print("File not Found exception on file system.Check the file on your system and try again")
