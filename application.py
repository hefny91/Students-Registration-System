import classes as reg ## load additional file includes all classes and functions used, must be located with this file
import pickle ## a module that allow data saving

print('\n' + 'Welcome to Students registration system \n') ## welcome message to users

#Data Persistence configuration using pickle
load_existing = input('Do you want to load existing data? Enter Yes or No: ')
load_existing = load_existing.lower()

if load_existing == 'yes':
    file_path = input('Please enter the file backup name "ex. final": ') #must be a .pickle file
    pickle_file = open(file_path, 'rb')
    institution = pickle.load(pickle_file) #load existing regsitration

else: #create a new institution class to enter brand-new data
    name = input('Please enter an institution name: ')
    institution = reg.Institution(name)
    print('\n' + 'Welcome to the Registration System \n')

## menu includes basic tasks
menu_string = '\n' + 'Please select an option from the following:' + '\n\n' + \
                'MENU' + '\n' + \
                '----------------------------------------' + '\n' + \
                '1 Create New Course' + '\n' + \
                '2 Activate Course for Registeration' + '\n' + \
                '3 Show available courses' + '\n' + \
                '4 Register Student to the system' + '\n' + \
                '5 Enroll a student for a course' + '\n' + \
                '6 List Registered students' + '\n' + \
                '7 List enrolled student to a course' + '\n' + \
                '8 Quit registration system' + '\n'

valid_options = ['1','2','3','4','5','6','7','8'] # valid options to select

while True:
    while True:
        var = input('\n ...press enter to continue...')
        if not(var):
            print(menu_string)
            menu_input = input('Enter Menu Choice: ')
            break
        else:
            print('Press enter to continue')
    if menu_input == '8': # if key 8 entered -> mapped to exit function and save progress
        print('\n' + 'EXITING...Thank you!' + '\n')
        break
    elif menu_input in valid_options: ## validation option to prevent choosing wrong number
##################################################################################################
        if menu_input == '1':         #OPTION 1 - Create New Course
            name = input('Please enter name: ')
            course = reg.Course(name) #create a course object
            institution.add_course(course) #add course
            print('\n' + course.name + ' added to course list!' + '\n')
##################################################################################################
        elif menu_input == '2':  #OPTION 2 - Activate Course for Registeration
            while True:
                key = input('Course Name: ')
                if key in institution.course_catalog.keys():
                    course = institution.course_catalog[key]
                    break
                else:
                    print('This course is not currently offered. Please add new course or select from the following offerings: ')
            course_offering = reg.CourseOffering(course)
            institution.add_course_offering(course_offering)
            print('\n' + course_offering.__str__() + ' has been scheduled!' + '\n')
##################################################################################################
        elif menu_input == '3':       #OPTION 3 -  Show available courses
            institution.list_course_catalog()
##################################################################################################
        elif menu_input == '4': #OPTION 4 - Register Student to the system
            first_name = input('First name: ')
            last_name = input('Last name: ')
            username = input('Assign unique username: ') #will be used to select user to join course
            student = reg.Student(first_name, last_name, username)
            institution.enroll_student(student) #fill data to student class in classes file
            print('\n' 'Student ' + student.first_name + ' ' + student.last_name + ' has been enrolled!'+'\n')
##################################################################################################
        elif menu_input == '5': #OPTION 5 - REGISTER A STUDENT FOR A COURSE
            while True:
                username = input('Student username: ')
                if username in institution.student_list.keys():
                    student = institution.student_list[username]
                    break
                else:
                    print('Student username not found, please enroll student or try again')
            while True:
                course_name = input('Course name: ')
                if course_name in institution.course_catalog.keys():
                    break
                else:
                    print('Course name not found, please enter valid coursename')
            institution.register_student_for_course(student,course_name)
##################################################################################################
        elif menu_input == '6': #OPTION 6 - List Registered students
            institution.list_students()
##################################################################################################
        elif menu_input == '7': #OPTION 7 - LIST STUDENTS REGISTERED FOR A COURSE
            while True:
                course_name = input('Course name: ')
                if course_name in institution.course_catalog.keys():
                    break
                else:
                    print('Course name not found, please enter valid coursename')
            institution.list_registered_students(course_name)
##################################################################################################
    else:
        print('\n' + 'INVALID MENU OPTION: Please try again' + '\n') ## error message appears when enter invalid option
##################################################################################################
save_session = input('Would you like to the contents of this session? Enter Yes or No: ') # save session after selecting number 8 to exit
save_session = save_session.lower() #save session function - related to pickle module
##################################################################################################
#configuration related to saveing if user typed "yes".
if save_session == 'yes':
    file_name = input('Please enter a filename for saving your data (this is a .pickle file): ')
    pickle_file = open(file_name, 'wb')
    pickle.dump(institution, pickle_file)
    pickle_file.close
    print('Session contents saved, goodbye!')
##################################################################################################
# if user do not want to save data then application will be closed
else:
    print('Goodbye!')
