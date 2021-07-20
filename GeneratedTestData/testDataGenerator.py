#!/usr/bin/env python

"""
This small program is used to generate test data matching a given format.
The output of this program will be a list of dictionary items
"""
import pprint
from faker import Faker
fake = Faker()
# Global variable
TEST_DATA_GENERATED_ITEMS = []

def format(dictionary,itemMax):
    # remove index and create list
    for i in range(0, itemMax):
        TEST_DATA_GENERATED_ITEMS.append(dictionary[i])
    #print(TEST_DATA_GENERATED_ITEMS)
    pprint.pprint(TEST_DATA_GENERATED_ITEMS,width=1)

def input_data(itemMax):
    # dictionnary
    generated_data= {}
    for i in range(0, itemMax):
        generated_data[i]= {}
        generated_data[i]["client_first_name"]= fake.first_name()
        generated_data[i]["client_last_name"]= fake.last_name()
    return generated_data

def main():

    # Enter number of Entries
    number_of_entries = 5
    generated_data = (input_data(number_of_entries))
    # print(generated_data)
    format(generated_data,number_of_entries)

if __name__ == "__main__":
    main()
