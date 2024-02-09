# # ! This is a bid project
import os
from art import logo

print(logo)

name = input("Enter your name please: ")
bid = int(input("Enter your bid: $"))

bid_ = {name: bid}
max = bid

is_there = input("Is there other biders who's want to bid :")

while is_there == "yes":

    # Clearing the Screen
    os.system("cls")

    name = input("Enter your name please: ")
    bid = int(input("Enter your bid: $"))
    bid_ = {name: bid}

    if bid > max:
        max = bid
    else:
        continue

    is_there = input("Is there other biders who's want to bid: ")

if is_there == "no":
    for bider in bid_:
        print(f"the winner is {bider} with bid ${bid}")

else:
    print("please enter your 'yes or no' ")
