import random
import os
import re

path = os.path.join(os.path.realpath(os.path.curdir) + '/books/')
books = os.listdir(path)


def create(num_words=20):
    for each_book in books:
        inputFile = open(path + each_book, 'r')
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
    print random_text.strip()

if __name__ == "__main__":
    create()
