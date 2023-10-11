def letter_combinations(digits):
    # y 값을 통해서 같은 키의 값이 2개 이상 나오지 않도록 한다
    def get_combinations(y, temp, combs):
        if len(temp) == len(digits):
            combs.append(''.join(temp[:]))
            return

        for i in range(y, len(digits)):
            key = digits[i]

            for j in range(len(letters[key])):
                temp.append(letters[key][j])
                get_combinations(i + 1, temp, combs)
                temp.pop()

        return combs

    letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    return get_combinations(0, [], [])


print(letter_combinations("23"))
# print(letter_combinations("2"))
