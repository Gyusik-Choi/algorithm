def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
    return sum(s in jewels for s in stones)
