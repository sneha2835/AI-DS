class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_avg(self):
        return sum(self.marks) / len(self.marks)

def get_avg_marks(students):
    avg_marks = {}
    for student_name, marks in students.items():
        student = Student(student_name, marks)
        avg_marks[student_name] = round(student.calculate_avg(), 2)
    return avg_marks

def get_top_performer(avg_marks):
    top_performer = max(avg_marks, key=avg_marks.get)
    return top_performer

# Input data
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

# Calculate average marks
avg_marks = get_avg_marks(students)
print("Average Marks:", avg_marks)

# Identify the top performer
top_performer = get_top_performer(avg_marks)
print("Top Performer:", top_performer)
