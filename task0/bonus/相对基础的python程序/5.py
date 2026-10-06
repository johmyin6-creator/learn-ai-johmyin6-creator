students={123456:"张三",123457:"李四",123458:"王五"}
for i in list(students.keys()):
    if i%2==0:
        students.pop(i)
print(students)