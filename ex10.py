tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass
"""

escapes = '''
This is a backslah \\ 
Let's put this in \'single\' quotes
We can do double \"quotes\" as well 
I don't know what a ASCII bell is: \a 
Does backspace back space 1=yes 12=no: 12\b
Formfeed? huh \f
'''
#comment
escapes_cond = """
A linefeed \n aka new line
\N{name} or maybe it's \N{Backslash}
Carriage Return \r
There is a blank above me? 
\t tibby tabby 
16-bit hex value \uxxxx
32-bit hex value \Uxxxxxxxx
\v <-we just went vertical tab
"""


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print escapes
print escapes_cond

print "here goes the while loop:"

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
