phrase = "Giraffe Academy"

print('lower', phrase.lower())  # giraffe academy
print('islower', phrase.islower())  # False
print('upper', phrase.upper())  # GIRAFFE ACADEMY
print('isupper', phrase.isupper())  # False
print('upper isupper', phrase.upper().isupper())  # True

print('len', len(phrase))

print('index G', phrase.index('G'))  # 0
print('index a', phrase.index('a'))  # 3
print('r index a', phrase.rindex('a'))  # 10
# print('index un exist', phrase.index('z'))  # ValueError: substring not found

print('replace', phrase.replace('Giraffe', 'Elephant'))  # Elephant Academy
