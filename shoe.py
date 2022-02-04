
stu = input("How many numbers of students: ")
shoes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(int(stu)):
    shoe = input("Enter the Shoe size: ")
    shoes.append(float(shoe))
shoes.sort()
search_no = float(input("What number do u want to search: "))

count = shoes.count(search_no)
print(count)
print(shoes)
