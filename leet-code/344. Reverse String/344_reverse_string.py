class Solution:
    def reverseString(self, s: list[str]) -> None:
        front, back = 0, len(s) - 1

        while front < back:
            s[front], s[back] = s[back], s[front]
            front, back = front + 1, back - 1
