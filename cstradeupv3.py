__author__ = '//dat//pebble'

import random
import sys
import os
import tokenize
import json

'''This is designed to calculate the end float value of a item from a csgo tradeup,
it is most likely broken ;)'''

# declares operations


def divide(x, y):
    return x / y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def plus(x, y):
    return x + y

# creates a list of the float values


FloatList = []
MaxLength = 10
while len(FloatList) < MaxLength:
    Floats = float(input("Enter A Float of an item that you are using in the tradeup "))
    FloatList.append(Floats)


# adds all the members of the list together


FloatWorking1 = sum(FloatList)


# Finds the minimum and maximum float of the users wanted skin


MinFloat = float(input("Enter the minimum float of an item that you could recieve: "))

MaxFloat = float(input("Enter the maximum float of an item that you could recieve: "))


# Uses the Trilluxe process to calculate the final wear level

AverageFloat = divide(FloatWorking1, len(FloatList))

working1 = subtract(MaxFloat, MinFloat)

working2 = multiply(working1, AverageFloat)

working3 = plus(working2, MinFloat)


# Works out which wear level to print


if working3 >= 0.45:
    print("You will receive a Battle Scared Skin")

if working3 >= 0.37:
    if working3 < 0.45:
        print("You will receive a Well Worn Skin")

if working3 >= 0.15:
    if working3 < 0.37:
        print("You will receive a Field Tested Skin")

if working3 >= 0.07:
    if working3 < 0.15:
       print("You will receive a Minimal Wear Skin")

if working3 >= 0.00:
    if working3 < 0.07:
       print("You will receive a Factory New Skin with a float Value of " + working3)


''' Changes the values of the skin to be recieved's minimum and maximum wear levels
based on if the user wants to calculate teh wear level they would recieve of another s
kin that they could get from the tradeup'''

print("Do you want to calculate the float of another skin that you could recieve? Type Yes or No")

input(str("Yes"))
while True:
    MinFloat = float(input("What is the Minimum Float Value of the New Item? "))
    MaxFloat = float(input("What is the Maximum Float Value of the New Item? "))

    AverageFloat = divide(FloatWorking1, 10)

    working1 = subtract(MaxFloat, MinFloat)

    working2 = multiply(working1, AverageFloat)

    working3 = plus(working2, MinFloat)

    if working3 >= 0.45:
        print("You will receive a Battle Scared Skin")

    if working3 >= 0.37 and working3 < 0.45:
        print("You will receive a Well Worn Skin")

    if working3 >= 0.15 and working3 < 0.37:
        print("You will receive a Field Tested Skin")

    if working3 >= 0.07 and working3 < 0.15:
        print("You will receive a Minimal Wear Skin")

    if working3 >= 0.00 and working3 < 0.07:
        print(("You will receive a Factory New Skin with a float Value of " + working3))

    print("Do you want to calculate the float of another skin that you will recieve? Type Yes or No")



