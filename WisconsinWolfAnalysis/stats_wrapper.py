from stats_module import *


def wrapper():
    options_str = input("------------------Statistical Analysis---------------\n"
          "Hello! Would you like to statistically test the correlation between "
          "two variables (1) examine trends over time (2), and/or compare "
          "two proportions (3)? \nPlease enter a comma separated list of the "
          "desired options.\n")
    
    options_ls = options_str.split(",")
    
    #------------------Check for illegal input-----------------
    #<1 or >3 options specified
    if (len(options_ls) < 1) or (len(options_ls) > 3):
        raise ValueError("Invalid Input: User must provide between 1 and 3 "
                         "options.")
    
    # #xxxxNo null values
    # if ()
    
    # #repeated option
    
    # #not a number
    # ones = 0
    # twos = 0
    # threes = 0
    # for elt in options_ls:
    #     if elt  == '1':
    #         ones = ones + 1
        
    #     elif elt == '2':
    #         twos = twos + 1
        
    #     elif elt == '3':
    #         threes = threes + 1
        
    #     else:
    #         raise ValueError("Invalid Input: The only valid options are: 1,2,3")
    
    #Perform the requested tasks
    for option in options_ls:
        if option == '1':
            filepath = input("You have selected option 1: testing correlation "
                             "between two variables. \nPlease provide the file "
                             "path to the CSV file containing the data you "
                             "wish to use. \nNote, the CSV must contain 3 "
                             "columns; the 1st is date/time, the 2nd is "
                             "population 1 data, and the 3rd is population 2"
                             "data.\n")
            
            hypothesis_function_one(filepath)
        
        elif option == '2':
            pass#do something
        
        elif option == '3':
            pass#do something
        else:
            raise ValueError("A non permitted ")

if __name__ == '__main__':
    wrapper()
