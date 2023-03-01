### How to Install PDF Parser Dependencies

## Introduction
There are a few specific dependies required (based on user OS) to use our PDF Parser. 
The main dependency is a package called Camelot. 
This document will guide the user on how to setup their specific environment. 

## General Dependencies 
User needs to have python 3.0 or greater installed. 
This is so the installation of ghostscript and tkinter goes smoothly. 

## For Ubuntu Users
Run the command:
`apt install ghostscript python3-tk`

This command installs both ghostscript and tkinter. 

## For Mac Users
Run the command:
`brew install ghostscript tcl-tk`

## After Installation
One needs to import tkinter before running anything in camelot. 
In python run the code `import tkinter` 

## Extra Information
[Camelot Documentation](https://camelot-py.readthedocs.io/en/master/user/install.html)
[Tkinter Documentation](https://wiki.python.org/moin/TkInter)
[Ghostscript Documentation](https://www.ghostscript.com/) 

