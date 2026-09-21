class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        flipped = ""
        for i in x:
            if i == "0":
                flipped += '1'
            else:
                flipped += '0'
        return int(flipped,2)