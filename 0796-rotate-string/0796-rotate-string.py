class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # a = list(s)
        # for i in range(len(s)):
        #     e = a.pop(0)
        #     a.append(e)
        #     if a==list(goal):
        #         return True
        #     else:
        #         continue
        # return False

        if len(s) != len(goal):
            return False
        s1= s + s
        if s1.find(goal) != -1:
            return True
        else:
            return False
            