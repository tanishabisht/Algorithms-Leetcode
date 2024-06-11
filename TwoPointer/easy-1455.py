# Check If a Word Occurs As a Prefix of Any Word in a Sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            if sentence[i].find(searchWord) == 0:
                return i + 1
        return -1