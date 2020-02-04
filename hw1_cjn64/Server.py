import threading
import time
import random
import socket as mysoc

# server task
def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',50007)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)

    #
    data_from_server=csockid.recv(100)
    print("[S]: Data received from client::  ",data_from_server.decode('utf-8'))

    # Convert to ascii with underscores between values.
    asciiData = ""
    dataReceived = data_from_server.decode('utf-8')
    for char in dataReceived:
        asciiData += str(ord(char)) + "_"
    asciiData = asciiData[:-1]

    csockid.send(asciiData.encode('utf-8'))

   # Close the server socket
    ss.close()
    exit()

t1 = threading.Thread(name='server', target=server)
t1.start()
time.sleep(random.random()*5)

# cd Desktop/School/Internet Technology/HW 1/hw1_cjn64