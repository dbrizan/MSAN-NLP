from person import person


class student(person):

    def __init__(self, name):
        '''
        Constructor for student.
        '''
        # super(student, self).__init__()  # This is python 3 syntax
        person.__init__(self, name)
        self.courses = []
        self.student_id = '000000'

    def get_student_id(self):
        '''
        Accessor for student ID.
        Input: none.
        Output: student ID (string).
        '''
        return self.student_id

    def set_student_id(self, sid):
        '''
        Mutator for student ID.
        Input: student ID (string).
        Output: none.
        '''
        self.student_id = sid

    def get_courses(self):
        '''
        Accessor for courses.
        Input: none.
        Output: courses (list).
        '''
        return self.courses

    def add_to_courses(self, course):
        '''
        Mutator for courses.
        Input: course (string) to be added.
        Output: none.
        '''
        self.courses.append(course)

    def get_biography(self):
        '''
        Accessor for biography.
        Input: none
        Output: the biography as a single string, entries separated by newline.
                Note that this includes courses taken.
        '''
        bio = ''
        for bio_entry in self.biography:
            bio += '  + ' + bio_entry + '\n'
        for course in self.courses:
            bio += '  + Took course = ' + course + '\n'
        return bio

