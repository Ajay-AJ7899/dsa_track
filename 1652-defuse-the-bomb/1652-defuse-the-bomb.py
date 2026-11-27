class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        li = code + code
        lis = [0]*n
        s = 0
        if k==0:
            return [0]*n
        elif k>0:
            left = 0
            right = n-1
            for left in range(n):
                for i in range(left+1,left+k+1):
                    s+= li[i]
                lis[left]=s
                s = 0
        else:
            s=0
            a=len(code)-1
            while a>=0:
                b=a-1
                for i in range(b,b+k,-1):
                    s+=li[i]
                    
                lis[a]=s
                s=0
                a-=1

        return lis

            

        