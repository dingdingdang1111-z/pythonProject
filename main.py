# Practice string operation

# assigning two strings
x='The quick brown fox'
y='jumps over the lazy dog'

# joint the two strings
z=x+y
print(z)

z=x+'\n'+y
print(z)

# Print the 31st to the 39th character of the string Z
print(z[31:39])

# Find how many "o"'s there exist up to the beginning of the word "jumps" in the string z.
z = 'The quick brown fox\njumps over the lazy dog'
# z1 is the substring of z before "jumps"
z1=z[:z.find('jumps')]
# the number of "o"s exist before "jumps" in the string z
print(z1.count('o'))

# Print string z where every character up to but not including the first "x" character is uppercased
# z2 is the substring of z before the first "x" not including "x"
z2=z[:z.find('x')]
print(z2.upper())

# Print string z where every character including the first "x" character is uppercased
# z3 is the substring of z before the first "x" including "x"
z3=z[:z.find('x')+1]
print(z3.upper())

# Split string z at the newline character
print(z.split('\n'))

# Split string z at every emtpy space
print(z.split())

#  Assign a short motivational sentence to a variable and print it 20 times.
str='Be a dreamer and a doer.\t'
print(str*20)