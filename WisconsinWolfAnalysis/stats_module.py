"""PROGRAM DOCSTRING GOES HERE"""

from scipy.stats import pearsonr, linregress
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
import seaborn as sns
import matplotlib.pyplot as plt


def hypothesis_function_one(filepath):
    """ 
    This function will calculate the correlation between two
    populations over time
    ---------------------------Arguments-------------------------------
    filepath: string
        Filepath to csv file for correlation analysis
    --------------------------Return Values----------------------------
    corr_coeff: numeric
        Pearson R correlation coefficient calculated via Scipy
    p_value: numeric
        p-value of the Pearson R correlation
    -----------------------------Side Effects--------------------------
    None
    ------------------------------Exceptions---------------------------
    TypeError raised if:
        The input file isn't a csv, doesn't have 3 columns,
        the final two columns aren't numeric type, there are fewer
        than 2 rows in the data frame, there are null values
    """

    #Putting the file into pandas and testing
    if filepath[-4:] != '.csv':
        raise TypeError('File must be a csv')
    correlation_df = pd.read_csv(filepath)
    if len(correlation_df.columns) != 3:
        raise TypeError("CSV file must have exactly 3 columns")
    if (not is_numeric_dtype(correlation_df.iloc[:,1]) or
        not is_numeric_dtype(correlation_df.iloc[:,2])):
        raise TypeError("Data in 2nd and 3rd column must be numeric")
    if len(correlation_df) < 2:
        raise TypeError("Data must have at least 2 samples (rows)")
    if correlation_df.isnull().values.any():
        raise ValueError("Data may not have any null values")

    x_var = correlation_df.iloc[:,1]
    y_var = correlation_df.iloc[:,2]

    print("\nCORRELATION HYPOTHESIS TEST (1):\n"
          "\nThe program will perform a simple linear regression and "
          "calculate \nthe Pearson Correlation Coefficient for the "
          "independent and dependent populations.\n"
          "All tests use 0.05 level of significance and two-sided"
           " hypothesis tests.\n\n"
           "-------------------------RESULTS-------------------------"
           "\n")

    #Linear regression
    linear_regression = linregress(x_var, y_var, alternative="two-sided")
    intercept = linear_regression[0]
    slope = linear_regression[1]
    slope_pvalue = linear_regression[3]
    if slope_pvalue >= 0.05:
        print("FAIL TO REJECT null hypothesis of no linear relationship\n"
              "WARNING: Linear regression model is not a good fit for"
              "this data\n")
    elif slope_pvalue < 0.05:
        print("REJECT null hypothesis of no linear relationship\n")

    #Correlation
    pearson_results = pearsonr(x_var,y_var)
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

def hypothesis_function_two(filepath):
    """ 
    This function will produce a graph with populations over time
    ---------------------------Arguments-------------------------------
    filepath: string
        Filepath to csv file for correlation analysis
    --------------------------Return Values----------------------------
    None
    -----------------------------Side Effects--------------------------
    Prints a graph of the second+ columns vs. the first column to the
        screen
    ------------------------------Exceptions---------------------------
    TypeError raised if:
        The input file isn't a csv, dataframe doesn't have >2 columns,
        the columns aren't all numeric, there are null values
    """
    #Putting the file into pandas and testing
    if filepath[-4:] != '.csv':
        raise TypeError('File must be a csv')
    graph_df = pd.read_csv(filepath)
    if len(graph_df.columns) < 2:
        raise TypeError("CSV file must have at least 2 columns")
    for i in range(len(graph_df.columns)):
        if not is_numeric_dtype(graph_df.iloc[:,i]):
            raise TypeError("Data must be numeric")
    if graph_df.isnull().values.any():
        raise ValueError("Data may not have any null values")
    
    #Creating the graphs using Seaborn
    x_var = graph_df.columns[0]
    graph_df_melted = graph_df.melt(x_var, var_name="Populations",
                                    value_name="Counts")
    sns.lineplot(data = graph_df_melted, x = x_var, y = "Counts",
                 hue = "Populations")
    plt.show()


def hypothesis_function_three(filepath):
    """MODULE DOCSTRING GOES HERE"""
    
    #Save the provided CSV as a pandas DataFrame
    if filepath[-4: ] != ".csv":
        raise TypeError("Error: the provided file must be a CSV.")
    df = pd.read_csv(filepath)
    
    #Ensure the DataFrame is valid
    if not len(df.axes[0]) >= 2:
        raise ValueError("Error: the provided CSV must have at least 2 rows.")
    
    if not len(df.axes[1]) >= 3:
        raise ValueError("Error: the provided CSV must have at least 3 columns.")
    
    if df.isnull().values.any():
        raise ValueError("Error: the provided CSV must have no NaN values.")
    
    print("\nPROPORTION HYPOTHESIS TEST (3):\n"
          "\nThe program will perform a 2-sample Z test for proportions at the "
          "0.05 significance level for each provided variable.\n"
           "-------------------------RESULTS-------------------------"
           "\n")
    
    #Conduct Tests
    #import scipy.stats.distributions as dist
    #pvalue = 2*dist.norm.cdf(-np.abs(test_stat))
    
    #Grab years
    time1 = df[df.columns[0]][0]
    time2 = df[df.columns[0]][len(df.axes[0]) - 1]
    
    #Get populations for years of interest
    total_obs1 = df[df.columns[1]][0]
    total_obs2 = df[df.columns[1]][len(df.axes[0]) - 1]
    total_obs_ls = [total_obs1, total_obs2]
    
    #drop first 2 columns
    df_dropped = df.drop(columns=df.columns[0:2], axis=1, inplace=False)
    
    #Get counts for rows of interest (first and last) //sucesses
    # char_counts1 = df_dropped.iloc[0].tolist()
    # char_counts2 = df_dropped.iloc[len(df.axes[0] - 1)].tolist()
    
    #Make lists of total observation counts
    # total_obs1_ls = [total_obs1] * len(char_counts1)
    # total_obs2_ls = [total_obs2] * len(char_counts2)
    
    #for each column in dropped df
    for (col_name, col_data) in df_dropped.iteritems():
        
        #get counts
        successes_yr1 = col_data[0]
        successes_yr2 = col_data[len(df.axes[0]) - 1]
        successes_ls = [successes_yr1, successes_yr2]
        
        #perform test
        test_stat, pval = proportions_ztest(successes_ls, total_obs_ls)
        
        print("****\n")
        print("VARIABLE: " + col_name + "\nNULL HYPOTHESIS: proportion in "
              "" + str(time1) + " = proportion in " + str(time2) + ".\n")
        
        prop1 = successes_ls[0] / total_obs_ls[0]
        prop2 = successes_ls[1] / total_obs_ls[1]
        
        #Reject null hypothesis
        if pval <= 0.05:
                        print("Result: reject null hypothesis that \nproportion 1 of " 
                  "" + str(prop1) + " = proportion 2 of " + str(prop2) + ".\n"
                  "Test Statistic: " + str(test_stat) + "\np-value: "
                  "" + str(pval) + "\n")
        
        #Fail to reject null hypothesis
        else:
            print("Result: fail to reject null hypothesis that\nproportion 1 of" 
                  " " + str(prop1) + " = proportion 2 of " + str(prop2) + ".\n"
                  "Test Statistic: " + str(test_stat) + "\np-value: "
                  "" + str(pval) + "\n")
        
    
    print("------------------------------------------------------------------")

#hypothesis_function_one('./pdf/test_files/wolf_and_deer_pop.csv')