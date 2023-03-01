"""PROGRAM DOCSTRING GOES HERE"""

from scipy.stats import pearsonr, linregress
from pathlib import Path
import pandas as pd

def hypothesis_function_one():
    """ 
    This function will calculate the correlation between two variables
    or populations over time
    ---------------------------Arguments-------------------------------
    none
    --------------------------Return Values----------------------------
    corr_coeff: numeric
        Description goes here
    p_value: numeric
        Description goes here
    -----------------------------Side Effects--------------------------
    User query: Asks the user for a csv file containing 3 columns.
        The first column can be any format, but second two need to be
        numeric types
    ------------------------------Exceptions---------------------------
    TypeError raised if:
        The input file isn't a csv, doesn't have 3 columns,
        the final two columns aren't numeric type, or there are fewer
        than 2 rows in the data frame
    """
    #Ask_path sub-function handles and tests the user input
    '''def ask_path(question, allowed_extension):
        file = Path(input(question))
        if file.exists() and file.is_file and file.suffix in allowed_extension:
            return file
        else:
            raise TypeError("Please ensure file exists and ends in '.csv'")            
    prompt = ("Correlation test: Please enter the relative filepath for"
              " a csv with 3 data columns.\n"
              "The second and third columns should contain numeric "
              "information on the independent and dependent "
              "populations, respectively.\n"
              "The first column can be any value(s) you choose "
              "e.g., a year or geographic region corresponding "
              "to the samples\n"
              "Filepath: ")
    file = ask_path(prompt, [".csv"])'''
    
    file = "./pdf/test_files/wolf_and_deer_pop.csv"

    #Putting the file into pandas and testing
    df = pd.read_csv(file)
    if len(df.columns) != 3:
        raise TypeError("CSV file must have exactly 3 columns")
    '''if df.iloc[:,[1,2]].dtypes not in ['int','float', 'complex']:
        raise TypeError("Data in 2nd and 3rd column must be numeric")
    if len(df) < 2:
        raise TypeError("Data must have at least 2 samples (rows)")
    if df.isnull().values.any():
        raise ValueError("Data may not have any null values")'''

    x = df.iloc[:,1]
    y = df.iloc[:,2]

    print("The program will perform a simple linear regression"
          " with a two-sided alternate hypothesis"
          " and calculate the Pearson Correlation Coefficient.")
    
    #Linear regression
    linear_regression = linregress(x, y, alternative="two-sided")
    intercept = linear_regression[0]
    slope = linear_regression[1]
    r_value = linear_regression[2]
    slope_pvalue = linear_regression[3]
    if slope_pvalue >= 0.05:
        print("Using a 0.05 level of statistical significance we FAIL"
              " TO REJECT the null hypothesis that there is no linear "
              "relationship between the independent and dependent "
              "populations.\n"
              "WARNING: Linear regression model is not a good fit for"
              "this data")
    elif slope_pvalue < 0.05:
        print("Using a 0.05 level of statistical significance we"
              " REJECT the null hypothesis that there is no linear "
              "relationship between the independent and dependent "
              "populations.")

    #Correlation
    pearson_results = pearsonr(x,y)
    corr_coeff = round(pearson_results[0],4)
    p_value = pearson_results[1]
    if p_value >= 0.05:
        print("Using a 0.05 level of statistical significance we FAIL"
              " TO REJECT the null hypothesis that there is no "
              "correlation between the independent and dependent "
              "populations")
    elif p_value < 0.05:
        print("Using a 0.05 level of statistical significance we "
              "REJECT the null hypothesis that there is no "
              "correlation between the independent and dependent "
              "populations\n"
              "REMEMBER: Correlation *does not* imply causation")
    print(f"Correlation coefficient: {corr_coeff}")
    print(f"p-value: {p_value}")

    return corr_coeff, p_value


def hypothesis_function_two():
    """MODULE DOCSTRING GOES HERE"""
    return "Nothing written yet"


def hypothesis_function_three():
    """MODULE DOCSTRING GOES HERE"""
    return "Nothing written yet"

'''testing'''
hypothesis_function_one()