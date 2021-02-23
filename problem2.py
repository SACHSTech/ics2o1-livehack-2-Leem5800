"""
***************************************************
Filename: Life hack #2, problem2.py
Description: if statements, sides of a triangle
Author: Lee.M
Date: 23/02/2021
***************************************************
"""
# Determine side lengths
side_1 = int(input("Enter the length of side_1"))
side_2 = int(input("Enter the length of side_2"))
side_3 = int(input("Enter the length of side_3"))

# output result
print ("welcome to the Triangle Checker")
if side_1 + side_2 < side_3:
  print ("The figure is NOT a triangle")
if side_1 + side_2 > side_3:
  print ("The figure is a triangle")
if side_2 + side_1 < side_3:
  print ("The figure is NOT a triangle")
if side_2 + side_1 > side_3:
  print ("The figure is a triangle")
