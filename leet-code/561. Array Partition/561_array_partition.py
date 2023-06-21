def array_pair_sum(nums) -> int:
    # 정렬 후 짝수 인덱스 값만 슬라이싱한 리스트 총합 리턴
    return sum(sorted(nums)[::2])


print(array_pair_sum([1, 4, 3, 2]))
print(array_pair_sum([6, 2, 6, 5, 1, 2]))
