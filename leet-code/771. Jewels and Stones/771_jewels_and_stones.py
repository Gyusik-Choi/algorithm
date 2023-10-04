from collections import defaultdict


def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
    char_count = defaultdict(int)

    for char in stones:
        char_count[char] += 1

    total_num = 0

    for char in jewels:
        total_num += char_count[char]

    return total_num
