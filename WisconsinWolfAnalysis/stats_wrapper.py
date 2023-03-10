"""Docstring Goes Here"""

<<<<<<< HEAD
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
=======
>>>>>>> main
from stats_module import (hypothesis_function_one,
                          hypothesis_function_two,
                          hypothesis_function_three)


def wrapper():
    """TBD Goes Here"""
    options_str = input("\n----------------Statistical Analysis--------------\n"
          "Hello! Would you like to statistically test the correlation between "
          "two variables (1) examine trends over time (2), and/or compare "
          "two proportions (3)? \nPlease enter a comma-separated list of the "
          "desired options.\n")

    options_ls = options_str.split(",")

    #------------------Check for illegal input-----------------
    #<1 or >3 options specified
    if (len(options_ls) < 1) or (len(options_ls) > 3):
        raise ValueError("Invalid Input: User must provide between 1 and 3 "
                         "options.")

    #Perform the requested tasks
    for option in options_ls:
        if option == '1':
            filepath = input("\n**You have selected Option 1: Testing Correlation"
                             "Between Two Variables**\nPlease provide the file "
                             "path to the CSV file containing the data you "
                             "wish to use. \nNote, the CSV must contain 3 "
                             "columns - the 1st is date/time, the 2nd is "
                             "population 1 data, and the 3rd is population 2 "
                             "data.\n")

            #A good test file: ./pdf/wolf_and_deer_pop.csv
            hypothesis_function_one(filepath)

        elif option == '2':
            filepath = input("\n**You have selected Option 2: Time-series "
                             "Visualization of Data and Trends**\nPlease "
                             "provide the file path to a CSV file containing "
                             "the data you wish to use.\nNote, the CSV must "
                             "contain at least 2 columns - the first must be a "
                             " datetime, and the second+ is/are a variable.\n")

            #A good test file: ./pdf/wolf_and_deer_pop.csv
            hypothesis_function_two(filepath)

        elif option == '3':
            filepath = input("\n**You have selected Option 3: Comparing Two "
                             "Proportions**\nPlease provide the file path to a "
                             "CSV file containing the data you wish to use.\n"
                             "Note, the CSV must contain at least 3 columns - "
                             "the first must be a datetime, the second must "
                             "be the total\nnumber of observations, and the "
                             "third+ must be the number of observations with a "
                             "specific characteristic of interest.\n")

            #A good test file: ./pdf/proportion_of_wolves.csv
            hypothesis_function_three(filepath)

        else:
            raise ValueError("User has not entered a valid option.")

if __name__ == '__main__':
    wrapper()
