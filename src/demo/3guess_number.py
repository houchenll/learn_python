# guess number
answer = 8
guess = -1
limit_count = 5
guess_count = 0

print('please guess the number')
while guess_count < limit_count and guess != answer:
    guess = int(input('input your number: '))
    guess_count += 1

if guess_count >= limit_count:
    print('you lose')
else:
    print('you got it, congratulations!')
