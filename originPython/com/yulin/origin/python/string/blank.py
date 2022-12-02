# blank

# rstrip(), remove blanks in the end of string and return changed string
# origin string has not changed
favorite_language = "python        "
print(favorite_language.rstrip())    # "python"
print(favorite_language)    # "python        "

# lstrip(), remove blanks in the beginning of string and return changed string.
# origin string has not changed.
name = "    jack"
print(name.lstrip())    # jack
print(name)    # "    jack"

# strip(), remove blanks in the beginning and end of string and return changed string.
# origin string has not changed.
message = "    hello world    "
print(message.strip())    # hello world
print(message)    # "    hello world    "