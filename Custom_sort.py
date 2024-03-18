class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def custom_sort_key(char):
            if char in order:
                return order.index(char)
            else:
                return len(order)  

        sorted_s = sorted(s, key=custom_sort_key)

        return ''.join(sorted_s)
