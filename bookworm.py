import random
import os
import re

path = os.path.join(os.path.realpath(os.path.curdir) + '/books/')
books = os.listdir(path)

def create(num_words=50, chars=''):
    inputFile = open(path + books[random.randrange(0, len(books))], 'r')
    text = inputFile.read()
    words = text.split()
    prefix = {}
    for i in range(len(words)-2):
        if (words[i], words[i+1]) not in prefix:
            prefix[(words[i], words[i+1])] = []
        prefix[(words[i], words[i+1])].append(words[i+2])
    current_pair = random.choice(prefix.keys())
    random_text = current_pair[0] + ' ' + current_pair[1]
    for i in range(num_words-2):
        if current_pair not in prefix:
            break
        next = random.choice(prefix[current_pair])
        random_text = random_text + ' ' + next
        current_pair = (current_pair[1], next)
    random_text = re.sub(r'[\W]', ' ', random_text)
    random_text = re.sub(r'  ', ' ', random_text)
    selection = random_text.strip()
    if chars:
        return selection[0:int(chars)].strip()
    else:
        return selection.strip()

if __name__ == "__main__":
    print create()
