class User: #parent class, 
    name = ''
    email = ''
    password = ''
    id = 0

class Student(User): #child class
    GPA = 3.2 #unique info about the Student class
    Year = "Freshman"

class Teacher(User): #child class
    Subject = "Geography" #unique info about the Teacher class
    Years_Teaching = 7
    
