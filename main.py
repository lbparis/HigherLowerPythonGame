import random

seedVal = int(input("What seed should be used? "))
random.seed(seedVal)
print('Welcome to higher or lower! HAVE FUN!!! :)')
lower = int(input('enter lower boundary: '))
print('lower: ', lower)
upper = int(input('enter upper boundary: '))
print('upper: ', upper)

if upper < lower:
    print('INVALID')
else:
    print('Great, lets guess a number between {} and {}'.format(lower, upper))

secret_num = random.randint(lower, upper)
##print('secret', secret_num)
while lower < secret_num < upper:
    guess = int(input())
    print(guess)
    if guess > secret_num:
        print('awwww, man! NOPE! too high!!!')
    if guess < secret_num:
        print('NOPE, NOPE, NOPE! too low!!!!')
    if guess == secret_num:
        print('You got it! WoooHOOOO!!!!')
        break


