import collections
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in range(len(word)):
            if word[i] == '.':
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if current.children.get(c):
                        word = word[:i] + c + word[i + 1:]
                        if self.search(word):
                            return self.search(word)
                return False
            else:
                current = current.children.get(word[i]) # if letter exists, return the TrieNode, else return None
                if current is None:
                    return False
        return current.is_word
        

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
#print wordDictionary.search("a")
#print wordDictionary.search(".at")
wordDictionary.addWord("bat")
print wordDictionary.search(".at")
#wordDictionary.search("an.")
#wordDictionary.search("a.d.")
#wordDictionary.search("b.")
#wordDictionary.search("a.d")
#wordDictionary.search(".")