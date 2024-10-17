from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    complement_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i
    return []

if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))

    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))

    nums3 = [3, 3]
    target3 = 6
    print(twoSum(nums3, target3))