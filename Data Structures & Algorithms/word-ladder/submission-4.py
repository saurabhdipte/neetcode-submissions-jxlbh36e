class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        seen=collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                newWord= word[:i] + '#' + word[i+1:]
                seen[newWord].append(word)
        
        visit=set([beginWord])
        q=collections.deque([beginWord])
        length=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return length
                for i in range(len(word)):
                    newWord=word[:i] + "#" + word[i+1:]
                    for neiWord in seen[newWord]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            length+=1
        return 0


