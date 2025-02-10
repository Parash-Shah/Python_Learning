#learned to use if elif and else
#learned to use different comparator operators.
#Implemented previously learned concepts.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age>=45 or age<=55:
        bill=0
        print("You get a free ride.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
# second practice
# made pizza delivery questionnaire using if else and elif.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size=="S":
    bill= 15
    if pepperoni=="Y":
        bill+=2
        if extra_cheese=="Y":
            bill+=1
        else:
            bill+=0
    else:
        bill+=0
elif size=="M":
    bill= 20
    if pepperoni=="Y":
        bill+=3
        if extra_cheese=="Y":
            bill+=1
        else:
            bill+=0
    else:
        bill+=0
elif size== "L":
    bill= 25
    if pepperoni=="Y":
        bill+=3
        if extra_cheese=="Y":
            bill+=1
        else:
            bill+=0
    else:
        bill+=0

else:
    print("Invalid entry.")
print(f"Your final bill is: ${bill}")

