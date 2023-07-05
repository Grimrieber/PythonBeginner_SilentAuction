import os
from asciart import logo


bids = {}

bidding_finished = False

print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?")
    price = input("What is your bid?")
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == "no":
        find_highest_bidder(bids)
        bidding_finished == True
    elif should_continue == "yes":
        os.system('cls')



