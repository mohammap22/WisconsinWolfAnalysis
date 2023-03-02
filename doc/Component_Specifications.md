# Component Specification Document

This document details the component specifications and interactions necessary to build the Wisconsin Wolf Analysis. It also contains a preliminary plan with tasks listed in priority order.

## Interaction Flow / Diagram
The software components detailed below interact to allow a user interested in answering wolf population hypotheses to pull data from PDFs and input the results into a statistical analysis generator. Not only could the user replicate our reported results given the same PDFs (Research Replicator persona), but they could also leverage the tool to do a similar analysis on different data (Research Expander persona). The output of the statistical analysis component will be used to inform our final report which will be publically avilable on GitHub (Report Reader persona).

![Interaction flow diagram for Wisconsin Wolf Analysis](./WisconsinWolfDiagram.drawio.pdf)

## Software Components:

### Software Component 1: Data Ingestion Component
    - Component overview: Ingests tabular data from locally stored PDF files

    - Inputs: Filepath to local directory containing downloaded PDF files with desired raw tabular data

    - Outputs: 
        * 1 directory per PDF filename passed in via input filepath
        * 1 directory in PDF filename directory containing successfully processed csv tables
        * 1 directory in PDF filename directory containing csv tables for review
        * Summary table of files read in per PDF and what folder they went into (e.g., 6 tables were successfully processed and stored in *filepath*. 5 tables were unsuccessfully processed and stored in *filepath* for review.)
        * (intermediate, passed to Data Checking Component) Object for each table identified in each PDF

    - Design:
        * Module given filepath to local directory containing downloaded pdfs with tabular data
        * For each PDF:
            ** Create a directory with the name of the PDF
            ** Create two sub-directories, one for well-proccessed files and one for poorly-processed files requiring human review
            ** Run extraction library on PDF
            ** Pass each object representing an identified table to Data Checking Component for quality validation, generation of storage location, and incremented counter
            ** Save each extracted table of information as a CSV in the correct file location as determined by the Data Checking Component

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data
        * External library tool is able to identify at least all valid tabular data
        * The user has storage space on their device avilable to handle the new directories and files
    
    - How it uses other components:
        * Leverages Data Checking Component to generate filepaths used to store CSV table outputs and increment counter for summary table

### Software Component 2: Data Checking Component
    - Component overview: This component performs a light quality validation of each extracted object representing an identified table and returns the best storage filepath and incremented counter. Optional scope increase could include more robust validation of objects.

    - Inputs: Objects representing each table identified in each PDF from Data Ingestion Component

    - Outputs: 
        * Filepath with extracted table save location based on data quality
        * Incremented counter for Data Ingestion Component summary output

    - Design:
        * For each object passed to Data Checking Component from Data Ingestion Component:
            ** Perform light quality check on object - does it contain any values, are dimensions valid, etc.
            ** Based on the outcome of the light quality checks, return a filepath to save the object to (e.g., pdf_name/successfully_parsed or pdf_name/for_review)
            ** Increment counter for filepaths generated with "successfully_parsed" vs. "for_review"

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data
        * External library tool is able to identify and generate objects for at least all valid data tables
        * The user has storage space on their device avilable to handle the new directories and files
        * External library tool passes a usable dataframe for validation
            
    - How it uses other components:
        * Inputs for the Data Checking Component are the object outputs from Data Ingestion Component
        * Returns the generated filepath and counter to the Data Ingestion Component

### Software Component 3: Data Processing & Analysis File Creation Component
    - Component overview: This component was created to make our team's data processing repeatable and reusable. It will be tailored to the data used to answer our research question, but would be avilable to those wishing to re-do or update our analysis with new information.

    - Inputs: CSV files generated by the Data Ingestion and Data Checking Components

    - Outputs: 
        * CSV files with the data necessary to answer our statistical analysis questions

    - Design:
        * Component takes in two or more CSVs from directory of PDF files and combines them to match specifications of example files

    - Assumptions:
        * The PDF parser was able to accurately and consistently extract information from the PDF reports
            
    - How it uses other components:
        * The inputs for this component are the outputs from the Data Ingestion and Data Checking Component

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
            ** Time-series visualization of data and trends
            ** Null hypothesis, statistical test, and results of correlation statistical test
        * Hypothesis Function Two:
            ** Time-series visualization of data and trends
        * Hypothesis Function Three:
            ** Graphical Output
            ** Null hypothesis, statistical test, and results of statistical test

    - Design:
        * Hypothesis function 1: Correlation between two variables/populations
            ** The function asks the user for a dataframe with 3 columns, 1st is date/time, 2nd is population 1 data, 3rd is population 2 data (opportunity to increase scope by handling imperfect dataframe inputs e.g., only running the test on rows with data in both columns)
            ** The function validates the dataframe and outputs an error message if necessary
            ** If no error in the dataframe format/content:
                *** The function will alert the user that it is running a simple linear regression with robust standard errors (opportunity to increase scope by letting users pick alternate tests)
                *** Run statistical test
            ** After the test is run:
                *** The function outputs the correlation, best fit line equation, and interpretation
                *** The function also outputs a graph of population 1 vs population 2 datapoints fitted with a trendline, giving the user the option to save the visualization  

        * Hypothesis function 2: Examining trends over time
            ** The function asks the user for a dataframe with at least 2 columns - the first must be a datetime, and the second+ is/are a variable 
            ** The function validates the dataframe and outputs an error message if necessary
            ** If no error in the dataframe format/content, the function asks which trends (via column names) the user wants to graph over time and verifies the request is valid
            ** The function outputs a graph of the population(s) over time fitted with trendline(s) and titles, giving the user the option to save the visualization
        
        * Hypothesis function 3: Comparing two proportions
            ** The function asks the user for a dataframe with at least 3 columns - the first must be a datetime, the second must be the total number of observations, and the third+ be the number of observations with a specific characteristic of interest 
            ** The function validates the dataframe and outputs an error message if necessary
            ** If no error in the dataframe format/content the function will:
                *** Notify the user that it will perform one or more hypothesis tests and state them in terms of the columns provided. It will also state that it will run a 2-sample Z test for proportions with a 0.05 significance level to make inferences about the hypotheses
                *** Notify the user of the two values in the datetime column of the provided dataframe that will be used for the 2 samples
            The function outputs:
                *** The test statistic, p-value, and whether or not the null hypothesis was rejected, for each of the 2-sample proportion tests performed
                *** A line chart showing the change in the third+ columns over time

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
