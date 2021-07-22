import random

top = input("Type a number: ")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print('Please type a number next time.')
    quit()


random_number = random.randint(0, top)
guesses = 0

while True:
    guesses +=1
    userGuess = input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print('Please type a number next time')
        continue

    if userGuess > random_number:
        print('try a smaller number')
    else:
        print('try a bigger number')

    if userGuess == random_number:
        print('you got it')
        break
    else:
        print('you got it wrong')

print('only took,', guesses, 'guesses!')