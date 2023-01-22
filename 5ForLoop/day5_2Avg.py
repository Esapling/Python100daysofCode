# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

sum = 0
len = 0
for h in student_heights:
    sum += h
    len +=1
#Write your code below this row 👇
avg = round(sum /len)
print(avg)



