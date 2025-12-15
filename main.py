from tabulate import tabulate

students =[{
    "student_id" : 1,
    "name" : "Andi",
    "class" : "10A",
    "gender" : "Male",
    "age" : 18,
    "email" : "Andi@gmail.com",
    "score" : 80,
},
{
    "student_id" : 2,
    "name" : "Budi",
    "class" : "10A",
    "gender" : "Male",
    "age" : 18,
    "email" : "Budi@gmail.com",
    "score" : 90,
},
{
    "student_id" : 3,
    "name" : "Cici",
    "class" : "10A",
    "gender" : "Female",
    "age" : 17,
    "email" : "Cici@gmail.com",
    "score" : 85,
},
{
    "student_id" : 4,
    "name" : "Dina",
    "class" : "10A",
    "gender" : "Female",
    "age" : 17,
    "email" : "Dina@gmail.com",
    "score" : 75,
},
{
    "student_id" : 5,
    "name" : "Eka",
    "class" : "10A",
    "gender" : "Male",
    "age" : 18,
    "email" : "Eka@gmail.com",
    "score" : 95,
},
{
    "student_id" : 6,
    "name" : "Fina",
    "class" : "10A",
    "gender" : "Female",
    "age" : 17,
    "email" : "Fina@gmail.com",
    "score" : 85,
},
{
    "student_id" : 7,
    "name" : "Gina",
    "class" : "10A",
    "gender" : "Female",
    "age" : 17,
    "email" : "Gina@gmail.com",
    "score" : 75,
}
]

def display_main_menu():
    print("Student Data Score Main Menu:")
    print("1. Read all data")
    print("2. Create new data")
    print("3. Update existing data")
    print("4. Delete existing data")
    print("5. Exit")

def display_read_menu():
    print ("=================================================")
    print("Read Sub Menu:")
    print ("=================================================")
    print("1. Read all data")
    print("2. Read data by Student ID")
    print("3. Back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_all()
    elif choice == "2":
        id = int(input("Enter student ID: "))
        read_by_id(id)
    elif choice == "3":
        main()
    else:
        print("Invalid choice")
        display_read_menu()

def read_all():
    print(tabulate(students, headers="keys", tablefmt="fancy_grid"))
    display_read_menu()
    

def read_by_id(id):
    for student in students:
        if student["student_id"] == id:
            print(tabulate([student], headers="keys", tablefmt="fancy_grid"))
            display_read_menu()
            
          
    print("Data not found")
    print("would you like to create new student?")
    choice = input("Enter your choice: ").lower()
    if choice == "yes":
        create_student()
    display_read_menu()
    return
    
def read_by_email(email):
    for student in students:
        if student["email"] == email:
            print(tabulate([student], headers="keys", tablefmt="fancy_grid"))
            return
        print("would you like to create new student?")
        choice = input("Enter your choice: ").lower()
        if choice == "yes":
            create_student()
        display_read_menu()
        return


def display_create_menu():
    print ("=================================================")
    print("Create Sub Menu:")
    print ("=================================================")
    print("1. Create student")
    print("2. Back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        main()
    else:
        print("Invalid choice")
        display_create_menu()


def create_student():
    newStudent = {}
    newId = int(input("Enter student ID ex: numeric: "))

    for student in students:
        if student["student_id"] == newId:
            print("ID already exists")
            display_create_menu()
            
        
    newStudent["student_id"] = newId
    newStudent["name"] = input("Enter name: ").capitalize()
    newStudent["class"] = input("Enter class: ").capitalize()
    newStudent["gender"] = input("Enter gender: ").capitalize()
    newStudent["age"] = int(input("Enter age: "))

    newEmail = input("Enter email: ")

    for student in students:
        if student["email"] == newEmail:
            print("Email already exists")
            display_create_menu()
            return
        
    newStudent["email"] = newEmail
    newStudent["score"] = int(input("Enter score: "))

    students.append(newStudent)

    print("Data created successfully")
    print (tabulate([newStudent], headers="keys", tablefmt="fancy_grid"))
    display_create_menu()


def display_update_menu():
    print ("=================================================")
    print("Update Sub Menu:")
    print ("=================================================")
    print("1. Update student")
    print("2. Back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        update_student()
    elif choice == "2":
        main()
    else:
        print("Invalid choice")
        display_update_menu()

def update_student():
    id = int(input("Enter student ID: "))

    selectedStudent = None

    for student in students:
        if student["student_id"] == id:
            selectedStudent = student
   
    if selectedStudent is None:
        print("Data not found")
        print("would you like to create new student?")
        choice = input("Enter your choice: ").lower()
        if choice == "yes":
            create_student()

        display_update_menu()
    
    print("select column to edit")
    print("1. name")
    print("2. class")
    print("3. gender")
    print("4. age")
    print("5. email")
    print("6. score")
    print("7. edit all column")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        selectedStudent["name"] = input("Enter name: ").capitalize()
    elif choice == 2:
        selectedStudent["class"] = input("Enter class: ").capitalize()
    elif choice == 3:
        selectedStudent["gender"] = input("Enter gender: ").capitalize()
    elif choice == 4:
        selectedStudent["age"] = int(input("Enter age: "))

    elif choice == 5:
        newEmail = input("Enter email: ")
        for student in students:
            if student["email"] == newEmail:
                print("Email already exists")
                display_update_menu()

        selectedStudent["email"] = newEmail

    elif choice == 6:
        selectedStudent["score"] = int(input("Enter score: "))
    elif choice == 7:
        update_all_column(selectedStudent)
    else:
        print("Invalid choice")
        display_update_menu()
        return

    print("Data updated successfully")
    print (tabulate([selectedStudent], headers="keys", tablefmt="fancy_grid"))
    display_update_menu()

def update_all_column(student): 
        student["name"] = input("Enter name: ").capitalize()
        student["class"] = input("Enter class: ").capitalize()
        student["gender"] = input("Enter gender: ").capitalize()
        student["age"] = int(input("Enter age: "))

        student["email"] = input("Enter email: ")
        newEmail = input("Enter email: ")
        for student in students:
            if student["email"] == newEmail:
                print("Email already exists")
                display_update_menu()

        student["email"] = newEmail

        student["score"] = int(input("Enter score: "))
        print("would you like to save the changes?")
        choice = input("Enter your choice: ").lower()
        if choice == "yes":
            print("Data updated successfully")
            print (tabulate([student], headers="keys", tablefmt="fancy_grid"))
        else:
            print("Data not saved")


def display_delete_menu():
    print ("=================================================")
    print("Delete Sub Menu:")
    print ("=================================================")
    print("1. Delete student")
    print("2. Back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        delete_student()
    elif choice == "2":
        main()
    else:
        print("Invalid choice")
        display_delete_menu()

def delete_student():
    id = int(input("Enter student ID: "))
    selectedStudent = None

    for student in students:
        if student["student_id"] == id:
            selectedStudent = student

    if selectedStudent is None:
        print("Data not found")
        display_delete_menu()
        return

    print("Are you sure you want to delete this data?")
    choice = input("Enter your choice: ").lower()
    if choice == "yes":
        students.remove(selectedStudent) 
        print("Data deleted successfully")
        print (tabulate(students, headers="keys", tablefmt="fancy_grid"))
    display_delete_menu()


def main():
    display_main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        display_read_menu()
    elif choice == "2":
        display_create_menu()
    elif choice == "3":
        display_update_menu()
    elif choice == "4":
        display_delete_menu()
    elif choice == "5":
        print("Goodbye!")
        return
    else:
        print("Invalid choice")
        main()

if __name__ == "__main__":
    main()