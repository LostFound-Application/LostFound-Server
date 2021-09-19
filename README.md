# LostFound-Server

The server working using UDP, and has a send, receive and API thread. A message gets received by the receive thread, forwarded to the API thread which then forwards a reply using the send thread.
A basic test client is included to test server functionalities.
Please stop the server by typing in stop in the terminal and wait for it to fully close. In case you wrongfully terminate the server, you might need to change the port numbers in the client and server test programs.