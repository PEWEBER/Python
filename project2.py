#--------------------------------------------------------
# File------------project2.py
# Developer-------Paige Weber
# Course----------CS1213-03
# Project---------Project #1
# Due-------------September 26, 2017
#
# This program uses Gregory-Leibniz series to compute
# an approximate value of pi.
#--------------------------------------------------------
number_of_terms = int(input("How many terms? "))
number_of_terms = number_of_terms + 1
if number_of_terms >= 1:

    add_approximation = 0

    for count in range (1, number_of_terms):
            approximation = (((-1)**(count + 1))/(2 * count - 1))
            add_approximation = approximation + add_approximation
    solution = add_approximation * 4

    print("Approxiation of pi: %1.5f"%solution)

else:
    print("The number of terms must be greater than zero.")
