#!/usr/bin/env python3
import sqlite3

def create_table():
    conn = sqlite3.connect('test.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
    print("Table created successfully")
    conn.close()    

def insert_data():
    conn = sqlite3.connect('test.db')
    conn.execute("INSERT INTO EMPLOYEES (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    conn.execute("INSERT INTO EMPLOYEES (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    conn.execute("INSERT INTO EMPLOYEES (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    conn.execute("INSERT INTO EMPLOYEES (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    conn.commit()
    print("Records created successfully")
    conn.close()

def print_data():
    conn = sqlite3.connect('test.db')
    cursor = conn.execute("SELECT id, name, address, salary from EMPLOYEES")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()

def update_data():
    conn = sqlite3.connect('test.db')
    # find out which row you want to update, so print_data runs first
    print_data()
    update_select = input("select row to update:")
    # what value needs to be changed?
    print("you can change, NAME, ADDRESS or SALARY")
    update_stuff = input("Enter NAME ADDRESS OR SALARY:")
    update_val = input("Enter new value:")
    if update_stuff == "NAME":
        cursor = conn.execute("UPDATE EMPLOYEES set NAME= ? where ID = ?", (update_val,update_select))
        conn.commit()
    elif update_stuff == "ADDRESS":
        cursor = conn.execute("UPDATE EMPLOYEES set ADDRESS= ? where ID = ?", (update_val,update_select))
        conn.commit()
    elif update_stuff == "SALARY":
        cursor = conn.execute("UPDATE EMPLOYEES set SALARY= ? where ID = ?", (update_val,update_select))
        conn.commit()

def delete_data():
    conn = sqlite3.connect('test.db')
    #print the table first
    print_data()
    line_del = input("Enter line to be deleted")
    conn.execute("DELETE from EMPLOYEES where id = ?;", (line_del))
    conn.commit()
    print_data()

if __name__ == "__main__":
    create_table()
    print("="*35)
    print("Inserting data")
    insert_data()
    print("="*35)
    print("here is your table")
    print_data()
    print("="*35)
    print("lets update it")
    update_data()
    print("="*35)
    print("Lets delete some stuff")
    delete_data()
    print("all done with the challenge")




