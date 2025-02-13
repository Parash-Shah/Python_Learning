# Learned to use random with number, list, and how to limit numbers after decimals.
import random
rand_num= random.randint(1,10)
print(rand_num)
random_nummber= random.random()*10
print(random_nummber)
random_float= round(random.uniform(1,10),2)
print(random_float)
random_heads_or_tails= random.randint(0,2)
if random_heads_or_tails==0:
    print("Heads")
else:
    print("Tails")
#Learned to print items from list.
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[2])
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
states_of_america.append("London")
print(states_of_america[50])
states_of_america.extend(["london","My home"])
print(states_of_america)
#Learned to randomly choose item from list of items.
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
Random_name= print(friends[random.randint(0,4)])
#Learned to convert list of items in to number of items in the list and then use
# the numbers to add subtract and print those items from the list.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

num_states= (len(states_of_america))
print(states_of_america[num_states-1])
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruit_and_veg= [fruits,veg]
print(fruit_and_veg)