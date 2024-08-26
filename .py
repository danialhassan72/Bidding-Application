import os
from art import logo, yo
#clears the console

def clear():
 os.system('cls' if os.name == 'nt' else 'clear')
print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("enter your name: ")
    bid = float(input("enter your bid : $"))
    bids[name] =bid

    should_continue = input("are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == 'yes':
        clear()
highest_bidder = ""
highest_bid = 0

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder

clear()
print(f"The highest bidder is {highest_bidder} with the bid of a ${highest_bid:.2f}")
print(yo)
