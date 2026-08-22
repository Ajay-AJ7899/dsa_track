class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum1 = 0
        product = 1
        n2 = n
        while(n):
            n1 = n%10
            sum1+=n1
            product*=n1
            n = n//10
        if n2%(sum1+product)==0:
            return True
        else:
            return False
