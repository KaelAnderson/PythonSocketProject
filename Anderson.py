import socket

def reverse_string(input_string):
    return input_string[::-1]   #this reverses the string using regex

def main():
    # create the socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # gives the socket its connection info
    host = '127.0.0.1'  # host ip adress
    port = 30060
    server_socket.bind((host, port))

    # listen for calls
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")

    while True:
        # connect with client
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            else:
                reversed_data = reverse_string(data) #call the reverse string function
                client_socket.send(reversed_data.encode('utf-8')) # send back the reversed data    
                if data == 'end':
                     print(f"Connection with {addr} closed")
                     client_socket.close()
                     
            


if __name__ == '__main__':
    main()