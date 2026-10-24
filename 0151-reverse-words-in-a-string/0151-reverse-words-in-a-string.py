class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        result = []
        for i in range(len(word)-1,-1,-1):
            result.append(word[i])
            if i!=0:
                result.append(" ") #bez we neeed space in between
        return "".join(result)#bez we need it as a single string 