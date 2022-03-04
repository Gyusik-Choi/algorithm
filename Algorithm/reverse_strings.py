def reverse4(w):
    reversed_word = list(w)
    reversed_word.reverse()
    return ''.join(reversed_word)


def reverse3(w):
    return ''.join(reversed(list(w)))


def reverse2(w):
    reversed_word = ''

    for i in range(len(w) - 1, -1, -1):
        reversed_word += w[i]

    return reversed_word


def reverse1(w):
    reversed_word = ''

    for i in range(0, len(w)):
        reversed_word = w[i] + reversed_word

    # for char in w:
    #     reversed_word = char + reversed_word

    # for i, v in enumerate(w):
    #     reversed_word = v + reversed_word

    return reversed_word


word = 'abcde'
print(reverse4(word))

# https://www.youtube.com/watch?v=QOqUrMzOTcw
# https://itholic.github.io/python-reverse-reversed/
