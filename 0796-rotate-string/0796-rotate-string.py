class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a = list(s)
        for i in range(len(s)):
            e = a.pop(0)
            a.append(e)
            if a==list(goal):
                return True
            else:
                continue
        return False