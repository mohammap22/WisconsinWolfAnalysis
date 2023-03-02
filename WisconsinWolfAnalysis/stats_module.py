"""PROGRAM DOCSTRING GOES HERE"""

from scipy.stats import pearsonr, linregress
from pathlib import Path
import pandas as pd
from pandas.api.types import is_numeric_dtype


def hypothesis_function_one(filepath):
    """ 
    This function will calculate the correlation between two variables
    or populations over time
    ---------------------------Arguments-------------------------------
    none
    --------------------------Return Values----------------------------
    corr_coeff: numeric
        Pearson R correlation coefficient calculated via Scipy
    p_value: numeric
        p-value of the Pearson R correlation
    -----------------------------Side Effects--------------------------
    User query: Asks the user for a csv file containing 3 columns.
        The first column can be any format, but second two need to be
        numeric types
    ------------------------------Exceptions---------------------------
    TypeError raised if:
        The input file isn't a csv, doesn't have 3 columns,
        the final two columns aren't numeric type, there are fewer
        than 2 rows in the data frame, there are null values
    """

    #Putting the file into pandas and testing
    if filepath[-4:] != '.csv':
        raise TypeError('File must be a csv')
    df = pd.read_csv(filepath)
    if len(df.columns) != 3:
        raise TypeError("CSV file must have exactly 3 columns")
    if (not is_numeric_dtype(df.iloc[:,1]) or  
        not is_numeric_dtype(df.iloc[:,2])):
        raise TypeError("Data in 2nd and 3rd column must be numeric")
    if len(df) < 2:
        raise TypeError("Data must have at least 2 samples (rows)")
    if df.isnull().values.any():
        raise ValueError("Data may not have any null values")

    x = df.iloc[:,1]
    y = df.iloc[:,2]

    print("\nCORRELATION HYPOTHESIS TEST (1):\n"
          "\nThe program will perform a simple linear regression and "
          "calculate \nthe Pearson Correlation Coefficient for the "
          "independent and dependent populations.\n"
          "All tests use 0.05 level of significance and two-sided"
           " hypothesis tests.\n\n"
           "-------------------------RESULTS-------------------------"
           "\n")
    
    #Linear regression
    linear_regression = linregress(x, y, alternative="two-sided")
    intercept = linear_regression[0]
    slope = linear_regression[1]
    r_value = linear_regression[2]
    slope_pvalue = linear_regression[3]
    if slope_pvalue >= 0.05:
        print("FAIL TO REJECT null hypothesis of no linear relationship\n"
              "WARNING: Linear regression model is not a good fit for"
              "this data\n")
    elif slope_pvalue < 0.05:
        print("REJECT null hypothesis of no linear relationship\n")

    #Correlation
    pearson_results = pearsonr(x,y)
    corr_coeff = round(pearson_results[0],4)
    p_value = pearson_results[1]
    if p_value >= 0.05:
        print("FAIL TO REJECT null hypothesis of no correlation")
    elif p_value < 0.05:
        print("REJECT null hypothesis of no correlation")
    print(f"Correlation coefficient: {corr_coeff}")
    print(f"p-value: {p_value}\n")
    print("---------------------------------------------------------"
           "\n")
    return corr_coeff, p_value


def hypothesis_function_two():
    """MODULE DOCSTRING GOES HERE"""
    return "Nothing written yet"


def hypothesis_function_three():
    """MODULE DOCSTRING GOES HERE"""
    return "Nothing written yet"

'''testing'''
#hypothesis_function_one("./pdf/test_files/wolf_and_deer_pop.csv")