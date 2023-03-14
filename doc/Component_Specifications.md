# Component Specification Document

This document details the component specifications and interactions necessary to build the Wisconsin Wolf Analysis. It also contains a preliminary plan with tasks listed in priority order.

## Interaction Flow / Diagram
The software components detailed below interact to allow a user interested in answering wolf population hypotheses to pull data from PDFs and input the results into a statistical analysis generator. Not only could the user replicate our reported results given the same PDFs (Research Replicator persona), but they could also leverage the tool to do a similar analysis on different data (Research Expander persona). The output of the statistical analysis component will be used to inform our final report which will be publically avilable on GitHub (Report Reader persona).

![Interaction flow diagram for Wisconsin Wolf Analysis](./WisconsinWolfDiagram.drawio.pdf)

## Software Components:

### Software Component 1: Data Ingestion Component
    - Component overview: Ingests tabular data from locally stored PDF files

    - Inputs: 
        * Filepath to local directory containing downloaded PDF files with desired raw tabular data
        * Filepath to local directory where extracted data folders should be written.

    - Outputs: 
        * 1 directory per PDF filename passed in via input filepath
        * 1 directory in PDF filename directory containing successfully processed csv tables
        * 1 directory in PDF filename directory containing csv tables for review, these likely contain no usable data, but may be 

    - Design:
        * Module given filepath to local directory containing downloaded pdfs with tabular data
        * For each PDF:
            ** Create a directory with the name of the PDF
            ** Create three sub-directories, one for well-proccessed files, one for poorly-processed files requiring human review, and one for merged files that contain dataframes with the same column names
            ** Run extraction library on PDF
            ** Save each extracted table of information as a CSV in the correct file location based on the values and column headers in the extracted dataframe

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data that can be read by camelot
        * External library tool is able to identify at least all valid tabular data
        * The user has storage space on their device avilable to handle the new directories and files

### Software Component 2: Data Extraction Component
    - Component overview: This component searches through PDF file trees that have been created by the data ingestion component and extracts a yearly total data from a user-specified row-label, then combines all of the matching data and writes to a csv file.

    - Inputs:
        * List of PDF files to search through to extract data
        * A row label
        * An output file path
        * A column label for the extracted data when writing to the output file

    - Outputs: 
        * A csv file containing a "year" column and a column with the extracted data from the PDFs

    - Design:
        * For each PDF file 
            ** Import all of the data files deemed "good" by the data ingestion component
            ** Search through the data for a row labeled with the user-specified row label
            ** Store the total value (right-most column in the PDF data) from each matched row along with the year associated with that data point
        * After processing all PDF files, remove any duplicate entries and save the data to the output file.

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data 
        * PDFs have been run through the data ingestion component
        * The user has storage space on their device avilable to handle the new directories and files
            
    - How it uses other components:
        * Inputs for the Data Extraction Component are the object outputs from Data Ingestion Component
        * Outputs from the Data Extaction Component are the inputs to the Data Processing Component

### Software Component 3: Data Processing & Analysis File Creation Component
    - Component overview: This component was created to make our team's data processing repeatable and reusable. It will be tailored to the data used to answer our research question, but would be avilable to those wishing to re-do or update our analysis with new information.

    - Inputs: 
        * Two user-specified CSV files 
        * A column name from each file that the user would like to combine
        * An output path for the combined file

    - Outputs: 
        * CSV files with the data necessary to answer our statistical analysis questions

    - Design:
        * Component takes in two CSVs files and a column name from each file. The data from the specified column in each csv file will be combined and saved to the output file along with a column for year. All years that are in each csv will be included in the output file, but any year in only one file will be dropped. 

    - Assumptions:
        * The PDF parser was able to accurately and consistently extract information from the PDF reports.
        * The files contain a column labeled "year"
            
    - How it uses other components:
        * The inputs for this component are the outputs from the Data Ingestion and Data Extractor Component

