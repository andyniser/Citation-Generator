# MLA Citation Generator
mla_citation = ""

def get_author(first_name, middle_initial, last_name):
    if len(middle_initial) != 1:
        return last_name + ", " + first_name + "."
    else:
        return last_name + ", " + first_name + " " + middle_initial + "."

def get_title(title, type):
    this_title = title
    if type.lower() == "book":
        return this_title + " (ITALICIZE THIS TITLE)" + "."
    if type.lower() == "website" or type.lower() == "journal" or type.lower() == "magazine" or type.lower() == "newspaper":
        return "\"" + this_title + ".\""
    else:
        return "That is not an accepted format.\nPlease enter an accepted format and try again!"
        SystemExit



# main method
print("Welcome to Andy's MLA Citation Generator: your add free generator!")
print("Please enter information as requested...")

# inputting author's name
print("\nLet's start with the author:\n")
print("Enter the author's first name below:")
first = input()
print("\nEnter the author's middle initial (enter \"none\" if not applicable):")
middle = input()
print("\nEnter the author's last name:")
last = input()
author = get_author(first, middle, last)


