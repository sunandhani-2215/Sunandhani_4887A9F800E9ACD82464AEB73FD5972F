'''
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA(Cumulative Grade Point Average) in ascending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float).Test the function
with different important lists of students.
'''

class Student:

  def __init__(self,name,roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sorted_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
       key=lambda student: student.cgpa,
       reverse=True)   
  return sorted_students


# Example usage
students = [
    Student("Hari", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Sowmiya", "A125", 9.1),
    Student("Mahi", "A126", 9.9),
]

students = sorted_students(students)

#Print the sorted list of students
for student in students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,
                                                     student.cgpa))