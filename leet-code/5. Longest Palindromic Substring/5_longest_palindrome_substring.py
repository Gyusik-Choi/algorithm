def two_pointers(word, start, end):
    while start >= 0 and end <= len(word) - 1 and word[start] == word[end]:
        start, end = start - 1, end + 1
    return word[start + 1: end]


def longest_palindrome(s):
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result,
                     two_pointers(s, i, i),
                     two_pointers(s, i, i + 1),
                     key=len)

    return result


print(longest_palindrome('babad'))
print(longest_palindrome('cbbd'))
print(longest_palindrome('babab'))
