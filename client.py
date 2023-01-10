# Adrian Melendrez
# CS 372 Summer 2022
# Assignment: Programming Project Client-Server Chat (Portfolio Assignment)
# Description: This program is a simple client-server program that uses python sockets
#              The program emulates a simple 1 -to- 1 chat client.
#              Only one socket connection is made and this socket is reused.

import socket


HOST = 'localhost'
PORT = 4038

# SOURCES: https://docs.python.org/3/howto/sockets.html for creating sockets
#          https://realpython.com/python-sockets/  for echo client and server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    addr = s.connect((HOST, PORT))
    print(f"Connected to: {HOST} on port: {PORT} ")
    print("Type /q to quit")
    print("Enter message to send...")
    while True:
        # Send data to server in bytes by encoding. Data can't be empty on send
        send_data = input(">")
        while send_data == '':
            print("ERROR: MESSAGE MUST HAVE CONTENT")
            send_data = input(">")
        send_data = send_data.encode('utf-8')
        s.sendall(send_data)
        # /q will close the client and server will receive /q and also close
        if send_data == b'/q':
            break

        # Data received from server and decoded to string type
        recv_data = s.recv(1024)
        recv_data = recv_data.decode('utf-8')
        print(str(recv_data))
        # Server sent /q, so it closed, client will close too
        if recv_data == '/q':
            break
