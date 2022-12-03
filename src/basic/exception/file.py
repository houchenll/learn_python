""" FileNotFoundError """

file_name = 'alice.txt'

try:
    with open(file_name) as fr:
        contents = fr.read()
except FileNotFoundError as e:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)
