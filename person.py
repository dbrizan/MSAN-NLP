class person:

    def __init__(self, name):
        self.name = dict()
        self.biography = []
        self.spouse = None
        self.change_name(name)

    def add_to_bio(self, words):
        self.biography.append(words)

    def get_biography(self):
        bio = ''
        for bio_entry in self.biography:
            bio += '  + ' + bio_entry + '\n'
        return bio

    def change_name(self, name):
        if 'f' in name:
            self.name['f'] = name['f']
        if 'last' in name:
            self.name['last'] = name['last']

    def get_name(self):
        name = ''
        if 'f' in self.name:
            name += self.name['f']
        if len(name) > 0:
            name += ' '
        if 'last' in self.name:
            name += self.name['last']
        return name

    def change_spouse(self, spouse):
        self.spouse = spouse

    def get_spouse(self):
        return self.spouse

    def to_string(self):
        details = self.get_name() + '\n'
        if self.get_spouse() is not None:
            details += '* Married to: ' + self.get_spouse().get_name() + '\n'
        if len(self.biography) > 0:
            details += '* Biography:\n' + self.get_biography()
        return details

