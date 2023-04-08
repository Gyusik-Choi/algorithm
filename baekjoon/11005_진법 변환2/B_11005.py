def get_changed_num(remain):
    if 'A' <= chr(remain + 55) <= 'Z':
        return chr(remain + 55)
    return str(remain)


N, B = map(int, input().split())
n = N
changed_num = ''

while n > 0:
    quotient, remainder = divmod(n, B)
    n = quotient
    changed_num = get_changed_num(remainder) + changed_num

print(changed_num)
