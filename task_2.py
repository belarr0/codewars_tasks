def last_man_standing(n):
    a = list(range(1,n+1))
    while len(a)>1:
        a = a[1::2][::-1]
    return a[0]

'''
Object
Find the last number between 1 and n (inclusive) that survives the elimination process

How It Works
Start with the first number on the left then remove every other number moving right until you reach the the end,
then from the numbers remaining start with the first number on the right and remove every other number moving left,
repeat the process alternating between left and right until only one number remains which you return as the "last man standing"
'''