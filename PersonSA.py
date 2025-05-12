from person import Person


class Teacher(Person):
   def __init__(self, name: str, birthyear: int, employee_id: str, subject: str, salary: int):
       super().__init__(name, birthyear)
       self.__employee_id = employee_id
       self.__subject = subject
       self.__salary = salary
  
   #Getter and Setters
   def get_employee_id(self):
       return self.__employee_id
   def set_employee_id(self, employee_id: str):
       self.__employee_id = employee_id
   def get_subject(self):
       return self.__subject
   def set_subject(self, subject: str):
       self.__subject = subject
   def get_salary(self):
       return self.__salary
   def set_salary(self, salary: int):
       self.__salary = salary
#introduce self
   def introduce_self(self):
       super().introduce_self()
       print(f"I am a {self.__subject} teacher at WL High School.")
       print(f"My employee ID is {self.__employee_id} and my salary is {self.__salary}.")
