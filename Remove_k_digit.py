class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k > 0:
                k -= 1
                stack.pop()
            stack.append(i)
        while stack and stack[0] == '0':
            stack.pop(0)
        stack = stack[:len(stack) - k]
        res = ''.join(stack)
        return res if res else "0"
