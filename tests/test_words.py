from moonlike_gums.words import count_syllables, Words


def test_count_syllables():
    assert count_syllables('foobar') == 2
    assert count_syllables('foo') == 1


def test_random_noun():
    nouns = ['bed', 'castle']
    words = Words()
    words.nouns.extend(nouns)
    assert words.random_noun() in nouns


def test_random_adjective():
    adjectives = ['red', 'sleepy']
    words = Words()
    words.adjectives.extend(adjectives)
    assert words.random_adjective() in adjectives

