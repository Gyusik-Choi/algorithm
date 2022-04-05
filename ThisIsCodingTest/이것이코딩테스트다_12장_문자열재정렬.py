import re


S = input()
strings = re.findall('[A-Z]{1}', S)
numbers = re.findall('[0-9]{1}', S)

strings.sort()
numbers.sort()

numbers_sum = sum(list(map(int, numbers)))

print(''.join(strings) + str(numbers_sum))

# K1KA5CB7 => ABCKK13
# 7K1KA5CB => ABCKK13
# AJKDLSI412K4JSJ9D => ADDIJJJKKLSS20

# https://software-creator.tistory.com/32

