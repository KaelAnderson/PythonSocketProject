import socket

def main():
    # make the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server using ip and port
    host = '127.0.0.1'# basic localhost IP
    port = 30060 #random port over 5000 as requested 
    client_socket.connect((host, port))

    while True:
        #connection made, now running the program
        message = input("Enter a message ('end' to exit): ")
        

        # Send the message to the server
        client_socket.send(message.encode('utf-8'))

        # Receive and print the reversed message from the server
        reversed_message = client_socket.recv(1024).decode('utf-8')

        print(f"Server Response: {reversed_message}") # this prints out the reversed text that the server sent over
        if reversed_message == "dne":# this checks to see if the end message has been recieved and sent by the server
            # if so, then the client shuts down
            client_socket.close()
            break

            

if __name__ == '__main__':
    main()