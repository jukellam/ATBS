def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error: You tried to divide by 0.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many dogs?')
numDogs = input()
try:
    if int(numDogs) > 1:
        print('That is too many dogs')
    elif int(numDogs) < 1:
        print('You cannot have negative dogs (but you can have negative cats)')
    else: 
        print('That is the right amount of dogs.')
except ValueError:
    print('You did not enter a number, bye bye!')