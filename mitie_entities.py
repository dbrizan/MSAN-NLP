import sys

sys.path.append('/home/dgbrizan/project/NLP/IE/MITIE/mitielib')

from mitie import *

ner = named_entity_extractor('/home/dgbrizan/project/NLP/IE/MITIE/MITIE-models/english/ner_model.dat')
tokens = tokenize(load_entire_file(sys.argv[1]))
entities = ner.extract_entities(tokens)

print 'Entities Detected'
print '================='
for entity in entities:
    print ' '.join(tokens[i].decode() for i in entity[0]),
    print '=', entity[1]

rel_detector = binary_relation_detector('/home/dgbrizan/project/NLP/IE/MITIE/MITIE-models/english/binary_relations/rel_classifier_people.person.place_of_birth.svm')
adjacent_entities = [(entities[i][0], entities[i+1][0]) for i in xrange(len(entities)-1)]
adjacent_entities += [(r, l) for (l, r) in adjacent_entities]

print ''
print 'Checking birth relationship between'
print '==================================='
for person, place in adjacent_entities:
    person_name = ' '.join(tokens[i].decode() for i in person)
    place_name  = ' '.join(tokens[i].decode() for i in place)
    print person_name, 'and', place_name

print ''
print 'Score', 'Person', 'Place'
print '=========================='
for person, place in adjacent_entities:
    relation = ner.extract_binary_relation(tokens, person, place)
    score = rel_detector(relation)
    person_name = ' '.join(tokens[i].decode() for i in person)
    place_name  = ' '.join(tokens[i].decode() for i in place)
    print score, person_name, place_name

