def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    answer = 0

    while left < right:
        if left_max <= right_max:
            answer += left_max - height[left]
            left_max = max(left_max, height[left + 1])
            left += 1
        else:
            answer += right_max - height[right]
            right_max = max(right_max, height[right - 1])
            right -= 1

    return answer


# print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(trap([4, 2, 0, 3, 2, 5]))
print(trap([1, 1, 6, 6, 5, 4, 3]))
