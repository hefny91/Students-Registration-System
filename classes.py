class Course: ## Creating course object
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (self.name)

class CourseOffering: ## Allowing course to be selected in registering students
    def __init__(self, course):
        self.course = course
        self.registered_students = [] #keep a list of registered students

    def register_students(self, *args):
        for arg in args:
            self.registered_students.append(arg)
            arg.course_list.append(self) #add courseoffering to list of this student's course

    def __str__(self):
            return (self.course.name)

class Institution:
    def __init__(self, name): #adding a domain to constructor
        self.name = name
        self.student_list = {} #key = student username
        self.course_catalog = {} #key = course name
        self.course_schedule = {} #key = course name

    def list_students(self):
        print('\n' + 'Enrolled Students (' + self.name + ') \n' + '-------------------------------------------')
        slist = [x.last_name + ', ' + x.first_name for x in self.student_list.values()]
        student_list = sorted(slist)
        for x in student_list:
            print(x)
        print('\n')

    def enroll_student(self, student):
        if isinstance(student,Student):
            if student.username in self.student_list.keys():
                print(student.first_name + ' ' + student.last_name + ' is already enrolled!')
            else:
                self.student_list[student.username] = student
        else:
            raise TypeError('Only accepts student object')

    def register_student_for_course(self,student,course_name):
        for offering in self.course_schedule[course_name]:
            offering.register_students(student)
            print('\n' + student.first_name + ' ' + student.last_name + ' has been enrolled ' + offering.__str__() +'\n')

    def list_course_catalog(self):
        print('\n' + 'Course Catalog (' + self.name + ') \n' + '----------------------------------------')
        for item in self.course_catalog.values():
            print(item.__str__())
        print('\n')

    def list_registered_students(self,course_name):
        for offering in self.course_schedule[course_name]:
                print('Registered Students List (' + offering.__str__() + ') \n' + '------------------------------------------------------------')
        for student in offering.registered_students:
                print(student.first_name + ' ' + student.last_name) #list of students registered

    def add_course(self, course): #this adds courses, NOT course offerings
        if isinstance(course, Course):
            if course.name in self.course_catalog.keys(): #validation to prevent recreation
                return 'Course has already been added'
            else:
                self.course_catalog[course.name] = course #otherwise create a new entry in our course catalog
        else:
            raise TypeError('Only accepts course object as argument')

    def add_course_offering(self, course_offering): ## function responsible for making course available to register
        if isinstance(course_offering, CourseOffering): #check for right instance
            if course_offering.course.name in self.course_catalog.keys(): #check to see if course in course catalog
                self.course_schedule.setdefault(course_offering.course.name, []) #sets default values to list
                self.course_schedule[course_offering.course.name].append(course_offering)
            else:
                return 'Please create a course before creating course offering'
        else:
            raise TypeError('Only accepts course offering as argument')

class Person: #person name related info - mapped to student
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

class Student(Person): #student class
    def __init__(self, last_name, first_name, username):
        Person.__init__(self, last_name, first_name, username)
        self.course_list = [] #list of offering objects
