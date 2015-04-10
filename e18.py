# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copy %s to %s." % (from_file, to_file)

#in_file = open(from_file)
#indata = in_file.read()

#print "There are %r bytes in the from_file." % len(indata)

#print "The file %s exists? %r" % (to_file, exists(to_file))

#print "Will copy %s to %s.Hit RETURN to continue." % (from_file, to_file)
#raw_input()

#out_file = open(to_file, "w")
#out_file.write(indata)

#in_file.close()
#out_file.close()

#print "Finish copy."

"""
改写在一行代码
"""
open(to_file, "w").write(open(from_file).read())
