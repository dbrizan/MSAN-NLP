'''
Demonstration for the person class and student subclass.
(This is somewhat unrealistic, but good for a demonstration.)
@author dbrizan
'''

def get_a_person(name):
    '''
    Factory for the person classes. Requires user input.
    Input: name of the person to be constructed.
    Output: person (or subclass) instance.
    '''
    import sys
    from person import person
    from student import student

    person_type = ''
    while person_type != 'person' and person_type != 'student':
        person_type = raw_input('Enter \'person\' or \'student\': ')
    p = None
    if person_type == 'person':
        p = person(name)
    else:
        p = student(name)
    return p

#
# Main
#
if __name__ == '__main__':
    from student import student

    s = get_a_person({'f': 'Elle', 'last': 'Woods'})  # Create a person named "Elle Woods"
    s.add_to_bio('2001: Entered Harvard')

    # If our person is a student, add some student stuff.
    if isinstance(s, student):   # In python 3: "if type(s) is student:"
        s.add_to_courses('2017: Web Analytics')
        s.add_to_courses('2017: Natural Language Processing')

    print s.to_string()

