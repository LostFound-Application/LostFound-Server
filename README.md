# LostFound-Server

The server working using UDP, and has a lowprio send, a high prio send, receive and API threads. A message gets received by the receive thread, forwarded to the API thread which then forwards a reply using either a low prio or high prio send thread.
Two basic test clients is included to test server functionalities.
The api requests are: "lost, latitude, longitude, id", "found, id", "updateme"
Please stop the server by typing in stop in the terminal and wait for it to fully close. In case you wrongfully terminate the server, you might need to change the port numbers in the client and server test programs.