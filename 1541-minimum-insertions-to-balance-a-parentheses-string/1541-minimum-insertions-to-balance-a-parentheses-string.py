class Solution:
    def minInsertions(self, s: str) -> int:
        need , ans = 0,0 #ans is number of insertions and need is number of ) closing braces
        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    ans += 1
                    need -= 1

                need += 2
            else:
                need -= 1

                if need < 0:
                    ans += 1
                    need = 1

        return ans + need
