![Github](https://img.shields.io/badge/python-3.8-green.svg?style=flat-square&logo=python&colorB=blue)
# GeneratedTestData
Short useful program that generates usable test data formatted such as the following example.
```json

      	[
      	{
      		"client_first_name": "Sandy",
      		"client_last_name": "Cohen",
      		"service_description": "routine teeth cleaning",
      		"service_date": "2019-03-04",
      		"service_performed_by": "Sam Oakland",
      		"service_amount_paid": 110.40,
      		"service_amount_currency": "USD"
          }
          ]
```
##pre-commit
    
    *Linting with flake
        
        In order to enable the auto-formatting in the development process, you have to spend a few seconds setting up 
        the pre-commit the first time you clone the repo.
        
        Install pre-commit by running: pip install pre-commit (or simply run pip install -r requirements.txt).
        
        Run pre-commit install to install the git hook.
        
        Once you successfully install the pre-commit hook to this repo, the Flake8 linter/formatter will be 
        automatically triggered and run on this repo.

##Building and running
    
    *Virtual environment
    It is recommended to create a virtual environment to run the program
    
    Create a virtual environment for running the program:
    
    virtualenv test-env
    source test-env/bin/activate
    pip install -r requirements.txt
    
    *Running the program
    Start from the folder GeneratedTestData then run the program testDataGenerator.py

    cd GeneratedTestData
    python testDataGenerator.py

    notes: by default the program generates 5 entries.

    *options to generate more entries (max 1000 - arbritary limit) 
    python testDataGenerator.py 50
    
    *Running unit tests
    few tests have been created and some need fixes
    Start from the folder GeneratedTestData
    
    pytest ../Tests/test_testDataGenerator.py
    
##Improvements

1. Fix unit tests that are commented and create more tests for each function
2. Fix the option to run the program with the --file argument to override the file service description
3. Fix the entry service_provider to insert Dr when needed. One idea will be to update the file service description with :Dr. for each service provided by a Doctor.

    Example: flu shot:Dr., cleaning, root canal:Dr.
    Use this information to update service provider with the proper prefix to the name 
4. Add more logging