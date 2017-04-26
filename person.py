'''
This class encapsulates everything we know about a person: name, bio and spouse.
We make the assumption that bio and spouse may be empty / missing.
@author dbrizan
'''


class person:

    def __init__(self, name):
        # This is the first function called when a person object is instantiated.
        # * Input: name = a dict with value for key 'f' representing a first name
        #                 ... and value for key 'last' representing a surname.
        # * Output: none
        # There are three fields: name (defaulted to an empty dict), biography
        # (defaulted to an empty list) and spouse (defaulted to a None object).
        self.name = dict()
        self.biography = []
        self.spouse = None
        self.change_name(name)

    def add_to_bio(self, words):
        # Mutator for biography: adds argument to the list of items in the biography.
        # Input: words (string) to be added to biography
        # Output: none
        self.biography.append(words)

    def get_biography(self):
        # Accessor for biography.
        # Input: none
        # Output: the biography as a single string, entries separated by newline.
        bio = ''
        for bio_entry in self.biography:
            bio += '  + ' + bio_entry + '\n'
        return bio

    def change_name(self, name):
        # Mutator for name.
        # Input: name = dictionary with first name(s) keyed by 'f' and surname keyed by 'last'
        # Output: none
        if 'f' in name:
            self.name['f'] = name['f']
        if 'last' in name:
            self.name['last'] = name['last']

    def get_name(self):
        # Accessor for name.
        # Input: none
        # Output: the name as a single string.
        name = ''
        if 'f' in self.name:
            name += self.name['f']
        if len(name) > 0:
            name += ' '
        if 'last' in self.name:
            name += self.name['last']
        return name

    def change_spouse(self, spouse):
        # Mutator for spouse.
        # Input: spouse (person object)
        # Output: none
        self.spouse = spouse

    def get_spouse(self):
        # Accessor for spouse.
        # Input: none
        # Output: spouse (person).
        return self.spouse

    def to_string(self):
        # Creates a string representation for the person object.
        # Input: none
        # Output: A string, formatted so that name, spouse and bio appear on different lines
        details = self.get_name() + '\n'
        if self.get_spouse() is not None:
            details += '* Married to: ' + self.get_spouse().get_name() + '\n'
        if len(self.biography) > 0:
            details += '* Biography:\n' + self.get_biography()
        return details

