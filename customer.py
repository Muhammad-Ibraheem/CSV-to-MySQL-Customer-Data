import pandas as pd
import mysql.connector
import sys
import json


# Get data
def readData():
    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
            data = pd.read_csv(sys.argv[1])
            processed_data = dataPreProcessing(data)
            dataStorage(processed_data)
        else:
            raise ValueError("Invalid file extension or missing filename argument.")
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} does not exist")


# Preprocessing data
def dataPreProcessing(data):
    # check null or missing values
    if data.isnull().any().any():
        data = data.dropna()
    return data[['first_name', 'last_name', 'email', 'phone_number', 'age', 'gender', 'city', 'country']]


# store data in DB
def dataStorage(data):
    cnx = connectDb()
    cursor = cnx.cursor()
    tableCreation(cursor)
    saveData(cursor, data)
    cnx.commit()
    cnx.close()


def load_config_file(file_path):
    with open(file_path, "r") as config_file:
        return json.load(config_file)


# connection to DB
def connectDb():
    config = load_config_file("db_config.json")
    user = config["user"]
    password = config["password"]
    host = config["host"]
    database = config["database"]
    cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    return cnx


def tableCreation(cursor):
    query = """CREATE TABLE IF NOT EXISTS client_information (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        phone_number VARCHAR(25),
        age INT,
        gender VARCHAR(10),
        city VARCHAR(50),
        country VARCHAR(50)
    )"""
    cursor.execute(query)


# saving data in DB
def saveData(cursor, data):
    query = "INSERT INTO client_information(first_name, last_name, email, phone_number, age, gender, city, country) VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s)"
    data_tuples = []
    for row in data.values:
        data_tuples.append(tuple(row))
    cursor.executemany(query, data_tuples)


try:
    readData()
except ValueError as e:
    print(e)
