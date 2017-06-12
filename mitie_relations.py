'''
@author dgbrizan@usfca.edu
Date: May, 2017
This script shows how to build MITIE binary relations and test them. In this case, we
use the cause celebre example of Aya Hijazi who was released from jail in Egypt last
month. We test with another well-known example: Amanda Knox.
'''

import sys, os
sys.path.append('/home/dgbrizan/project/NLP/IE/MITIE/mitielib')

from mitie import *


# We need to load an  NER model for the rest to work.
ner = named_entity_extractor('/home/dgbrizan/project/NLP/IE/MITIE/MITIE-models/english/ner_model.dat')

# We want to construct a binary relation. We need to name it (in harmony with MITIE's
# standards?) and pass the NER instance.
trainer = binary_relation_detector_trainer('people.person.court_acquittal', ner)

# Now: our training example. Ideally, we should have several.
train1 = ['An', 'Egyptian', 'court', 'has', 'acquitted', 'Aya', 'Hijazi', ',', 'her', 'husband', 'and', 'six', 'other', 'charity', 'workers', 'of', 'all', 'charges', ',', 'after', 'they', 'were', 'imprisoned', 'for', 'more', 'than', 'three', 'years', 'without', 'trial', '.']
# We indicate "acquitted" with entities: Egyptian court, Aya Hijazi.
trainer.add_positive_binary_relation(train1, xrange(1,3), xrange(5,7))  
# A negative example: Aya Hijazi did not acquit Egyptian court.
trainer.add_negative_binary_relation(train1, xrange(5,7), xrange(1,3))
# Train the above.
rel_detector = trainer.train()

# Save the relation to dis for future use.
# rel_detector.save_to_disk("rel_classifier.svm")


# Now let's test this with a new sentence using a rewording of Amanda Knox' Wikipedia:
test_sentence = ['In', '2015', ',', 'the', 'Supreme', 'Court', 'of', 'Cassation', 'definitively', 'acquitted', 'Amanda', 'Knox', '.']
# By the way, the real Wikipedia version (below) fails.
# test_sentence = ['In', '2015', ',', 'Knox', 'was', 'definitively', 'acquitted', 'by', 'the', 'Supreme', 'Court', 'of', 'Cassation', '.']

# The NER is not built in here -- so kind of cheating -- but it's good as an example.
print 'Sentence:', ' '.join(test_sentence)
print 'Detection score for Knox being acquitted:', rel_detector(ner.extract_binary_relation(test_sentence, xrange(3, 4), xrange(9, 13)))

