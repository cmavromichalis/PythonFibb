import socket
import threading
from optparse import OptionParser
from fibonnachi_compute import Fibonacci


class FibonnachiServer(threading.Thread):

    def __init__(self, host, port, socket):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.socket = socket
        print("New thread started for " + ip + ":" + str(port))

    def run(self):
        buffer = self.socket.recv(1024)

        if len(buffer) > 0:
            received_number = int.from_bytes(buffer, byteorder='little', signed=False)

            # Check the bytes we received are actually a unsigned number.
            # Otherwise send back 0
            if (type(received_number) != int) or (received_number < 0):
                print(received_number, 'is not a unsigned, whole number.')
                self.socket.send(b'\x00\x00')
                self.socket.close()
            else:
                print('Received number: ', received_number)
                number = Fibonacci.fibonacci_generator(received_number)
                fibonnachi_number_bytes = number.to_bytes(((number.bit_length() + 7) // 8), byteorder='little',
                                                          signed=False)
                print('Calculated Fibonnachi number: ', number)

                # Grab chunks of bytes and transmit them until there are no more to grab
                i = 0
                byte_chunk = fibonnachi_number_bytes[i:i + 1024]
                while byte_chunk != b'':
                    i += 1024
                    self.socket.send(byte_chunk)
                    print('Calculated chunks: ', byte_chunk)
                    byte_chunk = fibonnachi_number_bytes[i:i + 1024]
                self.socket.close()


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 8080))
threads = []

while True:
    socket.listen(4)
    print("\nListening for incoming connections...")
    (clientsock, (ip, port)) = socket.accept()
    newthread = FibonnachiServer(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)
