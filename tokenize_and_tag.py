'''
This script takes the first argument as the name of a text file, reads it into
memory, tokenizes the file, tags each token and prints the text/tag tuple list.
This file is meant for class demonstration purposes only.
@author dgbrizan@usfca.edu
'''

if __name__ == '__main__':
    import nltk
    import sys

    text = []
    tagged_text = []
    with open(sys.argv[1]) as f:
        content = f.readlines()
        for line in content:
            text.extend(nltk.word_tokenize(line))
    tagged_text = nltk.pos_tag(text)
    print tagged_text
