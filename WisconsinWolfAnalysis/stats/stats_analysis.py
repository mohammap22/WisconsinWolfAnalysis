"""
This module contains hypothesis functions one, two and three

Function
----------------------------------
hypothesis_function_one: calc correlation between 2 vars and graphs it
hypothesis_function_two: graphs populations over time
hypothesis_function_three: compares two %s and graphs vars over time

Exceptions
-----------------------------
TypeError: raised if inputs do not meet specifications
ValueError: raised if inputs do not meet specifications
"""

from scipy.stats import pearsonr, linregress
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
from pandas.api.types import is_numeric_dtype
import seaborn as sns
import matplotlib.pyplot as plt


def hypothesis_function_one(filepath):
    """
    This function will calculate the correlation between two
    populations over time

    Arguments
    -------------------------------
    filepath: string
        Filepath to csv file for correlation analysis

    Return Values
    ----------------------------
    corr_coeff: numeric
        Pearson R correlation coefficient calculated via Scipy
    p_value: numeric
        p-value of the Pearson R correlation

    Side Effects
    --------------------------
    Prints graph with population 1 vs. population 2 and best fit line
        in an independent window

    Exceptions
    ---------------------------
    TypeError raised if:
        The input file isn't a csv, doesn't have 3 columns,
        the final two columns aren't numeric type, there are fewer
        than 2 rows in the data frame
    ValueError raised if:
        There are null values in the input table
    """

    # Putting the file into pandas and testing
    if filepath[-4:] != '.csv':
        raise TypeError('File must be a csv')
    correlation_df = pd.read_csv(filepath)
    if len(correlation_df.columns) != 3:
        raise TypeError("CSV file must have exactly 3 columns")
    if (not is_numeric_dtype(correlation_df.iloc[:, 1]) or not
       is_numeric_dtype(correlation_df.iloc[:, 2])):
        raise TypeError("Data in 2nd and 3rd column must be numeric")
    if len(correlation_df) < 2:
        raise TypeError("Data must have at least 2 samples (rows)")
    if correlation_df.isnull().values.any():
        raise ValueError("Data may not have any null values")

    x_var = correlation_df.iloc[:, 1]
    y_var = correlation_df.iloc[:, 2]

    print("\nCORRELATION HYPOTHESIS TEST (1):\n"
          "\nThe program will perform a simple linear regression and "
          "calculate \nthe Pearson Correlation Coefficient for the "
          "independent and dependent populations.\n"
          "All tests use 0.05 level of significance and two-sided"
          " hypothesis tests.\n"
          "Researchers should verify independence, normality, "
          "constant variance and linearity.\n\n"
          "-------------------------RESULTS-------------------------"
          "\n")

    # Linear regression
    linear_regression = linregress(x_var, y_var, alternative="two-sided")
    intercept = linear_regression[1]
    slope = linear_regression[0]
    slope_pvalue = linear_regression[3]
    if slope_pvalue >= 0.05:
        print("FAIL TO REJECT null hypothesis of regression coefficient "
              "equal to zero\n"
              "WARNING: No statistically significant linear association"
              " between predictor and outcome \n")
    elif slope_pvalue < 0.05:
        print("REJECT null hypothesis of regression coefficient "
              "equal to zero\n")
        
    # Correlation
    pearson_results = pearsonr(x_var, y_var)
    corr_coeff = round(pearson_results[0], 4)
    p_value = pearson_results[1]
    if p_value >= 0.05:
        print("FAIL TO REJECT null hypothesis of no correlation")
    elif p_value < 0.05:
        print("REJECT null hypothesis of no correlation")
    print(f"Correlation coefficient: {corr_coeff}")
    print(f"p-value: {p_value}\n")
    print("---------------------------------------------------------"
          "\n")

    # Graphing the line of best fit and the data
    sns.scatterplot(x=x_var, y=y_var).set_title("Linear Regression")
    line_of_best_fit = []
    # pylint: disable=consider-using-enumerate)
    for i in range(len(x_var)):
        line_of_best_fit.append(intercept + slope*x_var[i])
    plt.plot(x_var, line_of_best_fit, color='orange')
    plot_label = (f"Line of best fit:\n y ="
                  f"{round(intercept,2)} + {round(slope,2)}*x")
    plt.text(0.02, 0.9, s=plot_label, transform=plt.gca().transAxes,
             bbox={"edgecolor": 'black', "facecolor": 'white',
                    "alpha":0.25})
    plt.show()
    return corr_coeff, p_value


def hypothesis_function_two(filepath):
    """
    This function will produce a graph with populations over time

    Arguments
    -------------------------------
    filepath: string
        Filepath to csv file for correlation analysis

    Return Values
    ----------------------------
    None

    Side Effects
    --------------------------
    Prints a graph with the first column on the x axis and the remaining
        columns on the y-axis

    Exceptions
    ---------------------------
    TypeError raised if:
        The input file isn't a csv, dataframe doesn't have >2 columns,
        the columns aren't all numeric
    ValueError raised if:
        Input file contains null values
    """

    # Putting the file into pandas and testing
    if filepath[-4:] != '.csv':
        raise TypeError('File must be a csv')
    graph_df = pd.read_csv(filepath)
    if len(graph_df.columns) < 2:
        raise TypeError("CSV file must have at least 2 columns")
    for i in range(len(graph_df.columns)):
        if not is_numeric_dtype(graph_df.iloc[:, i]):
            raise TypeError("Data must be numeric")
    if graph_df.isnull().values.any():
        raise ValueError("Data may not have any null values")

    print("\nTIME SERIES GRAPH (2):\n")
    # Creating the graphs using Seaborn
    x_var = graph_df.columns[0]
    graph_df_melted = graph_df.melt(x_var, var_name="Populations",
                                    value_name="Counts")
    sns.lineplot(data=graph_df_melted, x=x_var, y="Counts",
                 hue="Populations").set_title("Population(s) Over Time")
    # plot.set(xlabel='datetime')
    plt.show()
    # pylint: disable=too-many-locals


