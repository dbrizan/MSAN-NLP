'''
@author dgbrizan@usfca.edu
May, 2017
MSAN: Natural Language Processing
==
This script:
    1) Reads (text file) argv[1]
    2) Extracts NLTK-based named entities
    3) Prints entities in TYPE ==> NAME format
It is a proof-of concept only, meant to be easy to read, not
focused on efficiency, etc.
'''


def read_document(doc):
    '''
    Accepts file name (doc).
    Reads a text document and returns it as a single string.
    '''
    with open(doc) as f:
        content = f.readlines()
    lines = ''
    for c in content:
        # lines.append(c)
        lines += c
    return lines


def get_named_entities(subtree):
    '''
    Accepts nltk.Tree (subtree).
    Returns the named entities in the subtree.
    '''
    named_entities = []
    for node in subtree:
        if type(node) is Tree:
            if node.label() != 'ROOT':
                named_entities.append([node.label(), node.leaves()])
    return named_entities


def print_entities(entity_list):
    '''
    Accepts list of entities.
    Prints the named entities in the subtree.
    '''
    for entity in entity_list:
        # The entity is [TYPE, [NAME, POS_TAG]*]
        entity_type = entity[0]
        entity_name = ''
        for name in entity[1]:
            entity_name += name[0] + ' '
        name = name[:-1]
        print entity_type, '==>', entity_name


if __name__ == '__main__':
    import sys
    from nltk import *

    lines = read_document(sys.argv[1])
    chunks = ne_chunk(pos_tag(word_tokenize(lines)))
    entities = get_named_entities(chunks)
    print_entities(entities)

