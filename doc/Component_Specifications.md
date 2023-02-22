# Component Specification Document

This document details the component specifications and interactions necessary to build the Wisconsin Wolf Analysis. It also contains a preliminary plan with tasks listed in priority order.

## Interaction Flow / Diagram
The software components detailed below interact to allow a user interested in answering wolf population hypotheses to pull data from PDFs and input the results into a statistical analysis generator. Not only could the user replicate our reported results given the same PDFs (Research Replicator persona), but they could also leverage the tool to do a similar analysis on different data (Research Expander persona). The output of the statistical analysis component will be used to inform our final report which will be publically avilable on GitHub (Report Reader persona).

![Interaction flow diagram for Wisconsin Wolf Analysis](./info_flow_diagram.drawio.pdf)

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


### Software Component 3: Statistical Analysis Component
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
        * For each question:
            ** Time-series visualization of data and trends
            ** Null hypothesis, statistical test, and results of statistical test where applicable

    - Design:
        * When module is called, it will ask the user if they would like to statistically test the correlation between two variables (1), or examine trends over time (2)
        * The user will input a list of which (or both) of the numbered hypotheses they would like to test
        * The program will validate and store the user input
        * Based on the user input, the program will run the corresponding hypothesis function(s)

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
