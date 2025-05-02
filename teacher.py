from person import Person


class Teacher(Person):
   def __init__(self, name, birthyear, employee_id, subject, salary):
        super().__init__(name, birthyear)
       self.__employee_id = employee_id
       self.__subject = subject
       self.__salary = salary
  
   #Getter and Setters
   def get_employee_id(self):
       return self.__employee_id
   def set_employee_id(self, employee_id):
       self.__employee_id = employee_id
   def get_subject(self):
       return self.__subject
   def set_subject(self, subject):
       self.__subject = subject
   def get_salary(self):
       return self.__salary
   def set_salary(self, salary):
       self.__salary = salary
#introduce self
   def introduce_self(self):
      super().introduce_self()
   print("i am a {self.__subject} teacher at WL High School")
