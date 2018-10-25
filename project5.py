#--------------------------------------------------------
# File------------project5.py
# Developer-------Paige Weber
# Course----------CS1213-03
# Project---------Project #5
# Due-------------November 2nd, 2017
#
# This program computes a student's semester average
# and letter grade for this course using files.
#--------------------------------------------------------

import os.path
rawinput = input("Select input file: ")
if os.path.exists(rawinput):
    inputfile = open(rawinput, 'r')
    rawoutput = input ("Select output file: ")
    outputfile = open(rawoutput, 'w')
    
    
    while True: 
        name = inputfile.readline()
        if name == " ":
            break

        else:
            quiz_list = inputfile.readline()
            quiz_list = quiz_list.split()
            quizcount = len(quiz_list)
            qu_list = []
        
        
            for item in quiz_list:
                qu_list.append(float(item))
           
                lowest_quiz = 100
                for item in qu_list:
                    if item < lowest_quiz:
                        lowest_quiz = item
                
                overall_quiz = sum(qu_list)
                if quizcount == 1:
                    quiz_average = overall_quiz
                else:
                    quiz_average = (overall_quiz - lowest_quiz) / (quizcount - 1)

                quiz_weight = quiz_average * 1.5
       

                           
        program_list = inputfile.readline()
        program_list = program_list.split()
        procount = len(program_list)
        pro_list = []
        
        for item in program_list:
            pro_list.append(float(item))

            overall_program = sum(pro_list)
    
        if procount == 0:
            program_average = overall_program
        else:
            program_average = overall_program / procount
                
        program_weight = program_average * 2
        

        
        exam_list = inputfile.readline()
        exam_list = exam_list.split()
        ex_list =[]

        for item in exam_list:
            ex_list.append(float(item))
        if ex_list == []:
            break
        midterm1 = ex_list[0]
        midterm2 = ex_list[1]
        final = ex_list[2]

        midterm_overall_weight = (midterm1 * .2) + (midterm2 * .2)
        final_weight = final * .25
      
        
        average = quiz_weight + program_weight + midterm_overall_weight + final_weight

        if average >= 90:
            grade = "A"
        if average >= 80 and average < 90:
            grade = "B"
        if average >= 70 and average < 80:
            grade = "C"
        if average >= 60 and average < 70:
            grade = "D"
        if average < 60:
            grade = "F"


        name = name.strip()
        outputfile.write("%-20s"%name + " " + "%3.1f"%average + " "+ grade + '\n')


    inputfile.close()
    outputfile.close()

else:
    print("File does not exist.")
        
    


