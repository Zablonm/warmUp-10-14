from typing import List




class Course:
   def __init__(self, name:str, students:List[object], teacher:object):
       self.__name = name
       self.__students = students
       self.__teacher = teacher


   #Getter and Setters
   def get_name(self):
       return self.__name
   def set_name(self, name: str):
       self.__name = name
   def get_students(self):
       return self.__students
   def get_teacher(self):
       return self.__teacher
   def set_teacher(self, teacher: object):
       self.__teacher = teacher
   def add_student(self, student: object):
       for x in self.__students:
           if x.get_student_id() == student.student_id():
               print("Student {x.__name} already exists")
         
      
       self.__students.append(student)
       print(f"Student {student.get_name()} added to {self.__name} course.")


   def get_course_info(self):
       print(self.__name)
       print("Teacher: ", self.__teacher.get_name())
       print ("Students: ")
       for x in self.__students:
           print(x.get_name())

