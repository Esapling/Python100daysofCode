# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max = 0
for score in student_scores:
    if score > max:
        max = score
print("The highest score in the class is : " + str(max))

# max() takes a list as an argumment
# maxVal = max(student_scores)
#print(maxVal)

