import random
random_number = random.randint(1,100)
print(random_number)
attempts = 0
while True:
    guess = int(input('guess a number: '))
    attempts += 1
    if guess < random_number:
        print('guessed number is small! guess a bigger number.')
    elif guess > random_number:
        print('the number is big! guess a number smallar than that.')
    else:
        print(f'congrats ! youve guessed the right number after {attempts}')
        break