import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

choose = messages[random.randint(0,len(messages) - 1)]

print(choose)

for str in choose:
    for i in str:
        print('* * * '+i+' * * *')

newStr = choose[0:3] + 'the' + choose[4:]
print(newStr)

print(list(newStr))

print(tuple(newStr))

def addNewStr(someStr):
    someStr.append('Hello')

myStr = [1,2,3]
addNewStr(myStr)
print(myStr)