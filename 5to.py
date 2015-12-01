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
from sys import argv

script, user_name = argv
prompt = '< '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)


