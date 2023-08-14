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
