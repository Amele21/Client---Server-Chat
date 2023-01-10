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
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f"Server listening on: {HOST} on port: {PORT}")
        print(f"Connected by {addr}")
        print("Type /q to quit")
        print("Waiting for message...")
        while True:
            # Receive data from client. Data is decoded to string
            recv_data = conn.recv(1024)
            recv_data = recv_data.decode('utf-8')
            print(recv_data)
            # Client sent /q, so it closed, server will close too
            if recv_data == '/q':
                break

            # Send data to client type byte by encoding.Data can't be empty on send.
            send_data = input(">")
            while send_data == '':
                print("ERROR: MESSAGE MUST HAVE CONTENT")
                send_data = input(">")
            send_data = send_data.encode('utf-8')
            conn.sendall(send_data)
            # /q will close the server and client will receive /q and also close
            if send_data == b'/q':
                break
