import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    higgest_bid = 0
    for bidder in bidding_dictionary:
        price = bidding_dictionary[bidder]
        if price> higgest_bid:
            higgest_bid = price
            winner = bidder
    print(f"Our winner is {winner} with Bid of ${higgest_bid}.")

Bidding_info = {}
#print(Bidding_info)



Continue_bidding =True
while Continue_bidding:
    User_name = input("What is your name?\n")
    Bid_amount = int(input("How much would you like to bid?\n $"))
    Bidding_info[User_name] = Bid_amount
    next_bidder = input("is there someone else bidding after you? 'yes' or 'no'\n").lower()
    if next_bidder == "no":
        Continue_bidding = False
        find_highest_bidder(Bidding_info)
    elif next_bidder == "yes":
        print("\n"*20)
