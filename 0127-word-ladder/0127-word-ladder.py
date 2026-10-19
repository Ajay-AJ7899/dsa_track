class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        #we will convert the wordlist to set
        wordList = set(wordList)
        if endWord not in wordList:#bez makes no sense if end is not in wordlist
            return 0 
        queue = deque()
        level = 1
        queue.append((beginWord,level))
        while queue:#bfs
            word,level = queue.popleft()
            if word == endWord:
                return level
            #else now 
            for i in range(0,len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue
                    word_new = word[:i]+ch+word[i+1:]
                    if word_new in wordList:
                        queue.append((word_new,level+1))
                        wordList.remove(word_new)
        return 0
