from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res, dups = set(), set()
    seen = {}
    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            print(f"dups: {dups}")
            for val2 in nums[i + 1:]:
                complement = -(val1 + val2)
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
                print(f"Seen: [{val2}]: {seen}")
    return res


numbers = [-1, 0, 1, 2, -1, 4]
answers = threeSum(numbers)
print(answers)
