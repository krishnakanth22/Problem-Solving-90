class Solution:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums)
        pair_list = []

        for i in range(n):
            for j in range(i + 1, n):
                num1, num2 = nums[i], nums[j]
                answer = Solution.gcd(num1, num2)
                if answer > 1:
                    pair_list.append([num1, num2])

        return True if pair_list != [] else False
