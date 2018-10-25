#--------------------------------------------------------
# File------------project3.py
# Developer-------Paige Weber
# Course----------CS1213-03
# Project---------Project #3
# Due-------------October 5th, 2017
#
# This program computes how long it will take to pay
# off a loan and how much total interest is paid.
#--------------------------------------------------------
original_principal = float(input("Principal-------- "))
annual_interest = int(input("Annual interest-- "))
monthly_payment = float(input("Monthly payment-- "))
monthly_interest = (annual_interest/12) * .01

month = 0
principal = original_principal
old_minus_principal = 0
old_interest = 0


if monthly_payment < original_principal * monthly_interest:
    print()
    print("Loan not approved.")

else:
    while principal > 0:
        minus_principal = monthly_payment - (principal * monthly_interest)

        total_interest = (principal * monthly_interest) + old_interest
        old_interest = total_interest

        month = month + 1
        principal = original_principal - minus_principal - old_minus_principal
        old_minus_principal = minus_principal + old_minus_principal


    interest = total_interest

    print()
    print("Months   :", month)
    print("Interest : $%5.2f"%interest)
