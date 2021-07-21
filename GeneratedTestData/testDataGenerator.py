"""
This small program is used to generate test data matching a given format.
The output of this program will be a list of dictionary items
"""
import pprint
import decimal
import random

from faker import Faker
fake = Faker()

# Global variable
# Path to the file that list all type of service description
FILEPATH_SERVICE_DESCRIPTION = "../config/service_description.txt"
# Maximum amount a provider can bill
MAX_AMOUNT_RANGE = 10000

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
    test_data_generated_items = []
    for i in range(0, item_max):
        test_data_generated_items.append(item_dictionary[i])

    return test_data_generated_items

def print_data(item_list):
    #use pretty print to generate requested formating
    pprint.pprint(item_list,sort_dicts=False)

def input_data(item_max):
    # generate list of service description
    service_description_list = filetolist(FILEPATH_SERVICE_DESCRIPTION)

    # generate list of currencies
    amount_currency_list = ['CAD', 'USD']

    # generate dictionary
    generated_data= {}
    for i in range(0, item_max):
        generated_data[i] = {}
        generated_data[i]["client_first_name"] = fake.first_name()
        generated_data[i]["client_last_name"] = fake.last_name()
        generated_data[i]["service_description"] = fake.words(1, service_description_list, True)[0]
        generated_data[i]["service_date"] = fake.date_of_birth().strftime("%Y-%m-%d")
        generated_data[i]["service_performed_by"] = "Dr. "+ fake.name()
        generated_data[i]["service_amount_paid"] = '{}'.format(decimal.Decimal(random.randrange(0, MAX_AMOUNT_RANGE))/100)
        generated_data[i]["service_amount_currency"] = fake.words(1, amount_currency_list, True)[0]
    return generated_data


def main():

    # Enter number of Entries
    #TODO make this an argument of the script
    number_of_entries = 5

    # Generate fake data
    generated_data = (input_data(number_of_entries))
    # format data and print it
    # print(format(generated_data, number_of_entries))
    print_data(format(generated_data, number_of_entries))

    # Test


if __name__ == "__main__":
    main()
