class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        star_count = 0
        for i in s:
            if i == "(":
                open_count += 1
            elif i == ")":
                close_count += 1
            elif i == "*":
                star_count += 1

            if close_count > open_count + star_count:
                return False

        open_count = 0
        close_count = 0
        star_count = 0
        for i in reversed(s):
            if i == "(":
                open_count += 1
            elif i == ")":
                close_count += 1
            elif i == "*":
                star_count += 1

            if open_count > close_count + star_count:
                return False

        return True
