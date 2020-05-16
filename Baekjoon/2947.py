# 2947 나무 조각
"""
풀이 : 버블 정렬 사용
"""
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)):
        for j in range(len(nums) - i):
            if max(nums[j], nums[j + 1]) == nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                print(*nums)