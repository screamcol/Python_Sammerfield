import random, sys

articles = ['the', 'a', 'an']
nouns = ['wind', 'swimming', 'pot', 'mouse', 'cat', 'dog', 'house', 'car']
verbs = ['sang', 'run', 'jumped', 'cry', 'clap', 'eat', 'ask']
adverbs = ['loudly', 'quietly', 'well', 'badly', 'honestly', 'clearly']

try:
    amount_of_lines = sys.argv[1]
except IndexError:
    amount_of_lines = 5

try:

    amount_of_lines = int(amount_of_lines)

    if 0 < amount_of_lines <= 10:

        i = 0

        while i < amount_of_lines:
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
    else:
        input('Please use amount of lines between 0 and 10 inclusively. To exit press Enter')

except ValueError:
    input('Amount of lines should be int')