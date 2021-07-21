# unit tests for the module testDataGenerator

from GeneratedTestData import testDataGenerator

# test 5 entries generates 5 items
#TODEL input_data = target.input_data

def test_generateFiveEntries():
    five_entries = (testDataGenerator.input_data(5))
    assert len(five_entries) == 5

# test 1 entry generates client first name, client last name

def test_generateformat():
    one_entry = (testDataGenerator.format(testDataGenerator.input_data(1), 1))
    # Using iter to parse dictionary keys with next
    iter_one_entry = (iter(one_entry[0]))
    assert print(next(iter_one_entry)) == "client_first_name"
    assert print(next(iter_one_entry)) == "client_first_name"
    assert print(next(iter_one_entry)) == "service_description"
    assert print(next(iter_one_entry)) == "service_date"
    assert print(next(iter_one_entry)) == "service_performed_by"
    assert print(next(iter_one_entry)) == "service_amount_paid"
    assert print(next(iter_one_entry)) == "service_amount_currency"

