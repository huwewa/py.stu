from sys import argv

script,user_name = argv
prompt = '> '

print "Hi,%s, do you like me?" % user_name
like = raw_input(prompt)

print "What kinds computer you have?"
computer = raw_input(prompt)

print """
Hi,%s,your like me %r. And your computer is %r.
""" % (user_name, like, computer)
