import collections
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # defaultdict means that if an key is not found in the dictionary 
        # that instead of a KeyError being thrown a new value is created. 
        # The type of this new pair is given by the argument of defaultdict.

        # Usually, a Python dictionary throws a KeyError 
        # if you try to get an item with a key that is not currently in the dictionary. 
        # The defaultdict in contrast will simply create any items that you try to access 
        # (provided of course they do not exist yet). 
        # To create such a "default" item, 
        # it calls the function object that you pass in the constructor (more precisely, 
        # it's an arbitrary "callable" object, which includes function and type objects). 
        # Here default items are created using TrieNode, 
        # which will return the empty TrieNode object, None. 

        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter) # if letter exists, return the TrieNode, else return None
            if current is None:
                return False
        return current.is_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print trie.search("some")