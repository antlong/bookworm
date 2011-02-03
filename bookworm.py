import random
import glob

books = glob.glob('book_*.txt')
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


if __name__ == "__main__":
    create()
