subject1_martks = 80
subject2_marks = 80
subject3_marks = 80
student_marks1 = int(input("Enter student1 marks: "))
student_marks2 = int(input("Enter student2 marks: "))
student_marks3 = int(input("Enter student3 marks: "))

subject1_percentage = (student_marks1 / subject1_martks) * 100
subject2_percentage = (student_marks2 / subject2_marks) * 100
subject3_precentage = (student_marks3 / subject3_marks) * 100
if subject1_percentage >= 33 and subject2_percentage >= 33 and subject3_precentage >= 33:
    print("Student is pass")
else:
    print("Student is fail")