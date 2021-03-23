print('Hello', end=' ')
print('World', 'its', 'a', 'new', 'day')


eggs = 12
def spam():
        global eggs
        eggs = 99
        print(eggs)

spam()
print(eggs)