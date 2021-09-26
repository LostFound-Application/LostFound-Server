from . import Connection
#import Connection

def addNewLocation(location):
    conn = Connection.create_connection()
    id = Connection.get_location_by_clientid(conn, location[0])
    if not id:
        id = Connection.add_location(conn, location)
    Connection.close_connection(conn)
    return id

def getAll():
    conn = Connection.create_connection()
    all = Connection.get_all(conn)
    Connection.close_connection(conn)
    return all

def updateLocation(location, id):
    addid = list(location)
    addid.append(id)
    location = tuple(addid)

    conn = Connection.create_connection()
    id = Connection.update_location(conn, location)
    Connection.close_connection(conn)
    return id

def getLost():
    conn = Connection.create_connection()
    lost = Connection.get_lost(conn)
    Connection.close_connection(conn)
    return lost

def getLostLocations():
    conn = Connection.create_connection()
    lost = Connection.get_lost_locations(conn)
    Connection.close_connection(conn)
    return lost

def getLocationByID(id):
    conn = Connection.create_connection()
    found = Connection.get_location_by_id(conn, id)
    Connection.close_connection(conn)
    return found

def getLocationByClientID(cliid):
    conn = Connection.create_connection()
    found = Connection.get_location_by_clientid(conn, cliid)
    Connection.close_connection(conn)
    return found
def deleteLocation(id):
    conn = Connection.create_connection()
    Connection.delete_location(conn, id)
    Connection.close_connection(conn)

def initiateDatabase():
    conn = Connection.create_connection()
    Connection.create_locations_table(conn)
    Connection.close_connection(conn)

def deleteByClientID(cliid):
    conn = Connection.create_connection()
    Connection.delete_location_by_clientid(conn, cliid)
    Connection.close_connection(conn)

def main():
    print("ok")
    
if __name__ == '__main__':
    main()