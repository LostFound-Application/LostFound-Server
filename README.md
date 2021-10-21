# LostFound-Server
## Server
The server communicates using UDP. All but confirmation messages are received by the ServerListenThread, and they are queued into ServerLAPIThread, where the message's priority is assessed. Depending on the priority, an answer will be send either through a low or a high priority send thread. After a message is sent through the LowPrioSendThread, the server does not expect an answer and kills the thread right after the send. When using HighPrioSendThread, the thread stays active after sending the message, expecting a confirmation message back from the client before the thread is killed, resending the message if a timeout happens. All changes to the SQLite server are triggered by the ServerLAPIThread.

Currently supported API requests are as follows:
- "lost, latitude, longitude, id"

A lost person is added into the database, the insertion includes the persons id, latitude, longitude, datetime of the messages arrival and boolean for lost. The boolean is always true.

- "found, id"

A person with the provided id is deleted from the database.

- "updateme"

The client is provided with the location data of all the lost people in the database.

To run the server use following command:
```bash
$> py .\server.py
```
To close the server use following command:
```bash
$> stop
```
Please wait for the server to fully close. If the server is incorrectly terminated, change of port numbers in the server and testclient files might be necessary.
## Clients
Two basic test clients are included to test server functionalities.

Testclient tests the "updateme" request, and prints the coordinates returned by the server as longitude, latitude pairs.

Testclient2 tests the "lost" request, and running it adds a new entry to the database.

To run a test client use following command:
```bash
$> py .\testclient.py
```
or
```bash
$> py .\testclient2.py
```
