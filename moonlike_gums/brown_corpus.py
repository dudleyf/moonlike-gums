import nltk


adjectives = []
nouns = []

adjective_tags = ['JJ', 'JJR', 'JJS', 'JJT']
noun_tags = ['NN', 'NN+NN', 'NNS', 'NR']

for (word, tag) in nltk.corpus.brown.tagged_words():
    if word[0].isalpha() and word[-1].isalpha() and tag in adjective_tags + noun_tags:
        if tag in adjective_tags:
            adjectives.append(word.lower())
        elif tag in noun_tags:
            nouns.append(word.lower())
