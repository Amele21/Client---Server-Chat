# README
Client Server chat document
Introduction:
● This program is a simple client-server program that uses python sockets The program emulates a
simple 1 -to- 1 chat client. Only one socket connection is made and this socket is reused.
Instructions for how to run:
● NOTE: python command is python3.
● 1st run python server.py
● 2nd run python client.py
● Enter a message in the client program first. Then you can go back and forth. End with /q.
Comments:
● The program does not allow empty messages to be sent. A loop is used to force the user to input
valid data. This ensures the program doesn’t fail. Both server and client will receive the /q data
when sent. Both programs will close sockets on this data.
