from sys import argv

script,file_name = argv

print "Now we will erase the file: %r" % file_name

print "If you want that hit RETURN"
raw_input("?")

print "Opening the file ..."

target = open(file_name, "w")

print "Truncate the file. Goodbye."
target.truncate()

print "Write three lines:"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "Write in the file %r" % file_name
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Close the file"
target.close()