### Software Component 4: Statistical Analysis Wrapper Component
    - Component overview: This componet querries the user for which hypothesis tests they would like to perform and requests CSV files to execute the analysis.

    - Inputs: Number(s) representing the hypothesis test(s) the user would like to perform. CSV file(s) to execute the hypothesis test(s).

    - Outputs: 
        * Filepath(s) to CSV documents for analysis

    - Design:
        * When module is called, it will ask the user if they would like to statistically test the correlation between two variables (1), examine trends over time (2), or compare two proportions (3)
        * The user will input a list of numbers corresponding to the hypotheses they would like to test
        * The program will store the user input
        * IF TIME: Component will check validity of user input (e.g., user inputs an array, all elements are ints, all elements are between 1 and 3)
        * Based on the hypothesis numbers entered, component gives the user a brief description of data format required and solicits a filepath to a csv
        * Componet passes the csv filepaths to each of the respective hypothesis tests

    - Assumptions:
        * Without the component checking the user input, we must assume they follow the directions and input an array of numbers
        * CSV filepaths will be tested in the individual components, and thus requires no tests or assumptions here
            
    - How it uses other components:
        * Passes filepath(s) to the statistical analysis component
        * User replicating our research would input CSV files created from the Data Processing & Analysis File Creation Component

### Software Component 5: Statistical Analysis Component
    - Component overview: Provides reusable analysis and visualization tool for users interested in investigating wolf populations hypotheses.

    - Inputs: 
        * Tabular data necessary to answer each question (our questions used as examples below):
            ** Is there a correlation between the growth of the wolf population and changes in the deer population? (Annual wolf population data and deer population data)
            ** Is there a correlation between fewer sick deer and wolf population growth? (Annual wolf population data and deer sickness data)
            ** How are wolf and human interactions changing via observations, attacks, and law enforcement encounters? (Annual report data for each of the above)
            ** Is there a correlation in # of deer seen per hour by hunters and growing wolf populations? (Annual wolf population data and number of deer seen by hunters annually)
            ** Is there a correlation between growth in wolf population and # of deer harvested? (Annual wolf population data and annual deer harvesting data)
            ** Additional questions to be added, time permitting

    - Outputs: 
        * Hypothesis Function One:
            ** Scatter plot of raw data with best fit line
            ** Null hypothesis of linearity and rejection/failure to reject ** Null hypothesis of no correlation and rejection/failure to reject
            **Pearson's correlation coefficient, and p-value for correlation statistical test
        * Hypothesis Function Two:
            ** Line graph of first column vs. populations (columns 2+) 
        * Hypothesis Function Three:
            ** Line graphs of proportions over time
            ** Null hypothesis, results of 2-sided z-test

    - Design:
        * Hypothesis function 1: Correlation between two variables/populations
            ** The function validates the dataframe and outputs an error message if necessary
            ** If no error in the dataframe format/content:
                *** The function will alert the user that it is running a simple linear regression and calculating the Pearson Correlation Coefficient
                *** Run statistical test
            ** After the test is run:
                *** The function outputs if the null hypothesis of no linear relationship can be rejected, if the null hypothesis of no correlation can be rejected, the correlation coefficient, and the p-value for the correlation coefficient
                *** The function also outputs a graph of population 1 vs population 2 datapoints fitted with a trendline, giving the user the option to save the visualization  

        * Hypothesis function 2: Examining trends over time
            ** The function validates the dataframe and outputs an error message if necessary
            ** The function outputs a graph of the population(s) (columns 2+) over the first column fitted with trendline(s) and titles, giving the user the option to save the visualization
        
        * Hypothesis function 3: Comparing two proportions 
            ** The function validates the dataframe and outputs an error message if necessary
            ** If no error in the dataframe format/content the function will:
                *** Notify the user that it will perform a 2-sample Z test for proportions with a 0.05 significance level to make inferences about the hypotheses
                *** Notify the user of the two values in the  first column of the provided dataframe that will be used for the 2 samples
            The function outputs:
                *** The test statistic, p-value, and whether or not the null hypothesis was rejected, for each of the 2-sample proportion tests performed
                *** A line chart showing the change in the second+ columns over time

    - Assumptions:
        * Data necessary to answer questions has been combined across separate PDFs/tables into single dataframes
        * Dataframes are in a usable format
        * The user is familiar with the data and column/row names contained within their dataframes
    
    - How it uses other components:
        * The user will need to leverage the CSV outputs from the first two components to form dataframes which are fed into this component

## Preliminary Plan
    - Week of 2/20
        * Finalize technology review presentation (2/21)
        * Finalize component specifications (2/21)
        * Develop testcases for data ingestion
        * Develop testcases for data checking
        * Develop testcases for statistical analysis
        * Create pseudo-code of components
    - Week of 2/27
        * Build and test data ingestion
        * Build and test data checking
        * Build and test statistical analysis
    - Week of 3/6
        * Refine and correct any outstanding issues from week of 2/27
        * Develop and finalize presentation
    - Week of 3/13
        * Deliver final presentation
