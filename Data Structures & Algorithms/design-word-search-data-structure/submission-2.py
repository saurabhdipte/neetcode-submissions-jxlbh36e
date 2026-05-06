class TrieNode:
    def __init__(self):
        self.children ={}
        self.endOfWord =False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(root,i):
            if i == len(word):
                if root.endOfWord == True:
                    return True
                else:
                    return False
            if word[i] == '.':
                for char in root.children.values():
                    if dfs(char,i+1):
                        return True
                return False
            else:
                if word[i] not in root.children:
                    return False
                return dfs(root.children[word[i]], i+1)
        return dfs(self.root,0)

