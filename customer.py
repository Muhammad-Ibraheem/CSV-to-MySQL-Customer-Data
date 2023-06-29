import pandas as pd
import mysql.connector


# Get data
def readData():
    data = pd.read_csv('customer.csv')
    processed_data = dataPreProcessing(data)
    dataStorage(processed_data)


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


# connection to DB
def connectDb():
    cnx = mysql.connector.connect(user="user", password="passwprd", host="host", database="database")
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


readData()
