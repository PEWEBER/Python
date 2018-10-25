#--------------------------------------------------------
# File------------project4.py
# Developer-------Paige Weber
# Course----------CS1213-03
# Project---------Project #4
# Due-------------October 17th, 2017
#
# This program computes a students semester average
# and letter grade for this course.
#--------------------------------------------------------
lowest_quiz = 10
overall_quiz = 0
count = 1
quiz_score = 0

while quiz_score <= 10:
    quiz_score = float(input("Quiz #%1.0f ----- "%count))
    if quiz_score < 0:
        end = quiz_score
        break
    else:
        if quiz_score < lowest_quiz:
            lowest_quiz = quiz_score
        count = count + 1
        overall_quiz = overall_quiz + quiz_score
quiz_average = (overall_quiz - lowest_quiz) / (count - 2)
quiz_average = quiz_average * 10

quiz_weight = quiz_average * .15


print()

count2 = 1
overall_program = 0
program_score = 0

while program_score <=10:
    program_score = float(input("Program #%1.0f -- "%count2))
    if program_score < 0:
        end2 = program_score
        break
    else:
        count2 = count2 + 1
        overall_program = overall_program + program_score
program_average = overall_program / (count2 - 1)
program_average = program_average * 10

program_weight = program_average * .2   

print()

midterm1_score = float(input("Exam #1 ----- "))
midterm1_weight = midterm1_score * .2
midterm2_score = float(input("Exam #2 ----- "))
midterm2_weight = midterm2_score * .2

print()

final_score = float(input("Final Exam -- "))
final_weight = final_score * .25

print()

average = quiz_weight + program_weight + midterm1_weight + midterm2_weight + final_weight
print("Average -----", average)

if average >= 90:
    print("Grade ------- A")
if average >= 80 and average < 90:
    print("Grade ------- B")
if average >= 70 and average < 80:
    print ("Grade ------- C")
if average >= 60 and average < 70:
    print("Grade ------- D")
if average >= 0 and average < 60:
    print("Grade ------- F")
                    



                    

    
    


