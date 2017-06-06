'''
Created on May, 2017

@author: dbrizan
'''

class word(object):
    '''
    This class creates a shape for a word, one of many possible features in an NER system.
    '''
    
    
    def __init__(self):
        self.uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    def get_shape(self, spelling):
        shape = ''
        for char in spelling:
            if char in self.uppercase_list:
                if len(shape) == 0 or shape[-1] != 'X':
                    shape += 'X'
            elif char in self.lowercase_list:
                if len(shape) == 0 or shape[-1] != 'x':
                    shape += 'x'
            elif char in self.digit_list:
                if len(shape) == 0 or shape[-1] != 'd':
                    shape += 'd'
            else:
                shape += char
        return shape


if __name__ == '__main__':
    w = word()
    for test_word in ['and', 'Sydney', 'O\'Farrell', 'U.S.A.', 'Guinea-Bissau']:
        print 'Shape of', test_word, '=', w.get_shape(test_word)

