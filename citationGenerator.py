import sys

# formatted citation variables
source_type = ""
components = {} 

#-----------------------------------------------

# methods to correctly format information
# step 1: check for accepted type
def check_source_type(source_type):
    if source_type.lower() == "book" or source_type.lower() == "website" or source_type.lower() == "journal" or source_type.lower() == "magazine" or source_type.lower() == "newspaper":
        print("\n" + source_type.title() + " is an accepted type.")
    else:
        sys.exit("That is not an accepted format.\nPlease enter an accepted format and try again!")

# step 2: get author
def get_author(first_name, middle_initial, last_name):
    if len(middle_initial) != 1:
        components["author"] = last_name + ", " + first_name + "."
    else:
        components["author"] = last_name + ", " + first_name + " " + middle_initial + "."

# step 3: get title
def get_title(title, source_type):
    if source_type.lower() == "book":
        components["title"] = title + "."
        return title
    else: #citing all other types 
        components["title"] = "\"" + title + ".\""

# step 4: get container
def get_container(container):
    if container == "none":
        components["container"] = None
    else:
        components["container"] = container + ","

# step 5: get version
def get_version(version):
    if version == "none":
        components["version"] = None
    else:
        components["version"] = version + ","

# step 6: get publisher
def get_publisher(publisher):
    if publisher == "none":
        components["publisher"] = None
    else:
        components["publisher"] = publisher + ","
    

# step 7: get publication date
def get_publication_date(publication_date):
    if publication_date == "none":
        components["publication_date"] = None
    else:
        components["publication_date"] = publication_date + ","


# step 8: location (website or page number(s))
def get_location(location):
    if source_type == "website":
        components["location"] = location + "."
    if location == "none":
        components["location"] = None
    else:
        components["location"] = "pp. " + location + "."


# step 9: compile and print mla citation
def get_mla_citation():
    mla_citation = ""
    for component in components.values():
        if component != None:
            mla_citation += component + " "
    if mla_citation[-1] != ".":
        period_mla_citation = mla_citation[0:-2] + "."
        return period_mla_citation
    return mla_citation

#-----------------------------------------------

# script
print("Welcome to Andy's MLA Citation Generator: your ad free generator!")
print("If you are citing a book, wesbite, journal, magazine, or newspaper, this is the place for you!")
print("What type of source are you citing?")
source_type = input()
check_source_type(source_type)

print("Please enter information as requested...")

# inputting author's name
print("\nLet's start with the author:\n")
print("Enter the author's first name below:")
first = input()
print("\nEnter the author's middle initial (press \"enter\" if not applicable):")
middle = input()
print("\nEnter the author's last name:")
last = input()
get_author(first, middle, last)

# inputting title
print("\nWhat is the title?")
formatted_title = get_title(input(), source_type)

# inputting container
print("\nA container is the collection from which you found your source.")
print("Examples include online databases like JSTOR or services like Netflix.")
print("What is the name/title of the container of your source?\nEnter \"none\" if N/A")
container = input()
get_container(container)

# inputting edition
print("\nIf this source is listed as an version of a work (ex. 3rd ed. or Modern Version)")
print("please enter it below. Enter \"none\" if N/A")
get_version(input())

# inputting publisher
print("\nWho is the publisher? Enter \"none\" if N/A or not known.")
get_publisher(input())

# inputting publication date
print("\nWhat is the publication date?")
get_publication_date(input())

# inputting location
print("\nWhere is this source found?")
if source_type == "website":
    print("Enter the website's URL or enter \"none\" if N/A.:")
else:
    print("Enter the page number(s) or enter \"none\" if N/A.:")
get_location(input())

# output mla citiation to terminal and print italicized list
print("\nYour citation is: \n" + get_mla_citation())

# List of what needs to be italicized:
# 1) title of book
# 2) container
if source_type == "book" or container != "none":
    print("\nThe following item(s) must be italicized:")
    if source_type == "book":
        print(formatted_title)
    if container != "none":
        print(container)


# future additions
# 1) add a dictionary to store generated citation
# 2) sort the dictionary in alphabetical order by formatted_author
# 3) print a formatted works cited page to copy/paste into document with indentations
