import socket

def main():
    # make a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server using ip and port
    host = '127.0.0.1'  
    port = 30060         
    client_socket.connect((host, port))

    while True:
        message = input("Enter a message ('end' to exit): ")
        

        # Send the message to the server
        client_socket.send(message.encode('utf-8'))

        # Receive and print the reversed message from the server
        reversed_message = client_socket.recv(1024).decode('utf-8')

        print(f"Server Response: {reversed_message}")
        if reversed_message == "dne":
            client_socket.close()
            break

            

if __name__ == '__main__':
    main()