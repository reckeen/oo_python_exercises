# import the argv method from module sys
from sys import argv
# read in the script name and one command line argument
script, filename = argv
# open the file passed in as the first arg
txt = open(filename)
# print the message and the contents of the file
print "Here's your file %r:" % filename
print txt.read()
# print a message
print "Type the filename again:"
# read a value from raw input and store in file_again variable
file_again = raw_input("> ")
# open the filename stored in file_again, call it txt_again
txt_again = open(file_again)
# print the contents of txt_again
print txt_again.read()
txt.close()
txt_again.close()
