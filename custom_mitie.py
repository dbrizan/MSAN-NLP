'''
@author dgbrizan@usfca.edu
Date: May, 2017
This script shows how to train a custom MITIE model. Three labels are used:
a "person" tag for names of people; a DTT for dates and times; an org for
organisations.
This is an example only. (A real script would have more automation and many
more training examples.)
'''

import sys, os

sys.path.append('/home/dgbrizan/project/NLP/IE/MITIE/mitielib')
from mitie import *

# First training example: "My name is Sam at 2017-05-11." Entities: Sam; 2017-05-11.
sample = ner_training_instance(['My', 'name', 'is', 'Sam', 'at', '2017-05-11', '.'])
sample.add_entity(xrange(3, 4), "person")
sample.add_entity(xrange(5, 6), "DTT")

# Second training example, with "Brian Smith" and USF as the entities
sample2 = ner_training_instance(['The', 'other', 'day', 'at', 'work', 'I', 'saw', 'Brian', 'Smith', 'from', 'USF', '.'])
sample2.add_entity(xrange(7, 9), 'person')
sample2.add_entity(xrange(10, 11), 'org')

# Training -- use all word features.
trainer = ner_trainer('/home/dgbrizan/project/NLP/IE/MITIE/MITIE-models/english/total_word_feature_extractor.dat')
trainer.add(sample)
trainer.add(sample2)
ner = trainer.train()

# Save to disk.
# ner.save_to_disk("/home/dgbrizan/custom_ner_model.dat")

# Now that we have a trained model, let's look at what it does.
print "Model trained with tags:", ner.get_possible_ner_tags()

# Let's get a test instance
tokens = ['Paramore', 'was', 'manufactured', 'in', '2002-09-09', '.']
entities = ner.extract_entities(tokens)

# Print the test instance and all entities found.
print 'Test instance:', ' '.join(tokens)
for e in entities:
    range = e[0]
    tag = e[1]
    entity_text = ' '.join(tokens[i] for i in range)
    print '  ' + tag + ': ' + entity_text

