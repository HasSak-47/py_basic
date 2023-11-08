# string basic
string = "this is a string"
print(string)
string = 'this is also string'
print(string)
string = """this is
a multi line
string"""
print(string)
string = '''this is also
a multi line
string'''
print(string)
string = 'this string is a single line one \
but divided into 3 different ones \
to make it readable'
print(string)

# string slice
string = 'hello, world!'
print(string)
print(string[2:5])    # subslice starting at 2 ending at 5
print(string[:5])     # subslice starting at 0 ending at 5
print(string[2:])     # subslice starting at 2 ending at len
print(string[:-1])    # subslice starting at 0 ending at len - 1
print(string[-5:-2])  # subslice starting at len - 5 ending at len - 2

# concatenate strings
string_a = 'string a'
string_b = 'string b'
print(string_a)
print(string_b)
string = string_a + string_b
print(string)

# format string
x = 10.3
format_str = f'this is a format string {x}'
print(format_str)
print("this is string was formated (3 points){:.3} {} {}".format(x, x, x))

# escape characters
escape = """
\' 	    Single Quote
\" 	    Double Quote
\\ 	    Backslash
\n 	    New Line
\r 	    Carriage Return
\t 	    Tab
\b 	    Backspace
\f      Form Feed
\101    Octal value
\x41    hex value
"""

# 'A' = 65 = 0x41 = 0101

print(escape)
