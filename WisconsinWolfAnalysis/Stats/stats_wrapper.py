"""
This module contains the wrapper function

Function
----------------------------------
wrapper: handles IO with user and calls requested functions from stats_module

Exceptions
-----------------------------
ValueError: raised if inputs do not meet specifications
"""
import warnings
from Stats.stats_analysis import (hypothesis_function_one,
                                  hypothesis_function_two,
                                  hypothesis_function_three)


warnings.simplefilter(action='ignore', category=FutureWarning)


def wrapper():
    """
    This function will provide instructions to the user and recieve their
    requests. It will then call the specified functions from stats_module

    Arguments
    -------------------------------
    None

    Return Values
    ----------------------------
    None

    Side Effects
    --------------------------
    Prints the outputs and results from the requested stats_module functions

    Exceptions
    ---------------------------
    ValueError raised if:
        The user provides a list containing elements other than '1', '2', and
        '3', or, if there are not 1-3 elements in the list
    """

    options_str = input("\n----------------Statistical Analysis-------------\n"
          "Hello! Would you like to statistically test the correlation between"
          " two variables (1), examine trends over time (2), and/or compare "
          "two proportions (3)? \nPlease enter a comma separated list of the "
          "desired options.\n")

    options_ls = options_str.split(",")

    # ------------------Check for illegal input-----------------
    # <1 or >3 options specified
    if (len(options_ls) < 1) or (len(options_ls) > 3):
        raise ValueError("Invalid Input: User must provide between 1 and 3 "
                         "options.")

    # Perform the requested tasks
    for option in options_ls:
        if option == '1':
            filepath = input("\n**You have selected Option 1: Testing"
                             " Correlation Between Two Variables**\nPlease "
                             "provide the relative file path to the CSV file "
                             "containing the data you wish to use. Do not "
                             "encase the file path in quotes or other symbols."
                             "\nNote, the CSV must contain 3 columns - the 1st"
                             " can be any form (e.g., a year or other sample "
                             "identifier), the 2nd is population 1 data, and "
                             "the 3rd is population 2 data.\n")

            # A good test file: ./pdf/wolf_and_deer_pop.csv
            hypothesis_function_one(filepath)

        elif option == '2':
            filepath = input("\n**You have selected Option 2: Time-series "
                             "Visualization of Data and Trends**\nPlease "
                             "provide the relative file path to a CSV "
                             "containing the data you wish to use. Do not "
                             "encase the file path in quotes or other symbols."
                             "\nNote, the CSV must contain at least 2 numeric "
                             "columns - the first should represent a date or "
                             "period, and the remaining columns should contain"
                             " population data.\n")

            # A good test file: ./pdf/wolf_and_deer_pop.csv
            hypothesis_function_two(filepath)

        elif option == '3':
            filepath = input("\n**You have selected Option 3: Comparing Two "
                             "Proportions**\nPlease provide the relative file "
                             "path to a CSV file containing the data you wish "
                             "to use. Do not encase the file path in quotes "
                             "or other symbols. \nNote, the CSV must contain "
                             "at least 3 columns - the first must be numeric "
                             "(e.g., a year), the second must "
                             "be the total number of observations, and the "
                             "third+ must be the number of observations with "
                             "a specific characteristic of interest.\n")

            # A good test file: ./pdf/proportion_of_wolves.csv
            hypothesis_function_three(filepath)

        else:
            raise ValueError("User has not entered a valid option.")


if __name__ == '__main__':
    wrapper()
