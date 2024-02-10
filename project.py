# # ! This is a bid project


import os
from art import logo


def get_higher_bid(bid_dict):
    max_bid = 0

    for bidders in bid_dict:
        bid_price = bid_dict[bidders]

        if bid_price > max_bid:
            max_bid = bid_price
            winner = bidders

    print(f"the winner is {winner} with bid ${max_bid}")


print(logo)

bid = {}

name = input("Enter your name please: ")
price = int(input("Enter your bid: $"))

bid[name] = price

is_there = input("Is there other biders who's want to bid :")

while is_there == "yes":
    os.system("cls")
    name = input("Enter your name please: ")
    price = int(input("Enter your bid: $"))
    is_there = input("Is there other biders who's want to bid: ")
    bid[name] = price

if is_there == "no":
    get_higher_bid(bid)

else:
    print("Please enter your 'yes or no' ")
