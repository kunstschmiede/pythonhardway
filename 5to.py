# Exercise 5
# my_name = 'zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 
# my_weight = 180 
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'

# print "Let's talk about %s." % my_name
# print "He's %d inches tall." % my_height
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth

# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)


# Exercise 8
# formatter = "%r %r %r %r"

# print formatter % (1, 2, 3, 4)
# print formatter % ("one", "two", "three", "four")
# print formatter % (True, False, False, True)
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % (
# 	"I had this thing.",
# 	"That you could type up right.",
# 	"But it didn't sing.",
# 	"So I said goodnight."
# )


# Exercise 9
# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print "Here are the days: ", days
# print "Here are the months: ", months

# print """
# There's something going on here.
# With the three double quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """

# Exercise 10
# print "I am 6'2\" tall."  # escape double-quote inside string
# print 'I am 6\'2" tall.'   # escape single-quote inside string

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """

# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat

# while True:
# 	for i in ["/","-","|","\\","|"]:
# 		print "%s\r" % i,


# Exercise 11
# print "How old are you? ",
# age = raw_input()
# print "How tall are you? ",
# height = raw_input()
# print "How much do you weigh? ",
# weight = raw_input()

# print "So, you're %r old, %r tall and %r heavy." % (
# 	age, height, weight)


# Exercise 12
# age = raw_input("How old are you? ")
# height = raw_input("How tall are you? ")
# weight = raw_input("How much do you weigh? ")

# print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


# Exercise 13
# from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third


# print "What is your favorite fruit? ",
# fruit = raw_input()
# print "What is your favorite movie? ",
# movie = raw_input()
# print "What is your favorite book? ",
# book = raw_input()
# print "What is your favorite country? ",
# country = raw_input()
# print "So you like to eat %s, watch %s, read %s, and travel to %s" % (fruit, movie, book, country)


# Exercise 14
# from sys import argv

# script, user_name = argv
# prompt = '< '

# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)

# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)

# print "What kind of computer do you have?"
# computer = raw_input(prompt)

# print """
# Alright, so you said %r about liking me.
# You live in %r.  Not sure where that is.
# And you have a %r computer.  Nice.
# """ % (likes, lives, computer)


# Exercise 15
# from sys import argv

# script, filename = argv

# txt = open(filename)

# print "Here's your file %r:" % filename
# print txt.read()

# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()

# txt.close()
# txt_again.close()


# Exercise 16
# from sys import argv

# script, filename = argv

# print "We're going to erase %r." % filename
# print "If you don't want that, hit CTRL-C (^C)."
# print "If you do want that, hit RETURN."

# raw_input("?")

# print "Opening the file..."
# target = open(filename, 'w+')

# print "Truncating the file.  Goodbye!"
# target.truncate()

# print "Now I'm going to ask you for three lines."

# line1 = raw_input("line 1: ")
# line2 = raw_input("line 2: ")
# line3 = raw_input("line 3: ")

# print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# print target.read()

# print "And finally, we close it."
# target.close()


# Exercise 17
# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# # we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alright, all done."

# out_file.close()
# in_file.close()

# Exercise 17 refactored
# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv; in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata); out_file.close(); in_file.close()

# Exercise 18
# this one is like your scripts with argv
# def print_two(*args):
# 	arg1, arg2 = args
# 	print "arg1: %r, arg2: %r" % (arg1, arg2)

# # ok, that *args is actually pointless, we can just do this:
# def print_two_again(arg1, arg2):
# 	print "arg1: %r, arg2: %r" % (arg1, arg2)

# # this just takes one argument
# def print_one(arg1):
# 	print "arg1: %r" % arg1

# # this one takes no arguments
# def print_none():
# 	print "I got nothin'."

# print_two("Zed", "Shaw")
# print_two_again("Zed", "Shaw")
# print_one("First!")
# print_none()


# Exercise 19
#def cheese_and_crackers(cheese_count, boxes_of_crackers):


# Exercise 39
# stuff = {'name':'Zed', 'age': 39, 'height': 6 * 12 + 2}
# print stuff['name']
# print stuff['age']
# print stuff['height']
# stuff['city'] = "San Francisco"
# print stuff['city']

# stuff[1] = 'Wow'
# stuff [2] = 'Neato'
# print stuff[1]
# print stuff[2]
# print stuff

# del stuff['city']
# del stuff[1]
# del stuff[2]
# print stuff

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

