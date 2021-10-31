list = []
while True:
    num = input()
    if num == ' ':
        break
    list = list + [num]

print('list are:')
for num in list:
    print(' ' + num)