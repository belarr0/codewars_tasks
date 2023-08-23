'''sentence = 'abracadabra'

sum = 0

for i in sentence:
    if i in 'aeiou':
        sum += 1
    else:
        continue

print(sum)'''

sentence = 'abracadabra'
arr = list(sentence)

a = arr.count('a')
e = arr.count('e')
i = arr.count('i')
o = arr.count('o')
u = arr.count('u')

print(f"count of all vowell: {a + e + i + o + u}")


'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''