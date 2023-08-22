string = 'hello'
ending = 'lo'

str1 = len(string) - len(ending)
str2 = string[str1:]
if str2 == ending:
    print(f"Y + {string}, {str1}, {str2}")
else:
    print(f"N + {string}, {str1}, {str2}")

'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''