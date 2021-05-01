from brown_corpus import adjectives, nouns
import random

def random_addends(s):
    """Return two random nonzero integers whose sum is 's'"""
    r = random.randint(1, s-1)
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


DEFAULT_SYLLABLES = 99


def random_adjective(syllables=DEFAULT_SYLLABLES):
    while True:
        adj = random.choice(adjectives)
        if count_syllables(adj) <= syllables:
            return adj


def random_noun(syllables=DEFAULT_SYLLABLES):
    while True:
        noun = random.choice(nouns)
        if count_syllables(noun) <= syllables:
            return noun


def haikunate(syllables=DEFAULT_SYLLABLES, separator=' '):
    a, n = random_addends(syllables)
    adj = random_adjective(a)
    noun = random_noun(n)
    return adj + separator + noun
