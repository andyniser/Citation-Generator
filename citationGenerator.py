import sys

# MLA Citation Generator
mla_citation = ""   

# step 1: check for accepted type
def check_source_type(source_type):
    if source_type.lower() == "book" or source_type.lower() == "website" or source_type.lower() == "journal" or source_type.lower() == "magazine" or source_type.lower() == "newspaper":
        print(source_type + " is an accepted type.")
    else:
        sys.exit("That is not an accepted format.\nPlease enter an accepted format and try again!")

# step 2: get author
def get_author(first_name, middle_initial, last_name):
    if len(middle_initial) != 1:
        return last_name + ", " + first_name + "."
    else:
        return last_name + ", " + first_name + " " + middle_initial + "."

# step 3: get title
def get_title(title, source_type):
    if source_type.lower() == "book":
        return title + " (ITALICIZE THIS TITLE)" + "."
    else: #citing all other types 
        return "\"" + title + ".\""

# step 4: get container
def get_container(container):
    pass


# main method
print("Welcome to Andy's MLA Citation Generator: your ad free generator!")
print("If you are citing a book, wesbite, journal, magazine, or newspaper, this is the place for you!")
print("What type of source are you citing?")
source_type = input()
(check_source_type(source_type))
print("Please enter information as requested...")

# inputting author's name
print("\nLet's start with the author:\n")
print("Enter the author's first name below:")
first = input()
print("\nEnter the author's middle initial (enter \"none\" if not applicable):")
middle = input()
print("\nEnter the author's last name:")
last = input()
formatted_author = get_author(first, middle, last)
print(formatted_author)

# inputting title
print("\nWhat is the title of your source?")
title = input()
formatted_title = get_title(title, source_type)
print(formatted_title)



SystemExit



