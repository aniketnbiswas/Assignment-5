student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88,
    "Fiona": 72,
    "George": 81,
    "Hannah": 90,
    "Ian": 65,
    "Julia": 98
}

l=str(student_grades.keys())

name=input(r"Enter student's name: ")

try:
    print(fr"{name}'s marks: {name[student_grades]}")
except TypeError:
    print("Student not found")
