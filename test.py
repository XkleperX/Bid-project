# # ! This is a bid project

name = input("Enter your name please: ")
bid = int(input("Enter your bid: $"))

is_there = input("Is there other biders who's want to bid :")
bid_ = {name: bid}
max = bid
while is_there == "yes":
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
