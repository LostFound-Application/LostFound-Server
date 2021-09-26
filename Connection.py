import sqlite3
from sqlite3 import Error

db = r"GPS.db"

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    conn.close()

def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def create_locations_table(conn):
    sql = """ CREATE TABLE IF NOT EXISTS Locations (
    id integer PRIMARY KEY,
    clientid varchar(100),
    latitude varchar(100),
    longitude varchar(100),
    date varchar(100),
    lost boolean
    )"""
    create_table(conn, sql)

def add_location(connection, location):
    sql = """ INSERT INTO Locations (clientid, latitude, longitude, date, lost) VALUES (?,?,?,?,?)"""
    cur = connection.cursor()
    cur.execute(sql, location)
    connection.commit()
    return cur.lastrowid

def update_location(conn, location):
    sql = """ UPDATE Locations
     SET ip = ?, latitude = ?, longitude = ?, date = ?, lost = ?
       WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(sql, location)
    conn.commit()

def get_location_by_id(conn, id):
    sql = """ SELECT * FROM Locations WHERE id = ? """
    cur = conn.cursor()
    cur.execute(sql, (id,))
    return cur.fetchall()

def get_location_by_clientid(conn, ip):
    sql = """ SELECT * FROM Locations WHERE clientid = ? """
    cur = conn.cursor()
    cur.execute(sql, (ip,))
    return cur.fetchall()

def get_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Locations")
    return cur.fetchall()

def get_lost(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Locations WHERE lost = 1")
    return cur.fetchall()

def get_not_lost(conn):
    sql = """ SELECT * FROM Locations WHERE lost = 0 """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def delete_location(conn, id):
    sql = """ DELETE FROM Locations WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def delete_all(conn):
    cur = conn.cursor()
    cur.execute("DELETE * FROM Locations")
    conn.commit()
    

def main():
    #Used currently for testing the functionalities
    conn = create_connection()
    
    if conn is not None:
        add_location(conn, ("k22","23.44","45.33","14.23 24.09.2021",0))
        add_location(conn, ("k2233","43.44","67.33","14.53 24.08.2021",1))
    else:
        print("Error! Cannot connect to database.")

if __name__ == '__main__':
    main()
