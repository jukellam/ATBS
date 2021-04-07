import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} 

for character in message.lower():
    count.setdefault(character, 0) #If you don't find a letter in the key, set the value of that letter to 0
    count[character] = count[character] + 1

text = pprint.pformat(count)
print(text)

