This document documents the source code of the back-end server in detail.


server.py:
This python script is the script responsible for booting up the server and shutting it down. 
This script can be started by running the command ''python3 server.py''.
To stop the server please type in 'stop' in the command line interface and wait till the server properly shuts down all its sockets.


It contains the global variables localHost, which is the ip the server runs on by default, and localPort, which is set to 5553. These variables can be modified to boot up the server with different settings.


The main function is bootServer(), which creates a socket to listen to responses, sets an appriopate time-out and binds the socket, 
and then creates and starts a listening thread that is dedicated to receiving information over the network.
After, it will loop until it receives as input the word 'stop'.
Once this happens, it will signal the  threads to cease operations, wait till these operations have succeeded, and then shutdown and close the listening socket, before terminating the process.


HighPrioSendThread.py


This file contains a threading class meant to send high priority UDP packets between two end-points as described in detail in the accompanying project report. 
The class will be initialised with the data and address it needs to send the data. It will continuously attempt to do this, using retransmissions if necessary, 
until either the data is sent or an error occured. 
Once this process is completed the thread itself will cease operation.


LowPrioSendThread.py


This file contains a threading class meant to send low priority UDP packets between two end-points as described in detail in the accompanying project report. 
The class contains a linked list that it continuously checks for new send request messages. 
The linked list itself is a list of tuples of the data it needs to send out and the address it needs to use as destination. Once a packet has been sent out, the request gets popped from the list.
New requests can be added with the addSendRequest() function, and an object of the class will keep working until the killThread function is called.


ServerLAPIThread.py
In this file is a threading class dedicated to processing API requests it receives from a listening thread. 
The class contains a linked list which it continuously checks for new items. 
If there is a new item, which is of the form (data, address), it processes this requests and, if needed, creates a reply to send back.
The API thread has its own dedicated low priority send thread that it uses to send low priority replies, and for high priority messages it will create a separate high priority thread that will operate in the background as it forwards the high priority reply.
The thread will initialise the SQLite database to be able to process the incoming requests upon startup.
Once this item has been processed, it will pop it from the linked list.
The server listening thread can add new items for the API thread to listen to but using the addAPIRequest() function.
The API thread will continue operating until the killThread()  function has been called on it.


This API thread has dedicated functions to processing API requests. Below each one will be briefly discussed.
addLostPerson(Data):
It splits the data on ",", creates a timestamp, and then enters a new lost person entry into the database file.
personFound(Data):
It splits the data on ",", retrieves the ID, then deletes a lost person entry from the database using that ID.
getLostLocations():
It requests all all location data from all lost person entries in the database, stores it in a variable, and returns this data.


ServerListenThread.py
This file contains a threading class that is used to listen for incoming UDP packets. 
It will do so continuously until the killThread() function is called on the object derived from the class. 
This class will make its own dedicated apiThread, see file ServerAPIThread.py for more information. 
If it receives data, it will forward this data to its dedicated API thread with the addAPIRequest(Data, address) call.
The socket will time-out every few seconds before restarting operation. 
This is done to allow for the proper closure of the socket if called upon to cease operation as the socket otherwise is a blocking call.


Methods.py
This file contains various helper functions that give access to the database. 
The list of functions and with their brief descriptions is found below.
addNewLocation(location): Add new lost entry to database with location.
getAll(): Return all entries
updateLocation(location, id): Update location of entry with ID.
getLost(): Get lost entries.
getLostLocations(): Get location information of all lost entrieds.
getLocationByID(id): Get location of entry with ID.
getLocationByClientID(cliid):
deleteLocation(id): Delete entry with ID.
initiateDatabase(): Initiate database.
deleteByClientID(cliid):


Connection.py
This file contains functions dedicated to creating the database tables and their connections, with some minor utility functions.
The list of functions is given below.
create_connection():
close_connection(conn):
create_table(conn, sql):
create_locations_table(conn):
add_location(connection, location):
update_location(conn, location):
get_location_by_id(conn, id):
get_location_by_clientid(conn, clientid):
get_all(conn):
get_lost(conn):
get_lost_locations(conn):
get_not_lost(conn):
delete_location(conn, id):
delete_location_by_clientid(conn, clientid):
delete_all(conn):
