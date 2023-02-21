# Component Specification Document

This document details the component specifications and interactions necessary to build the Wisconsin Wolf Analysis. It also contains a preliminary plan with tasks listed in priority order.

## Interaction Flow / Diagram
The software components detailed below interact to allow a user interested in answering wolf population hypotheses to pull data from PDFs and input the results into a statistical analysis generator. Not only could the user replicate our reported results given the same PDFs (Research Replicator persona), but they could also leverage the tool to do a similar analysis on different data (Research Expander persona). The output of the statistical analysis component will be used to inform our final report which will be publically avilable on GitHub (Report Reader persona).

![Interaction flow diagram for Wisconsin Wolf Analysis](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=WisconsinWolfDiagram.drawio#R7Vxbk6I4GP01Pk4X4e5jt%2FZcqmZruqa3Zmf2DSFqppEwEEfdX78JJChJUFpFcapfWhJCgJOT810SemCNFusPWZDO%2F8IRjAemEa0H1nhgmgAYDv1hNZuyxvVAWTHLUMQbbSue0X%2BQVxq8dokimNcaEoxjgtJ6ZYiTBIakVhdkGV7Vm01xXL9rGsygUvEcBrFa%2Bw%2BKyLys9R1jW%2F8RotmcVC%2FMzywC0ZhX5PMgwqudKutxYI0yjEl5tFiPYMzAE7iU171vOFs9WAYT0uaCb%2FPlkwf%2FRcOvOP01%2Ffj3r%2BU6fydg%2Fh3ES%2F7G%2FGnJRkAwy%2FAy5c1gRuBaB3wwEc0N9cFA9bqUJxAvIMk2tAnvyBSQbUS5LK62eFdN5rtYi4YBH%2BNZ1fUWBnrAkXgFKp4Cyhhl9CVx8dgjnJAAJSiZ0cLT%2BD39%2Bx7FlKQycPkKLeIgoaWH1RwR%2BJwGITu1olOF1s3Jgj7VGNDDRnR3UdwzgCq21wPPVMArMQIqPvMgZYcJJi0wmgThC6NiEn1ZkhgxWIv6KMhevtCrEGH8Me6o4lgPeSkkwD8JXG8vb0GdtrZKW0cDvNsV7n4D7uqE7j3uTaTm3Xhur4AfNgBv%2FXHAA9vsFfLAOWy9YBLdMz%2BAlsI4yHMU1lEuAIbsLgYtTam2cycE2LQM14h8L1B2eOkHv44dj9f8sqKwEYWEvtvORaz4Y%2Ffc9rKiJK4rHx1GikMiGVL6eniZhfCwASNBNoN7x7vBMh8YUFGXwTgg6Hf9eXWjzO%2FwhBF9k4pOlqSg5lAiSvme%2FKpd10buyJU6sqWOSiCUjgrSVa99Ag%2FdvQ7DlHoHKXMHZW7S%2BUnqbMxJhl%2FgCMc4K3SicB7o9bFUFcRoljBKU2pAWv%2FAZjuibus9P7FAURQ3iUwz58228nHApRvatQEBtq0oBQAaZlmdeSWqT6cMR%2BeOrrinQMVTUbGBraICBMHOr6DgMCw7bmxOJ5LgirGPdcebILPB6RLxo8ojx9Uh1pnNUf3bcUACWvMpmcGcIJwMTDdm83qS1YB0fy1ZrFfMt3elvb5nfrGdrgvExHl6NGO%2FI7xI6WznkrVfN9rrQQbprTmJ2RCmTBQLkJyHgTNmfS0JFu6EIkkDKrahDydTSZdofRRAfxpqjGhR5k8PjmdGk7ES3fi1yWWpvkkV8%2Bhs2fmJYt3K1BLy5NQRvP5Us5um2mgOw5ciAH%2BbaV3MNOu2ZloL2358GGDWXPqaQ39nVg5%2Bg08v4gcRMexe1hhADA4HAnt9nIPhgbD6h%2BODBiJcJj7w6zwDhuQFtQ0PgFXvyJH66To6UDMznyI6kmiKKOHYKDCNMA08%2Bcky2H9QkHCMFQKepciJ56gc6yxSAGo%2Bpys1AXU18dqqiVFTE%2B%2FaamK1VZOrZhtk98Y%2FMtlQOUEN%2FXSsJsKy7tCTrT4UI8pSDEaQMFFBSZjBBZv40a6TVPo7IaUnU4Q3qamP5LCV8ohcxvlzFKqhOLfy3GY6s7W%2FYl7VX1HymXLi%2B%2Bh8phxidawxrprPVIlIB1aEGjgjczzDSRA%2FbmslKm7bfMY45az7CQnZcIKyYKjOZTm6OSOjzLY2y3X0jGpNldMUQc0h9GEl%2BkAixqqz19IEiJatmYagswjRUgm9F66%2Br9M16VzDyjRgEac8BNqVOu%2FO6WoI1CC92hdgjJ6%2FnULaM3oM%2B4H1TIFPc%2B7D1zG7sxyZrUYrHzCOzoupcRKm1n4vTAb0zvJUsnq6tSLrzuuKrY7qZX%2BFvxFc3SywHhUgowfANsmAeUMyACT%2F7Ooq4KiRQ99UwLlFFVDFtX8q8Cpge6ICriqv1Z6pm1GByoPqiwq46mJ%2B31TA3b%2FBrJcq4Jo3oAKvArYnKiC2v1w2q3BMDqzDTITL0T2cifD1I3yZTISrbrV8ynAIc0p%2F43FNsiAsUs18RhgoobibBluvn5YxtjHFGf17T8dqk6PmoDvl3R4dd5%2B%2BKP667xUcoAq%2Fds%2B9vL3xfIOjOtX3LEfUiPFyEZcNton6z8EExk84R8UOJms8wYTghSaTT7A0DrhEf1R9gdM8Y07LK0n21tF8KGLpkhqdwd4iX3%2FMDp%2Bm3R7N%2B0POwWrx8GL3j2Zz94X3%2F7iq%2B%2F1MqNblBWw1LZFXuN529LQzHmLBQfK7NCN%2FyQ09npqu3Q61QdU%2BXbLVEvWLorpz8MpAQS9057YeYJtjFd7YUIO3bgNVdzPN08y0MCB0OqQxJsWjFWvLU0RKK0%2Fo60aFzT3rEJwDX0%2FG1weqqwt09tnqytH11XC3LmRfYb6MieoT9RBMV0PWy4KpRrk6cVBN8Q2IgwXkBYYeiIOvxr9acag0oX88tkwZ19ai0Fn063f68doN7%2FYQbvXBiLh0E%2Fqy28M7ereHXe%2FIvfDXa36b3R5vRDxokq62sXEo8efozyg7IyItbv%2FRRdl8%2B%2B9CrMf%2FAQ%3D%3D)

## Software Components:

### Software Component 1: Data Ingestion Component
    - Component overview: Ingests tabular data from locally stored PDF files

    - Inputs: Filepath to local directory containing downloaded PDF files with desired tabular data

    - Outputs: 
        * 1 directory per PDF filename passed in via input filepath
        * 1 directory containing successfully processed tables
        * 1 directory containing poorly-processed tables for review
        * Summary table of files read in per PDF and what folder they went into (e.g., 6 tables were successfully processed and stored in the XX folder. 5 tables were unsuccessfully processed and stored in the YY folder for review.)
        * (intermediate, passed to Data Checking Component) Object for each table identified in each PDF

    - Design:
        * Module given filepath to local directory containing downloaded pdfs with tabular data
        * For each PDF:
            ** Create a directory with the name of the PDF
            ** Create two sub-directories, one for well-proccessed files and one for poorly-processed files requiring human review
            ** Run extraction library on PDF
            ** Pass each object representing an identified table to Data Checking Component for quality validation and generation of storage location
            ** Save each extracted table of information as a CSV in the correct file location as determined by the Data Checking Component

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data
        * External library tool is able to identify at least all valid tabular data
    
    - How it uses other components:
        * Leverages Data Checking Component to generate filepaths used to store CSV table outputs

### Software Component 2: Data Checking Component
    - Component overview: This component performs a light quality validation of each extracted object representing an identified table and returns the best storage filepath

    - Inputs: Object for each table identified in each PDF from Data Ingestion Component

    - Outputs: 
        * Filepath with extracted table save location based on data quality
        * Incremented counter for Data Ingestion Component summary output (COULD WE DO THIS AS A READER IN THE FIRST ONE)

    - Design:
        * For each object passed to Data Checking Component from Data Ingestion Component:
            ** Perform light quality check on object - does it contain any values for the columns and rows, are dimensions valid others to be developed as test external PDF parse library further
            ** Based on the outcome of the light quality checks, return a filepath to save the object to (e.g., pdf_name/successfully_parsed or pdf_name/for_review)
            ** Increment counter for filepaths generated with "successfully_parsed" vs. "for_review"

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data
        * External library tool is able to identify and generate objects for at least all valid data tables
        * External library tool returns a examinable dataframe
            
    - How it uses other components:
        * Inputs for Data Checking Component are outputs from Data Ingestion Component
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
            ** Null hypothesis, statistical test, and results of statistical test used to test each hypothesis where applicable

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
                *** The function also outputs a graph of the population 1 vs population 2, datapoints fitted with a trendline, and titles, giving the user the option to save the visualization  

        * Hypothesis function 2: Examining trends over time
            ** The function asks the user for a dataframe with at least 2 columns - the first must be a datetime, and the second+ is/are a variable 
            ** The function validates the dataframe and outputs an error message if necessary
            ** If no error in the dataframe format/content, the function asks which trends (via column names) the user wants to graph over time and verifies the request is valid
            ** The function outputs a graph of the population(s) over time fitted with trendline(s) and titles, giving the user the option to save the visualization

    - Assumptions:
        * Data necessary to answer questions has been combined across separate PDFs/tables into single dataframes
        * Dataframe is in a usable format
    
    - How it uses other components:
        * The user will need to leverage the CSV outputs from the first two components to form dataframes which are fed into this component.

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
