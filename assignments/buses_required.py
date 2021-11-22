#take input from user, no of people, buses, seats per bus
from math import ceil
people = int(input("People :"))
buses = int(input("Buses :"))
seats = int(input("Seats :"))

if people <= buses*seats:
    print("Buses Sufficient")
else:
    x = people - (buses*seats)
    y = x/seats
    y = ceil(y)
    print("More %s buses are required"%y)