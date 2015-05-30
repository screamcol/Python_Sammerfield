import random

articles = ['the', 'a', 'an']
nouns = ['wind', 'swimming', 'pot', 'mouse', 'cat', 'dog', 'house', 'car']
verbs = ['sang', 'run', 'jumped', 'cry', 'clap', 'eat', 'ask']
adverbs = ['loudly', 'quietly', 'well', 'badly', 'honestly', 'clearly']

i = 0

while i < 5:
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    sent_struct = [[article, noun, verb, adverb], [article, noun, verb]]
    sentence = sent_struct[random.randint(0, 1)]
    """
    if len(sentence) == 4:
        a, b, c, d = sentence
        print('{0} {1} {2} {3}'.format(a, b, c, d))
    elif len(sentence) == 3:
        a, b, c = sentence
        print('{0} {1} {2}'.format(a, b, c))
    """
    for x in sentence:
        print(x, end=' ')

    print('')
    i += 1
