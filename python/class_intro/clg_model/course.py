class Course:
    #Initiating constructor of class Course 
    def __init__(self,course_name,semester,capacity=10):
        self.course_name = course_name
        self.semester = semester
        self.capacity = capacity
        #Creating empty list to store enrollments of students in a course
        self.enrollments = []
    #repr function for representing course details     
    def __repr__(self):
        enrolls = []
        for each in self.enrollments:
            #Appending only roll_nos of students in course details
            enrolls.append(str(each.roll_no))
        a = ",".join(enrolls)
        return 'Course name = %s , Semester = %s , Enrollments = %s, count = %s' % (self.course_name , self.semester , a , len(self.enrollments))
