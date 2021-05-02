import random
from dataclasses import dataclass, field
import nltk

ADJECTIVE_TAGS = ['JJ', 'JJR', 'JJS', 'JJT']
NOUN_TAGS = ['NN', 'NN+NN', 'NNS', 'NR']


@dataclass
class Words():
    default_syllables: int = 99
    adjectives: list[str] = field(default_factory=list)
    nouns: list[str] = field(default_factory=list)

    @classmethod
    def from_brown_corpus(cls):
        obj = cls()
        for (word, tag) in nltk.corpus.brown.tagged_words():
            if word.isalpha() and tag in ADJECTIVE_TAGS + NOUN_TAGS:
                if tag in ADJECTIVE_TAGS:
                    obj.adjectives.append(word.lower())
                elif tag in NOUN_TAGS:
                    obj.nouns.append(word.lower())
        return obj

    def random_adjective(self, syllables=default_syllables):
        while True:
            adj = random.choice(self.adjectives)
            if count_syllables(adj) <= syllables:
                return adj

    def random_noun(self, syllables=default_syllables):
        while True:
            noun = random.choice(self.nouns)
            if count_syllables(noun) <= syllables:
                return noun


def random_addends(s):
    """Return two random nonzero integers whose sum is 's'"""
    r = random.randint(1, s - 1)
    return r, s - r


def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count
