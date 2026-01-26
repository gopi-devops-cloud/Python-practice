programming_dictionary ={
    "Function":"recipe of steps.",
    "Loop " : "repeat until condition changes.",
    "Bug":" mistake causing wrong behavior.",
    123:"without ("") this" 
}

print(programming_dictionary["Function"])
# without "" in number
print(programming_dictionary[123])
# adding new item in dictionary
programming_dictionary["item"]="new item"
print(programming_dictionary)
# empty dictionaries
empty_dictionary={}
# #wipe an existing dictionary
programming_dictionary={}
print(programming_dictionary)
# edit an item in dictionary?
programming_dictionary[123]="edited dictionary"
print(programming_dictionary)
# loop through dictionary
# wrong method
# for thing in programming_dictionary:
#     print(thing)
# right method
for key in programming_dictionary:
    print(key)
# but if want def also of key
    print(programming_dictionary[key])
capitals ={
    "france":"paris",
    "germany":"berlin"
}

#nested list in dictioanary(list inside list)
travel_vlog={
    "france":["paris","lille","dijon"],
    "germany":["stuttgart","berlin"],

    }
# print lille
print(travel_vlog["france"][1])

nested_list=["A","B",["C","D"]]
print(nested_list[2][1])
# dictionary under dictionary
travel_vlog={
   "france":{
    "cities_visited":["paris","lille","dijon"],
    "total_visites": 12
    },
   "germany":{
    "cities_visited": ["stuttgart","hamburg","berlin"],
    "total_visites": 5
    }
}
print(travel_vlog["germany"]["cities_visited"][0])

# day 9 project
print("welcome to the secret auction program.")
def find_highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0

    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids={}
continue_bidding=True
while continue_bidding:
    name=input("what is your name?: ")
    price=int(input("what is your bid?: $"))
    bids[name]=price
    should_continue = input("Are there any other bidders? type 'yes' or 'no'.\n").lower()
    if should_continue=="no":
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue=="yes":
        print("\n"*20)