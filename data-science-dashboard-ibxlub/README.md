

## Objective

Construct a simple web application to analyze and visualize scientific data. The application should be capable of ingesting a dataset, performing basic computations, and displaying the results in a user-friendly format.

## Brief

We would like you to build a web application that imports a CSV file containing scientific data, performs some basic analysis, and presents the results in a meaningful way. 
The CSV file will contain data related to a specific experiment and it will have fields such as 'Experiment Name', 'Date', 'Observation Type', and 'Value'. 
Each ‘Experiment Name’ can have multiple measurements of each 'Observation type', potentially occurring on differing 'Date' with differing 'Value'.
Below is an example table:

| Experiment Name | Date       | Observation Type | Value  |
|:----------------|:-----------|:-----------------|:-------|
| Alpha Test      | 2024-04-01 | Temperature      | 5.6    |
| Beta Probe      | 2024-04-02 | Pressure         | 3.9    |
| Alpha Test      | 2024-04-01 | Temperature      | 5.6    |
| Gamma Analysis  | 2024-04-03 | Humidity         | 4.2    |
| Beta Probe      | 2024-04-02 | Pressure         | 3.9    |
| Delta Study     | 2024-04-04 | Viscosity        | 6.1    |
| Gamma Analysis  | 2024-04-05 | Humidity         | 4.5    |
| Epsilon Review  | 2024-04-06 | pH Level         | 7.0    |


## Tasks

- Implement the assignment using an MVC framework like Rails, Laravel, Django, or similar web framework you feel comfortable with
- Your application should persist data in a database. SQLite is preferred, but you are free to use a database of your choice

1. **Create data file:** Create a csv file as described above and populate with some made up data
2. **Data Ingestion:** Create an endpoint that accepts a CSV file as input.
    - The CSV file will have columns 'Experiment Name', 'Date', 'Observation Type', and 'Value'. 
    - 'Experiment Name' and 'Observation Type' are strings.
    - 'Date' is in yyyy-mm-dd format.
    - 'Value' is a float.
    - Store the CSV data in a SQL database. 

2. **Data Analysis:** Implement a function that calculates the average 'Value' for each 'Observation Type' in each 'Experiment Name'.
    - The function should return a dictionary where the keys are the 'Experiment Name' and the values are another dictionary. 
    - In the second dictionary, the keys should be 'Observation Type' and the values should be the average 'Value'.

3. **Data Presentation:** Create a web page that displays the results of the data analysis.
    - Display the 'Experiment Name' and for each experiment show the 'Observation Type' and its average 'Value'.
    - Allow the user to sort the experiments by 'Experiment Name' and 'Observation Type'.
    - Implement a search functionality to find an 'Experiment Name'.
    - Use libraries to provide the above sort and search functionality rather than writing the code from scratch

4. **Testing Requirements:**
    - Write unit tests for the data analysis function.
    - Write integration tests for the data ingestion endpoint and the data presentation web page.



### Evaluation Criteria

- Code quality and organization
- Usage of modern programming practices
- Effective use of the database
- Functionality of the data analysis and presentation
- Quality and coverage of the tests

### CodeSubmit 

Please organize, design, test, and document your code as if it were going into production.  

Please regularly commit and push your changes to the git repo as you develop your application.



Have fun coding! 🚀

The U of W - Madison Team
