#--------------------------------------------------------
# File------------project1.py
# Developer-------Paige Weber
# Course----------CS1213-03
# Project---------Project #1
# Due-------------September 14, 2017
#
# This program computes an itemized bill for an online
# music retailer.
#--------------------------------------------------------

subscription = float(input("Subscription charge- "))
number_of_tunes = float(input("Tunes downloaded---- "))

download_fee = number_of_tunes * 1.29
donation = download_fee * .1
tax = (download_fee + subscription - donation) * .06
total = download_fee + subscription + tax

print()
print("Subscription-------- $%6.2f"%subscription)
print("Download fee-------- $%6.2f"%download_fee)
print("Tax----------------- $%6.2f"%tax)
print("Total--------------- $%6.2f"%total)
print()
print("Donation------------ $%6.2f"%donation)



