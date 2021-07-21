"""
This small program is used to generate test data matching a given format.
The output of this program will be a list of dictionary items
"""
import pprint
import os
from faker import Faker
fake = Faker()

# Global variable
filepath_service_description = "config/service_description.txt"

def filetolist(file_path):
    def fileread(file_read):
        #check is filename is a string then open file to read/put lines in a single string, then close filename.
        if isinstance(file_read,str):
            with open(file_read,'r') as f:
                file_string=f.read()
                f.close()
        return file_string
    # define a list of words (separated by comma)
    list_words_separated_by_comma = fileread(file_path).split(",")
    return list_words_separated_by_comma

def format(item_dictionary,item_max):
    # remove index and create list
    TEST_DATA_GENERATED_ITEMS = []
    for i in range(0, item_max):
        TEST_DATA_GENERATED_ITEMS.append(item_dictionary[i])

    return TEST_DATA_GENERATED_ITEMS

def print_data(item_list):
    #use pretty print to generate requested formating
    pprint.pprint(item_list)

def input_data(item_max):
    # generate list of service description
    service_description_list = filetolist(filepath_service_description)


    # dictionnary
    generated_data= {}
    for i in range(0, item_max):
        generated_data[i] = {}
        generated_data[i]["client_first_name"] = fake.first_name()
        generated_data[i]["client_last_name"] = fake.last_name()
        generated_data[i]["service_description"] = fake.words(1,service_description_list,True)[0]
    return generated_data


def main():

    # Enter number of Entries
    #TODO make this an argument of the script
    number_of_entries = 5

    # Generate fake data
    generated_data = (input_data(number_of_entries))
    # format data and print it
    print_data(format(generated_data, number_of_entries))

    # Test
    # service_description_list = filetolist(filepath_service_description)
    # print(format(generated_data, number_of_entries))


if __name__ == "__main__":
    main()
