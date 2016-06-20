from sys import argv

script, filename = argv

text = open(filename)

print "file contents"
print text.read()
