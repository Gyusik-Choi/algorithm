def is_palindrome(word):
    start, end = 0, len(word) - 1

    while start < end:
        if word[start] != word[end]:
            return 0

        start += 1
        end -= 1

    return 1

w = input()
print(is_palindrome(w))
