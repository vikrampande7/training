class Professor:
    def __init__(self,prof_name, subjects_taught = []):
        self.prof_name = prof_name
        self.subjects_taught = subjects_taught
    ###method to append subjects
    ###assign_new_subject
    def __repr__(self):
        return 'Professor Name = %s , Subjects_Taught = %s' % (self.prof_name , ','.join(self.subjects_taught))
