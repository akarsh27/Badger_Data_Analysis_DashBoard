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
