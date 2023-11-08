# Basic print
print('hello world')

# Variables
x = 0.1
y = "test"

print(x)
print(y)

# Basic input
inp = input('write something: ')
print(inp)

# Basic Types
a: int = 1         # Integer
b: float = 1.      # Float
c: str = "String"  # String
d: bool = True     # Boolean


# Type casting
to_i: int = int(1.)     # To int
to_f: float = float(1)  # To float
to_s: str = str(1.)     # To str


# functions
def square(x):
    return x * x


# function with type parameter
def square_ant(x: int) -> int:
    return x * x


print(square(0.2))
print(square_ant(3))


# Collections
list = [0., 'test', 1]   # mutable and growable
tuple = (0., 'test', 1)  # imutable and not growable
dictionary = {'one': 0., 'casa': 'test', 3: 1}  # mutable growable
# access through keys
# in this case 'one', 'casa', 3

# access
print(list[0])
print(tuple[0])
print(dictionary['one'])
