from .words import Words, random_addends


def project_name(separator=' ', syllables=Words.default_syllables, words=Words.from_brown_corpus()):
    a, n = random_addends(syllables)
    adj = words.random_adjective(a)
    noun = words.random_noun(n)
    return adj + separator + noun
