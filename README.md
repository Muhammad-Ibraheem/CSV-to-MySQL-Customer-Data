# CSV-to-MySQL-Customer-Data

This Python script reads customer data from a CSV file, performs data preprocessing, and stores the processed data into a MySQL database.

## Usage

1. Install the required Python packages:
2. Prepare the CSV file:
- Place the CSV file containing customer data in the same directory as the script.
- Ensure that the CSV file has the columns: 'first_name', 'last_name', 'email', 'phone_number', 'age', 'gender', 'city', 'country'.

3. Update the connection details:
- Open the script and modify the credentials in the `connectDb()` function to match your MySQL server.

4. Execute the script:
- Run the following command:
  ```
  python script.py
  ```

5. Data storage:
- The processed customer data will be saved in a MySQL database table named "client_information".

## Customization

- To modify the selected columns or table schema, update the code in the `dataPreProcessing()`, `tableCreation()`, and `saveData()` functions.

- If your MySQL server is hosted on a different host or port, adjust the connection details in the `connectDb()` function.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

