from moonlike_gums.words import count_syllables


def test_count_syllables():
    assert count_syllables('foobar') == 2
    assert count_syllables('foo') == 1
