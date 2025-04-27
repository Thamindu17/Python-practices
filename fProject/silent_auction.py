import os
def findwinner(bidderdetail):
    highest_bid=0
    winner=""
    for i in bidderdetail:
        bidding_price=bidderdetail[i]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=i
    print(bidderdetail)
    print(f"winner is {winner} bid price is {highest_bid}")
bidder_data = {}
end_of_bid = False
while not end_of_bid:

    name = input("enter name:")
    price = int(input("enter your bid"))
    bidder_data[name] = price
    more_bidders = input("continue type 'yes' for exit type 'no'").lower()
    if more_bidders == 'no':
        end_of_bid = True
        findwinner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')