def hypothesis_function_three(filepath):
    """
    This function will perform 2-sample Z-tests for proportions and plot them
    over time

    Arguments
    -------------------------------
    filepath: string
        Filepath to csv file for hypothesis testing

    Return Values
    ----------------------------
    None

    Side Effects
    --------------------------
    Prints the results of the tests to the terminal and plots a graph in
    Seaborn

    Exceptions
    ---------------------------
    TypeError raised if:
        The input file isn't a csv
    ValueError raised if:
        The input file does not have at least 3 columns and 2 rows or there are
        null values in the input table
    """

    # Save the provided CSV as a pandas DataFrame
    if filepath[-4:] != ".csv":
        raise TypeError("Error: the provided file must be a CSV")
    prop_df = pd.read_csv(filepath)
    # Ensure the DataFrame is valid
    if not len(prop_df.axes[0]) >= 2:
        raise ValueError("Error: the provided CSV must have at least 2 rows")
    if not len(prop_df.axes[1]) >= 3:
        raise ValueError("Error: the provided CSV must have at least 3" +
                         " columns")
    if prop_df.isnull().values.any():
        raise ValueError("Error: the provided CSV must have no NaN values")
    print("\nPROPORTION HYPOTHESIS TEST (3):\n"
          "\nThe program will perform a 2-sample Z test for proportions at the"
          " 0.05 significance level for each provided variable.\n"
          "-------------------------RESULTS-------------------------"
          "\n")

    # Grab years
    time1 = prop_df[prop_df.columns[0]][0]
    time2 = prop_df[prop_df.columns[0]][len(prop_df.axes[0]) - 1]

    # Get populations for years of interest
    total_obs1 = prop_df[prop_df.columns[1]][0]
    total_obs2 = prop_df[prop_df.columns[1]][len(prop_df.axes[0]) - 1]
    total_obs_ls = [total_obs1, total_obs2]

    # drop first 2 columns
    df_dropped = prop_df.drop(columns=prop_df.columns[0:2], axis=1,
                              inplace=False)

    # for each column in dropped df
    for (col_name, col_data) in df_dropped.iteritems():

        # get counts
        successes_yr1 = col_data[0]
        successes_yr2 = col_data[len(prop_df.axes[0]) - 1]
        successes_ls = [successes_yr1, successes_yr2]

        # perform test
        test_stat, pval = proportions_ztest(successes_ls, total_obs_ls)

        print("****")
        print("VARIABLE: " + col_name + "\nNULL HYPOTHESIS: proportion in "
              "" + str(time1) + " = proportion in " + str(time2) + ".\n")

        prop1 = successes_ls[0] / total_obs_ls[0]
        prop2 = successes_ls[1] / total_obs_ls[1]

        # Reject null hypothesis
        if pval <= 0.05:
            print("Result: REJECT null hypothesis that \nproportion 1 of "
                  "" + str(prop1) + " = proportion 2 of " + str(prop2) + ".\n"
                  "Test Statistic: " + str(test_stat) + "\np-value: "
                  "" + str(pval) + "\n")

        # Fail to reject null hypothesis
        else:
            print("Result: FAIL TO REJECT null hypothesis that\nproportion 1 "
                  "of " + str(prop1) + " = proportion 2 of " + str(prop2)
                  + ".\n"
                  "Test Statistic: " + str(test_stat) + "\np-value: "
                  "" + str(pval) + "\n")

    print("------------------------------------------------------------------"
          "\n\n")

    # --------------------Plot the data------------------------------------

    pop_counts = prop_df.iloc[:, 1]
    mydatetime = prop_df.iloc[:, 0]

    # Drop first 2 cols
    df_dropped = prop_df.drop(columns=prop_df.columns[0:2], axis=1,
                              inplace=False)

    # Create a dataFrame with proportions instead of counts
    new_rows = []
    for index, row in df_dropped.iterrows():
        temp_row = row.copy()

        # create proportions
        # pylint: disable=consider-using-enumerate
        for i in range(len(row)):
            temp_row[i] = row[i] / pop_counts[index]

        new_rows.append(temp_row)
    df_prop_no_year = pd.DataFrame(new_rows)

    # add back in year
    df_prop = df_prop_no_year
    df_prop["datetime"] = mydatetime

    # Graph the data
    x_var = df_prop.columns[len(df_prop.axes[1]) - 1]
    df_prop_melted = pd.melt(frame=df_prop, id_vars=["datetime"],
                             var_name="Categories", value_name="Proportions")
    sns.lineplot(data=df_prop_melted, x=x_var, y="Proportions",
                 hue="Categories").set_title("Proportion(s) Over Time")
    plt.show()
