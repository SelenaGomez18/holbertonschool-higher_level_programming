#!/usr/bin/env python3
"""
Client-Server application demonstrating serialization with JSON over sockets.
"""

import socket
import json


def start_server(host='127.0.0.1', port=65432):
    """
    Starts a simple TCP server that receives serialized data from a client.

    Args:
        host (str): The host IP address. Default is localhost.
        port (int): The port number to listen on.

    Returns:
        None
    """
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)

        print(f"Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Receive data from the client
        data = conn.recv(1024)

        if data:
            try:
                # Decode bytes -> string -> dict
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)
            except json.JSONDecodeError:
                print("Error decoding JSON data.")
        else:
            print("No data received from client.")

        conn.close()
        server_socket.close()

    except Exception as e:
        print(f"Server error: {e}")


def send_data(data_dict, host='127.0.0.1', port=65432):
    """
    Sends a serialized dictionary to the server.

    Args:
        data_dict (dict): Dictionary to serialize and send.
        host (str): The server IP address.
        port (int): The port to connect to.

    Returns:
        None
    """
    try:
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Serialize dictionary -> JSON string -> bytes
        serialized_data = json.dumps(data_dict).encode('utf-8')

        client_socket.sendall(serialized_data)
        client_socket.close()

    except ConnectionRefusedError:
        print("Connection failed: The server may not be running.")
    except Exception as e:
        print(f"Client error: {e}")
