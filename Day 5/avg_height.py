# 🚨 Don't change the code below 👇
sum = 0
count = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
    sum = student_heights[n] + sum
    count += 1

avg = round(sum/count)
print(avg)



