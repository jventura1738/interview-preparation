# Justin Ventura

'''This is the module for tries api.'''


class TrieNode:
    def __init__(self, x=0):
        self.val = x
        self.children = dict()


class Trie:
    # Constructor:
    def __init__(self):
        self.root = TrieNode()

    # Insert in O(n) time where n is the length of the word.
    def insert(self, word: str) -> None:
        '''Insert a word into the trie.'''
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(x=char)
            node = node.children[char]
        node.children['*'] = TrieNode(x='*')  # Mark end of word.

    # Search for a word in O(n) time where n is the length of the word.
    def search(self, word: str) -> bool:
        '''Search for a word in the trie.'''
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if '*' in node.children:
            return True
        return False

    # Check if a prefix exists in O(n) time where n is the length of the prefix.
    def starts_with(self, prefix: str) -> bool:
        '''Search for a prefix in the trie.'''
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == '__main__':
    words = ['joe', 'joseph', 'ma', 'mom', 'momma', 'mama', 'mommy', 'joey']
    Lambda = Trie()
    map(Lambda.insert, words)

    # TODO: Test search, starts_with, and insert.
