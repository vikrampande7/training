class Department:
    def __init__(self,dept_name):
        ###student objects,prof obj , course obj
        ###3 methods 
        ###3 lists
        ###assign_new_hod method
        self.dept_name = dept_name

    def __repr__(self):
        return 'Department = %s'  % (self.dept_name)