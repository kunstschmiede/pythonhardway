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
print "I am 6'2\" tall."  # escape double-quote inside string
print 'I am 6\'2" tall.'   # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


