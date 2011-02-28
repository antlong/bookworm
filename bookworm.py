import random
import glob
import os

path = os.path.realpath(__file__.replace(__file__, '/'))
books = glob.glob('*.txt')
text = open(random.choice(books), 'r').read()
words = text.split()
prefix = {}


def create(num_words=50, chars=''):
    l = []
    for i in range(num_words):
        l.append(random.choice(words))
    if chars:
        return ' '.join(l)[:chars]
    else:
        return ' '.join(l)

