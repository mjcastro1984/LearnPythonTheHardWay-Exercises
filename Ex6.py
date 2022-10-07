# declare variable x with value of string, including 10 for %d
x = "There are %d types of people" % 10
# declare variable binary with value of "binary"
binary = "binary"
# declare variable do_not with value of "don't"
do_not = "don't"
# declare variable y with value of string, including the other variables in the string
y = "Those who know %s and those who %s." % (binary, do_not)

# print the following to console
print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)

# declare variable hilarious with value of Boolean False
hilarious = False
# declare variable joke_evaluation with value of string as shown - %r displays raw value of variable
joke_evaluation = "Isn't that joke so funny?! %r"

# print following to console, with variable hilarious used for %r
print (joke_evaluation % hilarious)

# declare variable w with value of string
w = "This is the left side of..."
# declare variable e with value of string
e = "a string with a right side."

# print result of w + e; w + e is a concatenation of the two variables
print (w + e)
