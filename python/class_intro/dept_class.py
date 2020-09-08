class Course:
    #Initiating constructor of class Course 
    def __init__(self,course_name,semester,related_dept,capacity=10):
        self.course_name = course_name
        self.semester = semester
        self.capacity = capacity
        self.related_dept = related_dept
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
            
class Professor:
    def __init__(self,prof_name, subjects_taught = []):
        self.prof_name = prof_name
        self.subjects_taught = subjects_taught

    def __repr__(self):
        return 'Professor Name = %s , Subjects_Taught = %s' % (self.prof_name , ','.join(self.subjects_taught))

class Department:
    def __init__(self,dept_name,HOD_name):
        self.HOD_name = HOD_name
        self.dept_name = dept_name
  
    def assign_course_to_professor(self,professor,course):
        prof_list = []
        course_list = []
        if professor.prof_name not in prof_list:
            prof_list.append(professor.prof_name) 
        for each in professor.subjects_taught:
            if each not in course_list:
                course_list.append(professor.prof_name)
        print (course_list)

    def check_hod(self,professor):
        if self.HOD_name == professor.prof_name:
            print ('Mr.',professor.prof_name, 'is the HOD of' ,self.dept_name, 'Department')
        else:
            print ('Mr.',professor.prof_name, 'is not the HOD of', self.dept_name, 'Department')

    def __repr__(self):
        return 'Department = %s, HOD = %s'  % (self.dept_name , self.HOD_name)



 
