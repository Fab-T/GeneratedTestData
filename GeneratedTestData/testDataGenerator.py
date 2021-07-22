"""
This small program is used to generate test data matching a given format.
The output of this program will be a list of dictionary items

usage:
    ./testDataGenerator.py {--file} number_of_entries

Example for generating 50 fake data entries:
    ./testDataGenerator.py 50

Variables:
    FILEPATH_SERVICE_DESCRIPTION is the path to a file containing a list of all possible service description
    MAX_AMOUNT_RANGE is the maximum value that can be generated as amount paid.

Config:
    service_description.txt contains a list of all possible services a doctor can perform.
    It is located within config directory and can be updated
    The format is important, service description should be separated by comma
"""
import pprint
import decimal
import random
import sys

# Using Faker library that produces fake data
from faker import Faker
fake = Faker()

# Global variables
# Path to the file that list all type of service description
FILEPATH_SERVICE_DESCRIPTION = "../config/service_description.txt"
# Maximum amount a provider can bill
MAX_AMOUNT_RANGE = 10000

# Check the formatting for file FILEPATH_SERVICE_DESCRIPTION
# should not contain empty value

def check_file_service_description_format(list_service):
    error_msg = "the file used for service description is not formatted correctly."
    if '' in list_service:
        sys.exit(error_msg + " It contains empty value")

# Checking the value given for the number of entries to generate
# Should check the value is an integer and is not above t
def check_number_of_entries(entries_input):
    try:
        entries_number = int(entries_input)
        if entries_number > 1000:
            sys.exit("Enter a number of entries lower than 1000")
    except ValueError:
        sys.exit("The value you entered ({}) cannot be converted to an integer".format(entries_input))
    return entries_number

def filetolist(file_path):
    def fileread(file_read):
        #check is filename is a string then open file to read/put lines in a single string, then close filename.
        if isinstance(file_read,str):
            with open(file_read,'r') as f:
                file_string=f.read()
                f.close()
        return file_string
    # remove newline at the end of the file if exists
    service_description = fileread(file_path).rstrip()
    # define a list of words (separated by comma)
    service_description_separated_by_comma = service_description.split(",")
    # check if the file is formatted correctly
    check_file_service_description_format(service_description_separated_by_comma)

    return service_description_separated_by_comma

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

def print_usage():
    print("usage: ./testDataGenerator.py {--file} number_of_entries \n"
          "Example: ./testDataGenerator.py 50 \n"
          "Example: ./testDataGenerator.py --file config/service_description.txt 50 \n"
          )

def main():

# This basic command line argument parsing code is provided to
# define the number of entries which you must define.
# Default value is 5.
# Optional : file path for the list of service descriptions.

    if len(sys.argv) > 4 or len(sys.argv) == 3:
        print_usage()
        sys.exit(1)
    if len(sys.argv) == 4:
        option = sys.argv[1]
        number_of_entries_input = sys.argv[3]
        if option == '--file':
            print("This option is currently not implemented. Running using file /config/service_description.txt")
            # TODO: implement a feature to pass the file containing the service description as an argument.
        else:
            print('unknown option: ' + option)
            sys.exit(1)
    else:
        if len(sys.argv) == 2:
            number_of_entries_input = sys.argv[1]
        else:
            number_of_entries_input = 5

    number_of_entries = check_number_of_entries(number_of_entries_input)

    # Generate fake data
    generated_data = (input_data(number_of_entries))
    # format data and print it
    print_data(format(generated_data, number_of_entries))


if __name__ == "__main__":
    main()
