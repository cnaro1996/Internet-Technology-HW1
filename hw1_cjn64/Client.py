import threading
import time
import random
import socket as mysoc

#client task
def client():
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))


# Define the port on which you want to connect to the server
    port = 50007
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

    #
    msg="Apple"
    print("Sending the following string to server:: ", msg)
    cs.send(msg.encode('utf-8'))

    data_from_server=cs.recv(100)
    print("Data received from server:: ", data_from_server.decode('utf-8'))

# close the cclient socket
    cs.close()
    exit()

t2 = threading.Thread(name='client', target=client)
t2.start()