# # ! This is a bid project


import os
from art import logo


def get_higher_bid(bid_dict):
    max_bid = 0
    winner = ""
    for bidders in bid_dict:
        bid_price = bid_dict[bidders]

        if bid_price > max_bid:
            max_bid = bid_price
            winner = bidders

    print(f"the winner is {winner} with bid ${max_bid}")


print(logo)

bids = {}


while True:
    name = input("Enter your name please: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price

    more_bidders = input("Are there other bidders? (yes/no): ").lower()

    if more_bidders == "yes":
        os.system("cls")
        continue
    elif more_bidders == "no":
        break


get_higher_bid(bids)

