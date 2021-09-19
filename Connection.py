import sqlite3
from sqlite3 import Error

db = r"GPS.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
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
    ip varchar(100),
    coordinates varchar(100),
    date varchar(100),
    lost boolean
    )"""
    create_table(conn, sql)

def add_location(connection, location):
    sql = """ INSERT INTO Locations (ip, coordinates, date, lost) VALUES (?,?,?,?)"""
    cur = connection.cursor()
    cur.execute(sql, location)
    connection.commit()
    return cur.lastrowid

def update_location(conn, location):
    sql = """ UPDATE Locations
     SET ip = ?, coordinates = ?, date = ?, lost = ?
       WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(sql, location)
    conn.commit()
    return cur.lastrowid

def get_location_by_id(conn, id):
    sql = """ SELECT * FROM Locations WHERE id = ? """
    cur = conn.cursor()
    cur.execute(sql, (id,))
    return cur.fetchall()

def get_location_by_ip(conn, ip):
    sql = """ SELECT * FROM Locations WHERE ip = ? """
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
    conn = create_connection(db)
    if conn is not None:
        for i in get_all(conn):
            print(i)
        close_connection(conn)
    else:
        print("Error! Cannot connect to database.")

if __name__ == '__main__':
    main()
