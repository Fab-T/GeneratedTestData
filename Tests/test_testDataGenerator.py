# unit tests for the module testDataGenerator
import pytest
from GeneratedTestData import testDataGenerator

# test 5 entries generates 5 items
#TODEL input_data = target.input_data

def test_generateFiveEntries():
    five_entries = (testDataGenerator.input_data(5))
    assert len(five_entries) == 5

# test 1 entry generates the requested key elements from the template

def test_generateformateddata():
    one_entry = (testDataGenerator.format(testDataGenerator.input_data(1), 1))
    keys_view = one_entry[0].keys()
    keys_iterator = iter(keys_view)
    assert next(keys_iterator) == "client_first_name"
    assert next(keys_iterator) == "client_last_name"
    assert next(keys_iterator) == "service_description"
    assert next(keys_iterator) == "service_date"
    assert next(keys_iterator) == "service_performed_by"
    assert next(keys_iterator) == "service_amount_paid"
    assert next(keys_iterator) == "service_amount_currency"

# test check number of entries use cases
# TODO: fix these tests
# def test_check_number_above_1000():
#    with pytest.raises(SystemExit) as exc:
#        testDataGenerator.check_number_of_entries(1001)
#    assert exc.value == "Enter a number of entries lower than 1000"

# def test_check_number_str():
#    with pytest.raises(SystemExit) as exc:
#        testDataGenerator.check_number_of_entries('str')
#        assert exc.value == "The value you entered (str) cannot be converted to an integer"

# test check file service description format
# def test_service_description_empty_value():
#    fake_list_service_description = ["flu shot", "", "root canal"]
#    with pytest.raises(SystemExit) as exc:
#        testDataGenerator.check_file_service_description_format(fake_list_service_description)
#        assert exc.value == "the file used for service description is not formatted correctly. It contains empty value"
