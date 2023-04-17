S = list(input())
alphabets = ''
nums = 0
for i, s in enumerate(S):
    if s.isalpha():
        alphabets += s
        continue

    nums += int(s)

print(''.join(sorted(alphabets)) + str(nums))

# 참고
# https://appia.tistory.com/178
