# 최대공약수를 구하는 알고리즘
def get_gcd(first, second):
    if second == 0:
        return first
    return get_gcd(second, first % second)


a = 12
b = 8
gcd = get_gcd(a, b)
print(gcd)
