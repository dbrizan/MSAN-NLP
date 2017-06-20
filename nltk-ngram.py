'''
Script to count n-grams of text (argv) using NLTK's ngrams utility.
@author dgbrizan@usfca.edu
@date June, 2017
'''


def read_text(filename):
    import nltk
    from nltk import word_tokenize

    with open(filename) as f:
        content = f.readlines()
    text = []
    for line in content:
        for token in nltk.word_tokenize(line):
            text.append(token)
    return text


def get_ngrams(text, n):
    import nltk
    from nltk.util import ngrams

    return ngrams(text, n)


if __name__ == '__main__':
    import sys
    from collections import Counter

    text = read_text(sys.argv[1])
    print 'Bigrams:', Counter(get_ngrams(text, 2))
