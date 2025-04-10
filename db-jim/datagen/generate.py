import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta
import argparse

fake = Faker()

def connect_db(host, user, pw, db): 
    try:
        connection = mysql.connector.connect(
            host=host;
            user=user,
            password=pw,
            database=db
        )
        return connection
    except mysqld.connector.Error as err:
        print("Erro connection to mysql: {err}")
        return None

def create_tables(waiter):
    waiter.execute("""
    CREATE TABLE IF NOT EXISTS connection_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME NOT NULL,
        incoming_ip VARCHAR(45) NOT NULL,
        outgoing_ip VARCHAR(45) NOT NULL
    )
    """)
    
    # User data table
    waiter.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        address TEXT NOT NULL
    )
    """)
    
    # User payments table
    waiter.execute("""
    CREATE TABLE IF NOT EXISTS user_payments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        last_payment_date DATE NOT NULL,
        next_payment_date DATE NOT NULL,
        payment_amount DECIMAL(10, 2) NOT NULL,
        billing_address TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user_data(user_id)
    )
    """)
    
    # Employee data table
    waiter.execute("""
    CREATE TABLE IF NOT EXISTS employee_data (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        address TEXT NOT NULL,
        employee_email VARCHAR(100) NOT NULL,
        employee_login_id VARCHAR(50) NOT NULL
    )
    """)

def generate_user_data():



def generate_user_payments():



def generate_employee_data():


def main():
    parser = argparse.ArgumentParser(description='generate data')
    parser.add_argument('-h', default='localhost')
    parser.add_argument('-u', default='root')
    parser.add_argument('-p', default='')
    parser.add_argument('-d', required=True)
    parser.add_argument('--users', type=int, default=100)
    parser.add_argument('--payments', type=int, default=100)
    parser.add_argument('--employees', type=int, default=100)
    parser.add_argument('--create-tables', action='store_true')
    
    args = parser.parse_args()

    connection = connect_db(args.h, args.u, args.p, args.d)
    if not connection:
        return
    
    waiter = connection.cursor()