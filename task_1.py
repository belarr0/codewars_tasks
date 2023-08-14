digit_list = []
result_number = 0
num = 58246

while num > 0:
    digit = num % 10
    digit_list.insert(0, digit)
    num //= 10

print(digit_list, "\n")

digit_list.sort(reverse=True)

for i in digit_list:
    result_number = result_number * 10 + i

print(result_number)

'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
'''