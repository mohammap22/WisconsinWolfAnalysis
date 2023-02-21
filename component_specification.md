# Component Specification Document

This document details the component specifications and interactions necessary to build the Wisconsin Wolf Analysis. It also contains a preliminary plan with tasks listed in priority order.

"""
This documents provides the component specifications due in class 2/21.

Its sections include:
    Software components. High level description of the software components such as: data manager, which provides a simplified interface to your data and provides application specific features (e.g., querying data subsets); and visualization manager, which displays data frames as a plot.
    
    Describe at least 3 components specifying: what it does, inputs it requires, and outputs it provides. If you have more significant components in your system, we highly suggest documenting those as well.

    Interactions to accomplish use cases.
    Describe how the above software components interact to accomplish your use cases. Include at least one interaction diagram.
    
    Preliminary plan. A list of tasks in priority order.

Items to include:

interactions
interaction diagram
preliminary plan
"""

## Interaction Flow / Diagram
User collects the pdfs to be used in the analysis and saves them locally -> User gives software component 1 filepath to directiory where pdfs are stored -> Software component 1 runs (calling software component 2) to extract and save CSVs of tabular data contained in the PDFs -> User combines the CSV tabular data files into a single dataframe for input to software component 3 -> User selects which tests they want to run and software component 3 ouputs the visualizations, statistical tests used, and results

## Software Components:

### Software Component 1: External Library Data Processing Component
    - Component overview: Ingests tabular data from locally stored PDF files

    - Inputs: Filepath to local directory containing downloaded PDF files with desired tabular data

    - Outputs: 
        * 1 directory per PDF filename passed in via input filepath
        * 1 directory containing successfully processed tables
        * 1 directory containing poorly-processed tables for review
        * Summary table of files read in per PDF and what folder they went into (e.g., 6 tables were successfully processed and stored in the XX folder. 5 tables were unsuccessfully processed and stored in the YY folder for review.)
        * (intermediate, passed to Internal Logic Data Processing Component) Object for each table identified in each PDF

    - Design:
        * Module given filepath to local directory containing downloaded pdfs with tabular data
        * For each PDF:
            ** Create a directory with the name of the PDF
            ** Create two sub-directories, one for well-proccessed files and one for poorly-processed files requiring human review
            ** Run extraction library on PDF
            ** Pass each object representing an identified table to Internal Logic Data Processing Component for quality validation and generation of storage location
            ** Save each extracted table of information as a CSV in the correct file location as determined by the Internal Logic Data Component

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data
        * External library tool is able to identify at least all valid tabular data
    
    - How it uses other components:
        * Leverages Internal Logic Data Processing Component to generate filepaths used to store CSV table outputs

### Software Component 2: Internal Logic Data Processing Component
    - Component overview: This component performs a light quality validation of each extracted object representing an identified table and returns the best storage filepath

    - Inputs: Object for each table identified in each PDF from External Library Data Processing Component

    - Outputs: 
        * Filepath with extracted table save location based on data quality
        * Incremented counter for External Library Data Processing Component summary output (COULD WE DO THIS AS A READER IN THE FIRST ONE)

    - Design:
        * For each object passed to Internal Logic Data Processing Component from External Library Data Processing Component:
            ** Perform light quality check on object - does it contain any values for the columns and rows, are dimensions valid others to be developed as test external PDF parse library further
            ** Based on the outcome of the light quality checks, return a filepath to save the object to (e.g., pdf_name/successfully_parsed or pdf_name/for_review)
            ** Increment counter for filepaths generated with "successfully_parsed" vs. "for_review"

    - Assumptions:
        * User has found, downloaded, and stored PDF information locally
        * PDFs contain tabular data
        * External library tool is able to identify and generate objects for at least all valid data tables
        * External library tool returns a examinable dataframe
            
    - How it uses other components:
        * Inputs for Internal Logic Data Processing Component are outputs from External Library Data Processing Component

### Software Component 3: Analysis Tool and Graphical Generator Component
    - Component overview: Provides reusable analysis and visualization tool for users interested in investigating hypothesis regarding wolf populations.

    - Inputs: 
        * Tabular data necessary to answer each question:
            ** Is there a correlation between the growth of the wolf population and changes in the deer population? (Annual wolf population data and deer population data)
            ** Is there a correlation between fewer sick deer and wolf population growth? (Annual wolf population data and deer sickness data)
            ** How are wolf and human interactions changing via observations, attacks, and law enforcement encounters? (Annual report data for each of the above)
            ** Is there a correlation in # of deer seen per hour by hunters and growing wolf populations? (Annual wolf population data and number of deer seen by hunters annually)
            ** Is there a correlation between growth in wolf population and # of deer harvested? (Annual wolf population data and annual deer harvesting data)
            ** Additional questions to be added, time permitting

    - Outputs: 
        * For each question:
            ** Time-series visualization of data and trends
            ** Null hypothesis, statistical test, and results of statistical test used to test each hypothesis

    - Design:
        *  6 functions
            ** One runs after the module is called
                *** It instructs user on what data format is required to run the program
                *** If the user agrees that their data is in the correct format, get filepath of dataframe
                *** Verify dataframe contains correct columns, outputting an error message if not
                *** Ask the user if they would like to run each test/hypothesis
                *** Run the necessary tests
            ** For each hypothesis:
                *** Execute correct statistical test
                *** Output the result of the statistical test
                *** Output visualization with data trendlines, giving the user the option to save it

    - Assumptions:
        * Data necessary to answer questions has been combined across separate PDFs/tables into a single dataframe
        * Dataframe is in a usable format (e.g., pandas)
    
    - How it uses other components:
        * The user will need to leverage the CSV outputs from the first two components to form a single dataframe whcih is then fed into this component.

## Preliminary Plan
    - Week of 2/20
        * Finalize technology review presentation (2/21)
        * Finalize component specifications (2/21)
        * Split work between team members
        * Develop testcases for component 1
        * Develop testcases for component 2
        * Develop testcases for component 3
        * Create pseudo-code of components
    - Week of 2/27
        * Build component 1
        * Test component 1
        * Build component 2
        * Test component 2
        * Build component 3
        * Test component 3
    - Week of 3/6
        * Continue to correct any issues from 2/27
        * Develop and finalize presentation
    - Week of 3/13
        * Deliver final presentation
