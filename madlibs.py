"""
This program generates passages that are generated in mad-lib format
Author: Hong Wei
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year%s, in a world where %s ruled the world."
print("Mad Libs has started!")
name = input("Enter a name: ")
adj1 = input("Enter the first adjective: ")
adj2 = input("Enter the second adjective: ")
adj3 = input("Enter the third adjective: ")
verb = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")
print STORY %(name, adj1, adj2, adj3, verb, noun1, noun2, animal, food, fruit, superhero, country, dessert, year)
