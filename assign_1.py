import pickle

class Students:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self.student_number = student_number
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.country_of_birth = country_of_birth

    # getter methods
    def get_student_number(self):
        return self.student_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_sex(self):
        return self.sex

    def get_country_of_birth(self):
        return self.country_of_birth

    # Setter methods
    def set_student_number(self, student_number):
        self.student_number = student_number

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def set_sex(self, sex):
        self.sex = sex

    def set_country_of_birth(self, country_of_birth):
        self.country_of_birth = country_of_birth

def write_to_file(filename, student_arr):
    try:
        f = open(filename, mode='wb')
        ff = open("StudentsDataBase.txt",'w')
        for student in student_arr:
            pickle.dump(student, f)
            ff.write(str(student.get_student_number())+" "+student.get_first_name() +" "+ student.get_last_name()+" "+str(student.get_date_of_birth())+" "+student.get_sex()+" "+student.get_country_of_birth()+"\n")
    finally:
        f.close()

def read_from_file(filename):
    student_arr = []
    try:
        f = open(filename, mode = 'rb')
        while True:
            try:
                student = pickle.load(f)
                student_arr.append(student)
            except EOFError:
                break
    finally:
        f.close()
    return student_arr

def add_student(student_arr, filename):

    student_number = int(input("Enter student number: "))
    student_first_name = input("Enter student first name: ")
    student_last_name = input("Enter student last name: ")
    student_date_of_birth = int(input("Enter student year of birth: "))
    student_sex = input("Enter student sex: ")
    student_country = input("Enter student country of birth: ")
    student_arr.append(Students(student_number, student_first_name, student_last_name, student_date_of_birth, student_sex, student_country))
    write_to_file(filename, student_arr)
    print("A student was added successfully")

def find_student(student_arr):
    found = []
    student_number = int(input("Enter Student number to view the student information: "))
    for student in student_arr:
        if student.get_student_number() == student_number:
            found.append(student)
            break
    if (len(found) == 0):
        print("The Student is not registered in the system.")
        return
    show_all_students(found)

def show_all_students(student_arr):
    print(f"{'ID':<10}{'FIRST NAME':^20}{'LAST NAME':^30}{'BIRTH YEAR':>10}{'AGE':>15}{'SEX':>15}{'COUNTRY OF BIRTH':>25}")
    for student in student_arr:
        age = 2023-int(student.get_date_of_birth())
        print(
            f"{student.get_student_number():<10}{student.get_first_name():^20}{student.get_last_name():^30}{student.get_date_of_birth():>10}{age:>14}{student.get_sex():>15}{student.get_country_of_birth():>21}")

def show_all_students_born_on_given_year(student_arr):
    year = int(input("Enter year: "))
    found = []
    for student in student_arr:
        if student.get_date_of_birth() == year:
            found.append(student)
    if (len(found) == 0):
        print("No student found in the given year")
        return
    show_all_students(found)

def modify_student(student_arr, filename):
    student_number = int(input("Enter Student number you want to modify details for: "))
    flag = True
    for student in student_arr:
        if student.get_student_number() == student_number:
            flag = False
            print("Which informatin you would like to modify:\n1-Student Number\n2-First Name\n3-Last Name\n4-Year of birth\n5-Sex\n6-Country of Birth\n")
            x = int(input("Enter the number of the operation: "))
            if x == 1:
                student_number = input("Enter new student number: ")
                student.set_student_number(student_number)
            elif x == 2:
                student_first_name = input("Enter new first name: ")
                student.set_first_name(student_first_name)
            elif x == 3:
                student_last_name = input("Enter new last name: ")
                student.set_last_name(student_last_name)
            elif x == 4:
                student_yob = input("Enter new year of birth: ")
                student.set_date_of_birth(student_yob)
            elif x == 5:
                student_sex = input("Enter sex: ")
                student.set_sex(student_sex)
            elif x == 6:
                student_cob = input("Enter country of birth: ")
                student.set_country_of_birth(student_cob)
            break
    if (flag):
        print("Student record not found.")
    else:
        print("The Student Record is updated.")
        write_to_file(filename, student_arr)

def delete_student(student_arr, filename):
    student_number = int(input("Enter Student number you want to delete: "))
    flag = True
    for student in student_arr:
        if student.get_student_number() == student_number:
            flag = False
            student_arr.remove(student)
            break
    if (flag):
        print("Student record not found.")
    else:
        print("Record deleted.")
        write_to_file(filename, student_arr)

student_array =[Students(20910394,"Hassan","Mahamat",2000,"M","Jeddah"),Students(20911131,"Nour","Barakat",2001,"F","Kwait"),Students(19071169,"Aziz","bin Afif",2000,"M","Saudi")]

message = "STUDENTS INFORMATION PROGRAM"
print('{:^100}'.format(message))

counter = -1
while(counter != 9):
    print("{:^100}".format("PROGRAM MENU"))
    print(" 1-Write Student information to a file\n 2-Read Student information from file\n 3-Add a student\n 4-Find a student by student number\n 5-Display all Students information\n 6-Show all students based on year of birth\n 7-Modify a student \n 8-Delete a student \n 9-Quit")
    choice = int(input("Choose an operation to be perform: "))

    if choice == 1:
        write_to_file("students.txt", student_array)
    elif choice == 2:
        student_array = read_from_file("students.txt")
    elif choice == 3:
        add_student(student_array, "students.txt")
    elif choice == 4:
        find_student(student_array)
    elif choice == 5:
        show_all_students(student_array)
    elif choice == 6:
        show_all_students_born_on_given_year(student_array)
    elif choice == 7:
        modify_student(student_array, "students.txt")
    elif choice == 8:
        delete_student(student_array, "students.txt")
    elif choice == 9:
        print("YOU QUITED THE PROGRAM")
        break
    else:
        print("You have entered invalid choice!!")
        print("please enter valid choice from 1 - 9")
        continue
