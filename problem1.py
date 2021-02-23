"""
***************************************************
Filename: Life hack #2, problem1.py
Description: if statements for radar problem1
Author: Lee.M
Date: 23/02/2021
***************************************************
"""
# get variables
speed = int(input("Enter a speed as an integer"))

# compute fines
fine_1 = 100
fine_2 = 270
fine_3 = 570

# setting the fines
if speed > 0 or speed < 21:
  print ("You are speeding and your fine is $" + str(fine_1))
else:
  print ("Congratulations, you are within the speed limit!")

if speed > 20 or speed < 31:
  print ("You are speeding and your fine is $" + str(fine_2))
else: 
  print ("Congratulations, you are within the speed limit!")

if speed > 31:
  print ("You are speeding and your fine is $" + str(fine_3))
else:
  print ("Congratulations, you are within the speed limit!")



