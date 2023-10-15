'''
implement a function called sort_students that takes a list of student onjects as input and sorts the
list based on their CGPA (cumulative grade point average) in descending order. each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). test the function
with different input lists of students. 
'''

class Student:
  def __init__(self, name, roll_number, cgpa):
    self.name = roll_number
    self.roll_number = roll_number
    self. cgpa = cgpa



def sort_students(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, 
      key=lambda student: student.cgpa,
      reverse=True)
  # Syntax
  return sorted_students


# Example usage:
students = [
  Student("Hari", "A123", 7.8),
  Student("Srikanth", "A124", 8.9),
  Student("Saumya", "A124", 9.1),
  Student("Mahidhar", "A126", 9.9),
]
sorted_students = sort_students(students)


# print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:  {}".format(student.name,
                                        student.roll_number, 
                                                   student.cgpa))
  

