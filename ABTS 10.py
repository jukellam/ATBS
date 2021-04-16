import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone-number sized
    for i in range(0, 3):
        if not text[i].isdecimal(

        ):
            return False # no area code
    if text[3] != '-':
        return False # no dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no 1st 3 digits
    if text[7] != '-':
        return False # no second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # no last 4 digits
    return True

number = '415-555-1011'

print(isPhoneNumber(number))

message = 'My number is 303-827-6338'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())