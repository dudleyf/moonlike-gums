from moonlike_gums.words import Words
from moonlike_gums.gen import project_name

def test_project_name():
    words = Words(adjectives=['red', 'crunchy'], nouns=['door', 'leaf'])
    combinations = ['red door', 'red leaf', 'crunchy door', 'crunchy leaf']
    assert project_name(words=words) in combinations


def test_project_name_with_separator():
    words = Words(adjectives=['red'], nouns=['leaf'])
    assert project_name(separator='-', words=words) == 'red-leaf'
