class Student:
    #Initiating constructor of class Student
    def __init__(self,name,roll_no,year,department):
        self.name = name
        self.roll_no = roll_no
        self.year = year
        self.department = department
        #Empty list for storing courses 
        self.enrolled_courses = []
    #creating a method for a student to enroll for a course
    def enroll_to_course(self,course):
        #List of current semesters
        current_semester = ['I','III','V','VII']
        #Condition for checking the course capacity
        if self.department == course.related_dept:
            if len(course.enrollments) < course.capacity:
                #Checking the course availability on the basis of year
                if self.year == 'BE':
                    #Checking the availability on the basis of semester
                    if course.semester == 'VII' or course.semester == 'VIII': 
                        if course.semester in current_semester:
                            #Appending the selected course in the enrolled_courses list
                            self.enrolled_courses.append(course)
                            #Appending all student objects in the course enrollments list  
                            course.enrollments.append(self)
                        else:
                            print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                    else:
                        print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year)

                elif self.year == 'TE':
                    if course.semester == 'V' or course.semester == 'VI':
                        if course.semester in current_semester:
                            self.enrolled_courses.append(course)
                            course.enrollments.append(self)
                        else:
                            print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                    else:
                        print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year)

                elif self.year == 'SE':
                    if course.semester == 'III' or course.semester == 'IV':
                        if course.semester in current_semester:
                            self.enrolled_courses.append(course)
                            course.enrollments.append(self)
                        else:
                            print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                    else:
                        print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year)

                elif self.year == 'FE':
                    if course.semester == 'I' or course.semester == 'II':
                        if course.semester in current_semester:
                            self.enrolled_courses.append(course)
                            course.enrollments.append(self)
                        else:
                            print ("can't enroll", self.name ,':', course.course_name, 'is not available in current semester')
                    else:
                        print ("Can't enroll" ,self.name,':', course.course_name, 'is not available for',self.year) 
            else:
                print ("Cannot enroll student: ",self.name , ',capacity is full')
        else:
            print('Cannot enroll Student: ',self.name ,',Department does not match')
    #repr function for representing student data
    def __repr__(self):
        enrolls = []
        for each in self.enrolled_courses:
            #Appending only course_name in student details
            enrolls.append(str(each.course_name))
        a = ", ".join(enrolls)
        return 'Student Name = %s , Roll_no = %d , Year_studying_in = %s , Department = %s Enrolled_courses  = %s' % (self.name , self.roll_no , self.year ,self.department,a)
