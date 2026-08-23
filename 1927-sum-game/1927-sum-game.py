class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2

        q1 = q2 = 0
        num1 = num2 = 0

        for i in range(len(num)):
            if num[i] == "?":
                if i < mid:
                    q1 += 1
                else:
                    q2 += 1
            else:
                if i < mid:
                    num1 += int(num[i])
                else:
                    num2 += int(num[i])
        diff = num1 - num2
        if q1 == q2:
            return diff != 0
        return diff * 2 != 9 * (q2 - q1)