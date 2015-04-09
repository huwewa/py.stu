# -*- coding: utf-8 -*-
from sys import argv

script,file_name = argv

txt = open(file_name)
print "Here is the filename : %r" % file_name
print txt.read()

print "Open the file?"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
