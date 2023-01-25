student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for std in student_scores:
    str = ""
    if student_scores[std] > 90:
        student_grades[std] ="Outstanding"
    elif student_scores[std] > 80: 
        student_grades[std] ="Exceeds Expectations"
    elif student_scores[std] > 70:
        student_grades[std] = "Acceptable"
    else:
        student_grades[std] = "Fail"
        

    
    

# 🚨 Don't change the code below 👇
print(student_grades)