# Functional Specification:

## Background:
The goal of this project is to perform a statistical analysis on the impact of the Gray Wolf population in Wisconsin in order to support or refute commonly held concerns about the impacts of Gray Wolves

Questions of Interest:
- How has the growth in the Wisconsin Gray Wolf population impacted the Wisconsin deer population?
- Has the growing wolf population led to an increase in the number of interactions between people and wolves?
- Time permitting, how have the lives and deaths of wolves changed over the reporting period?

## User Profile/Stories:

### Story 1: Research Replicator
- Who: 
    * An individual with some technical and research experience who desires to
    repeat our analysis to verify its integrity or to learn new techniques. 
- Wants:
    * They wish to rerun our data cleaning and analysis procedures with the same
    data to validate our results.
- Interaction Methods:
    * The researcher will need access to the script or Jupyter Notebook used in
    the analysis.
    * They will also need the data interface requirements to use new data with
    our script.
- Needs
    * If we generate any random numbers or draw randomly from distributions in
    our statistical analysis, they will need the seed we use.
    * The researcher will need documentation on the interface requirements that
    must be met to link a data source to the scripts used in our analysis. 
- Skills
    * The researcher must have the ability to replicate results with a moderate
    degree of documentation highlighting our unique implementation or
    application of common programming packages and statistical techniques.

### Story 2: Research Expander
- Who: 
    * The Research Expander is an individual who wishes to build upon our work
    and take it in new directions. They also may posses more technical skills
    than the Research Replicator. 

- Wants:
    * This researcher desires to expand upon the work that we do in our analysis
    and take it in a new direction.

- Interaction Methods:
    * Like the Research Replicator, this person will need access to the scripts
    or Jupyter Notebooks used in the analysis to see our code.
    * They will also need Data interface requirements to know how to link their
    own data to the program we created to perform our analysis.
- Needs
    * If we generate any random numbers or draw randomly from distributions in
    our statistical analysis, they will need the seed we use.
    * The researcher will need documentation on the interface requirements that
    must be met to link a data source to the scripts used in our analysis.
    * Additionally, they will need detailed documentation explaining our
    analysis process so that they can identity what and where they will modify
    things to suit their needs. 

- Skills
    * Ability to replicate and expand upon results with moderate documentation
    highlighting our unique implementation or usage. 
    * Knowledge of software development, comfortable using the terminal and
    running scripts.

### Story 3: A Reader
- Who: 
    * Someone who finds the report documenting the findings of our analysis
    and who wishes to read it.
- Wants:
    * They may wish to learn the findings of our study and how it might impact
    them, particularly if they live in an area inhabited by wolves. 
    * Alternatively, they might be a frequent reader of academic journal
    articles who wishes to learn about our findings and the process we employed
    to arrive at those findings.  

- Interaction Methods:
    * They will interact with our work by reading our report.
- Needs:
    * They will need a means of accessing our report.
- Skills:
    * The casual reader will posses a 12th grade reading level.

## Data Sources:
Question 1: 
Has the growth in the Wisconsin Gray Wolf population impacted the Wisconsin deer population?
Sub-questions:
    - Is there a correlation between the growth of the wolf population and changes in the deer population?
        * Data: 
            Wolf population datasets (see bottom of file)
            Statewide deer population (2003-2022) - https://apps.dnr.wi.gov/deermetrics/DeerStats.aspx?R=2 
    - Is there a correlation between fewer sick deer and wolf population growth?
        * Data:
            Wolf population datasets (see bottom of file)
            Statewide Chronic Wasting Disease Data (2002-2022) - https://apps.dnr.wi.gov/deermetrics/DeerStats.aspx?R=Disease 


Question 2: Has the growing wolf population led to an increase in the number of interactions between people and wolves?
Sub-questions:
    - How are wolf and human interactions changing via observations, attacks, and law enforcement encounters?
        * Data:
            2017 Wolf Report - https://p.widencdn.net/pa9xbm/WolfReport2017
            2018 Wolf Report - https://p.widencdn.net/ijt3dc/WolfReport2018
            2019 Wolf Report - https://p.widencdn.net/2o5pum/WolfReport2019
            2020 Wolf Report - https://dnr.wisconsin.gov/sites/default/files/topic/WildlifeHabitat/wolfreport2020.pdf
            2021 Wolf Report - https://widnr.widen.net/s/vlfpznrl2w/wisconsin_gray_wolf_2020_2021_final
            2022 Wolf Report - https://widnr.widen.net/s/nlrl7tzdw5/wisconsin_gray_wolf_report_2022
    - Is there a correlation in # of deer seen per hour by hunters and growing wolf populations?
        * Data:
            Wolf population datasets (see bottom of file)
            Statewide Number of Deer Seen by Hunters (2008-2022) - https://apps.dnr.wi.gov/deermetrics/DeerStats.aspx?R=OBSurvey#background
    - Is there a correlation between growth in wolf population and # of deer harvested?
        * Data:    
            Wolf population datasets (see bottom of file)
            Statewide Deer Harvesting Statistics (2006-2022) - https://apps.dnr.wi.gov/deermetrics/DeerStats.aspx?R=2 


Question 3: Time permitting, how have the lives and deaths of wolves changed over the reporting period?
Sub-questions:
    - How are wolf populations changing via quality and causes of death?
        * Data:
            2017 Wolf Report - https://p.widencdn.net/pa9xbm/WolfReport2017
            2018 Wolf Report - https://p.widencdn.net/ijt3dc/WolfReport2018
            2019 Wolf Report - https://p.widencdn.net/2o5pum/WolfReport2019
            2020 Wolf Report - https://dnr.wisconsin.gov/sites/default/files/topic/WildlifeHabitat/wolfreport2020.pdf
            2021 Wolf Report - https://widnr.widen.net/s/vlfpznrl2w/wisconsin_gray_wolf_2020_2021_final
            2022 Wolf Report - https://widnr.widen.net/s/nlrl7tzdw5/wisconsin_gray_wolf_report_2022


Wolf Population Datasets:
    2019 Wolf Report (wolf pop data 1980-2019) - https://p.widencdn.net/2o5pum/WolfReport2019
    2022 Wolf Report (wolf pop data 2000-2022) - https://widnr.widen.net/s/nlrl7tzdw5/wisconsin_gray_wolf_report_2022 

## Use Cases:

### 1. A Researcher Replicating Our Work
They will:
- Find the original source of the data we used
- Use our process to scrape the data
- Follow any data cleaning steps we employed
- Rerun the statistical tests we did in our analysis and compare their results
with ours
    * Check that the assumptions we used in our analysis also hold for the data
    in theirs

### 2. A Researcher Expanding Upon Our Work
They will:
- Find the original source of the data we used and the format we worked it into
- Decide whether to use our data source or another
- Use our process to scrape the data from our source, or use a variety of
methods to clean their alternate data source(s) 
- Understand why we selected the statistical tests we did so they can determine
what methods they will use in their work 
- If they decide to run the statistical tests we did, they will rerun the tests
and compare their results with ours
    * Check that the assumptions we used in our analysis also hold for the data
    in theirs


### 3. A Curious Reader Studying Our Report
They will:
- Access to results of our analysis, probably from a link online
- Examine the report to learn how wolves might impact their lives or to learn
about our analysis process 
