def collatz(num):
    if num % 2 == 0:
        res = num//2
        print(num//2)
    else:
        res = 3 * num + 1
        print(3 * num + 1) 
    return res

num = int(input())
res = collatz(num)
while(res != 1):
    res = collatz(res)
