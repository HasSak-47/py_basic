
# open file
# write and clear and create if it doesn't exist
with open('file.txt', 'w+') as file:
    file.write('hello there!\n')

# append and create if it doesn't exist
with open('file.txt', 'a+') as file:
    file.write('hello there!\n')

# read and create if it doesn't exist
with open('file.txt', 'r+') as file:
    text = file.readline()
    print(text)
