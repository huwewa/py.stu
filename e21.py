from sys import argv
script, file_name = argv

def print_all(f):
    print f.read()

def rewin(f):
    f.seek(0)

def print_line(line_count, f):
    print line_count, f.readline()

in_file = open(file_name)

print "Print all: "
print_all(in_file)

print "Rewin: "
rewin(in_file)

line_count = 1
print_line(line_count, in_file)

line_count = line_count + 1
print_line(line_count, in_file)

line_count = line_count + 1
print_line(line_count, in_file)
