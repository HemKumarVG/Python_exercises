"""
Brilliant School sets an exam wherein, 
    English exam is for 80 marks, 
    Science for 90 marks and 
    Mathematics for 100 marks. 

Ask the student to enter the marks scored in each of these exams. 
Calculate the total percentage marks and rank the student as below :
   - First Class if score is more than or equal to 90 %
   - Second Class if score is more than or equal to 75%
   - Average if student has not failed
   - Failed if score is less than or equal to 35 %

"""

def cls(score):
    if score >= 90:
        print("first class")
    elif score >= 75:
            print("Second class")
    elif score <= 35:
            print("Failed")
    else:
        print("average")

            
print("enter the marks scored in each of these exams")
english_scored = int(input("enter the marks scored in english: "))
science_scored = int(input("enter the marks scored in science: "))
mathematics_scored = int(input("enter the marks scored in maths: "))

total_marks = english_scored + science_scored + mathematics_scored
max_marks = 80 + 90 + 100

percentage = (total_marks / max_marks) * 100

result = cls(percentage)


                


                        




