from sys import argv

script, first, second, third = argv

print "The script is called:", script
author = raw_input("Who wrote the script? ")
print "Your first variable is:", first
exp_first = raw_input("Explain first variable: ")
print "Your second variable is:", second
print "Your third variable is:", third
print "The author is %r" % (author)
print "The first variable explained: %r" % (exp_first)
