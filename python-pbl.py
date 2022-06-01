import sys

class Student:
    def __init__(self,name,rollno,total_marks,isPass):
        self.name = ""
        self.rollno = 0
        self.total_marks =0
        self.isPass = False
         
    def insert(self,students):
        name = input("Enter student's name : ")
        rollno = int(input("Enter student's roll number : "))
        total_marks = int(input("Enter student's total marks : "))
        isPass = True
        if total_marks < 300:
            isPass = False
        newStudent = Student(name, rollno, total_marks,isPass )
        students.append(newStudent)
       
    def display(self, student):
            print("Name   : ", student.name)
            print("RollNo : ", student.rollno)
            print("Total Marks : ", student.total_marks)
            print("Result : ", student.isPass)
            print("\n")    
         
  
    def search(self, roll):
        for i in range(students.__len__()):
            if(students[i].rollno == roll):
                return i 
        return -1      
                                
    def delete(self, roll):
        i = student.search(roll)  
        del students[i]
  
         
students = []
student = Student('', 0, 0, 0)
  
print("Student Record Management system : ")
print("Enter 1 to insert new student record")
print("Enter 2 to view student record")
print("Enter 3 to search student record")
print("Enter 4 to delete student record")
choice = int(input("Enter choice : "))

while True:
    if choice == 1:
        student.insert(students)
    elif choice ==2:
        for i in range(students.__len__()):
            student.display(students[i])
    elif choice ==3:
        rollnumber = int(input("Enter roll number of student : "))
        if student.search(rollnumber) == -1:
            print("No records found")
        else:
            student.display(students[student.search(rollnumber)])
    elif choice ==4:
        rollnumber = int(input("Enter roll number of student : "))
        student.delete(rollnumber)
    else:
        sys.exit(0)
