from collections import Counter


def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
    char_nums = Counter(stones)

    num = 0

    for char in jewels:
        num += char_nums[char]

    return num
