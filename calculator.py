# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 01:44:07 2018

@author: Aakriti Adhikari
"""

#python_calculator_simple
def add(x, y): 
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice = input("enter choice(1/2/3/4):")
first_num = int(input("enter first number:"))
second_num = int(input("enter second number:"))
if choice == '1':
    print(first_num,"+",second_num,"=",add(first_num,second_num))
elif choice == '2':
    print(first_num,"-",second_num,"=",subtract(first_num,second_num))
elif choice == '3':
    print(first_num,"*",second_num,"=",multiply(first_num,second_num))
elif choice == '4':
    print(first_num,"/",second_num,"=",divide(first_num,second_num))
else:
    print("invalid syntax")
    
    
