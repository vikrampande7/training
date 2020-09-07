class Course:
    #Initiating constructor of class Course 
    def __init__(self,course_name,semester,capacity = 10):
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
            print ("Cannot enroll student: ",self.name , 'capacity is full')
    #repr function for representing student data
    def __repr__(self):
        enrolls = []
        for each in self.enrolled_courses:
            #Appending only course_name in student details
            enrolls.append(str(each.course_name))
        a = ", ".join(enrolls)
        return 'Student Name = %s , Roll_no = %d , Year_studying_in = %s , enrolled_course = %s' % (self.name , self.roll_no , self.year , a)
            
class Professor:
    def __init__(self,prof_name, subjects_taught = []):
        self.prof_name = prof_name
        self.subjects_taught = subjects_taught
        

    def __repr__(self):
        return 'Professor Name = %s , Subjects_Taught = %s' % (self.prof_name , ', '.join(self.subjects_taught))

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

    def check_hod(self,profes):
        if self.HOD_name == profes.prof_name:
            print (profes.prof_name, 'is the HOD of' ,self.dept_name )
        else:
            print (profes.prof_name, 'is not the HOD of', self.dept_name)

    def __repr__(self):
        return 'Department = %s, HOD = %s'  % (self.dept_name , self.HOD_name)



if __name__ == "__main__":


    dept1 = Department('E&TC','Vilas')
    dept2 = Department('Mechanical','Ajay')

    course1 = Course('VLSI','VIII')
    course2 = Course('EDC','IV')
    course3 = Course('SS','III')
    course4 = Course('Physics','I')
    course5 = Course('Microprocessor','V')
    course6 = Course('BCS','VII')
    course7 = Course('Maths','I')
    course8 = Course('DME','VII')
    course9 = Course('RAAC','V')
    course10 = Course('MQC','VI')
    course11 = Course('EEE','III')
    course12 = Course('Robotics','VIII')
    course13 = Course('Thermal Engineering','IV')
    course14 = Course('HT','V')

    prof1 = Professor('Kishor',['EDC','VLSI'])
    prof2 = Professor('Vilas',['SS','VLSI'])
    prof3 = Professor('Ninad',['Physics','Maths','Microprocessor'])
    prof1 = Professor('Vallabh',['Robotics','MQC','Maths'])
    prof2 = Professor('Nilesh',['HT','RAAC','MQC'])
    prof3 = Professor('Mihir',['EEE','DME','Physics'])

    stud = Student('Archis' , 4125 , 'BE','E&TC')
    stud1 = Student('Vikram',2122 , 'SE','E&TC')
    stud2 = Student('Arnav', 3170 , 'TE','E&TC')
    stud3 = Student('Vijay', 1962,'FE','E&TC')
    stud4 = Student('Soham', 2990,'SE','E&TC')
    stud5 = Student('Pranav', 3971,'TE','E&TC')
    stud6 = Student('Viraj', 4987,'BE','E&TC')
    stud7 = Student('Anil', 1910,'FE','E&TC')
    stud8 = Student('Girish',3861,'TE','E&TC')
    stud9 = Student('Vinit' , 4146 ,'BE', 'Mechanical')
    stud10 = Student('Dinesh',2091 , 'SE','Mechanical')
    stud11 = Student('Anand', 3683 , 'TE','Mechanical')
    stud12 = Student('Chinmay', 1500,'FE','Mechanical')
    stud13 = Student('Prasad', 2111,'SE','Mechanical')
    stud14 = Student('Ritesh', 3900,'TE','Mechanical')
    stud15 = Student('Parth', 4004,'BE','Mechanical')
    stud16 = Student('Siddhesh', 1991,'FE','Mechanical')
    stud17 = Student('Chirag',1144,'FE','Mechanical')

    print ('\n')
    print ('Students not enrolled')
    print ('-----------------------------')
    stud.enroll_to_course(course6)
    stud1.enroll_to_course(course3)
    stud2.enroll_to_course(course4)
    stud3.enroll_to_course(course4)
    stud4.enroll_to_course(course2)
    stud5.enroll_to_course(course5)
    stud6.enroll_to_course(course1)
    stud7.enroll_to_course(course5)
    stud3.enroll_to_course(course7)
    stud8.enroll_to_course(course5)
    stud9.enroll_to_course(course8)
    stud10.enroll_to_course(course11)
    stud11.enroll_to_course(course12)
    stud12.enroll_to_course(course9)
    stud13.enroll_to_course(course10)
    stud14.enroll_to_course(course14)
    stud15.enroll_to_course(course13)
    stud16.enroll_to_course(course11)
    stud17.enroll_to_course(course8)
    stud11.enroll_to_course(course12)

    print ('\n')
    print ('Department Details')
    print ('----------------')
    print (dept1)
    print (dept2)

    print ('\n')
    print ('Courses Details')
    print ('---------------')
    print (course1)
    print (course2)
    print (course3)
    print (course4)
    print (course5)
    print (course6)
    print (course7)


    print ('\n')
    print ('Professor Details')
    print ('----------------')
    print (prof1)
    print (prof2)
    print (prof3)
  
    print ('\n')
    print ('Students Details')
    print ('----------------')
    print (stud1)
    print (stud)
    print (stud2)
    print (stud3)
    print (stud4)
    print (stud5)
    print (stud6)
    print (stud7)
    print (stud8)   
