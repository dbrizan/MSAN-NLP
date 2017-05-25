'''
@author: dgbrizan@usfca.edu
May, 2017
MSAN: Natural Langauge Processing
'''


class ir_system(object):
    '''
    The ir_system is the MVP implemetation of the boolean retrieval model.
    This class is provided for demonstration purposes only. A real IR system
    would be much more sophisticated.
    '''


    def __init__(self):
        '''
        The only data we need is a dictionary.
        '''
        # TODO: Extend this example by using defaultdict: key --> set
        self.__system_dictionary__ = dict()


    def read_file(self, file_name):
        '''
        This function takes the file_name, passed as an argument, and reads it
        into the dictionary. We depend on the caller to pass each file to be 
        indexed, one at a time, to this function.
        '''
        with open(file_name) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            for c in content:
                for token in c.split(' '):
                    # TODO: Extend this by adding to an existing set.
                    self.__system_dictionary__[token] = file_name


    def get_documents_matching(self, search_term):
        '''
        This function returns the file names corresponding to the search terms
        '''
        # TODO: Extend this by allowing multiple search terms (list?).
        # TODO: Extend this by performing an intersection of sets.
        if search_term in self.__system_dictionary__:
            return self.__system_dictionary__[search_term]
        else:
            return None

