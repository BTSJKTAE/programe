
stu = input("How many numbers of students: ")
ages = []

for i in range(int(stu)):
    age = input("Enter the age: ")
    ages.append(int(age))
ages.sort()
print(ages)
