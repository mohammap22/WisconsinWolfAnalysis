## pdf parser Walkthrough and Example 

## Background and Use Case
- The data used in the Wisconsin Wolf Analysis mostly came from tables in PDF documents.
- Using the python package Camelot, we constructed a script that parses through given PDF file(s) and outputs CSVs in subfolders.
- This document will help those with limited coding experience use this tool.

## Before Use

- Install all the required packages information in **doc/development.md**
- The pdf parser script is located within the **WisconsinWolfAnalysis** folder.
- Install the PDF file(s) you want to extract data from and add it into the same directory as pdf_parser.py
- Activate the `wolf_env` virtual environment by running `conda activate wolf_env` from the git repository in the command line. 


## How to Use

- Open the `pdf_parser.py` file (in a text document or IDE)
- Scroll to the bottom of the file and create a new variable like so
`PDF_LIST = [‘YOUR_PDF_FILE_NAME.pdf’, ‘OTHER_PDF_NAME.pdf’]`
> **Note:** This list can contain a single element instead of multiple depending on how many files you want to parse.
- Then call the function within the python code like so
`pdf_parser(PDF_LIST, 'pdf/')`
>**Note:** This will send the extracted csv files to a new subfolder called **pdf**. The name of the folder can be whatever string you want it to be. 
- Finally run the python script from terminal 
`python pdf_parser.py`
>**Note:** Might need to use python3 instead of python depending on your specific installation 
 
## Example 
- This example came from running pdf parser on the pdf file **WolfReport2022.pdf**
- Many csv files were created, here is single output from page 12 of the report:
![Alt text](pdf_parser_example_input.JPG  "PDF version")
![Alt text](pdf_parser_example_output.JPG  "CSV version")


