def is_palindrome(s: str):
    arr_s = []

    for idx, char in enumerate(s):
        if char.isalnum():
            arr_s.append(char.lower())

    front = 0
    back = len(arr_s) - 1

    while front < back:
        if arr_s[front] != arr_s[back]:
            return False

        front += 1
        back -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))
print(is_palindrome("0P"))

# 참고
# 파이썬 알고리즘 인터뷰
# https://docs.python.org/3/library/stdtypes.html?highlight=isalnum#str.isalnum
