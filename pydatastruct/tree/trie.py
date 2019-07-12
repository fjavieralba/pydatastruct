
class Node():
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end_of_word = False
        self.words_count_under = 0
    
    def add(self, word):
        if len(word) == 0:
            self.is_end_of_word = True
        else:
            char = word[0]
            if char not in self.children:
                self.children[char] = Node(char)
            self.words_count_under += 1
            self.children[char].add(word[1:])

    def contains(self, word):
        if len(word) == 0:
            return self.is_end_of_word
        char = word[0]
        if char in self.children:
            return self.children[char].contains(word[1:])
        else:
            return False
    
    def words_under(self, prefix):
        if len(prefix) == 0:
            acum = 1 if self.is_end_of_word else 0
            return acum + self.words_count_under
        else:
            char = prefix[0]
            if char not in self.children:
                return 0
            else:
                return self.children[char].words_under(prefix[1:])