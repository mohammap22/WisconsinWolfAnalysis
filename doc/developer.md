# How to Install PDF Parser Dependencies

## Introduction
There are a few specific dependies required (based on user OS) to use our PDF Parser. 
The main dependency is a package called Camelot. 
This document will guide the user on how to setup their specific environment. 

## General Dependencies 
User needs to have python 3.0 or greater installed. 
This is so the installation of ghostscript and tkinter goes smoothly. 

## For Ubuntu Users
Run the command:
`sudo apt install ghostscript python3-tk`

This command installs both ghostscript and tkinter. 

## For Mac Users
Run the command:
`sudo brew install ghostscript tcl-tk`

## After Installation
One needs to import tkinter before running anything in camelot. 
In python run the code `import tkinter`

## Set-Up Virtual Environment
- If you haven't already, clone the WisconsinWolfAnalysis repository to your local machine. 
- Navigate to the repo in the command line. Then, create a new environment by entering the command `conda env create -f environment.yml`. It may take a while to install all of the packages. 
- Before running any of the scripts or modules from the project, be sure to switch to the environment you just created in the previous step by entering `conda activate wolf_env`. 

## Extra Information
[Camelot Documentation](https://camelot-py.readthedocs.io/en/master/user/install.html)

[Tkinter Documentation](https://wiki.python.org/moin/TkInter)

[Ghostscript Documentation](https://www.ghostscript.com/) 

