programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}


programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)
# wipe existing dictionary.
#programming_dictionary = {}
#print(programming_dictionary)

# erase previous definition of key.
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# lesson 2
Capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

travel_log = {
    "France" : ["Paris" , "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
}
# Nested list in the dictionary
# print out "lille" from the travel log
print(travel_log["France"][1])

# from the nested list below print out "D".
nested_list = ["A" , "B" , ["C" , "D"]]
print(nested_list[2][1])

# dictionary in side another dictionary
# print "Stuttgart" from the dictionary.

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])