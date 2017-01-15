import asyncore
import socket
from optparse import OptionParser
from fibonnachi_compute import fibonacci_generator


class Handler(asyncore.dispatcher_with_send):

    def handle_read(self):
        self.out_buffer = self.recv(1024)

        if len(self.out_buffer) > 0:
            received_number = int.from_bytes(self.out_buffer, byteorder='little', signed=False)
            number = fibonacci_generator(received_number)
            fibonnachi_number_bytes = number.to_bytes(((number.bit_length() + 7) // 8), byteorder='little',
                                                      signed=False)
            print('Received number: ', received_number)
            print('Calculated Fibonnachi number: ', number)
            print('Calculated Fibonnachi number bytes: ', fibonnachi_number_bytes)

            # Grab chunks of bytes and transmit them until there are no more to grab
            i = 0
            byte_chunk = fibonnachi_number_bytes[i:i + 1024]
            while byte_chunk != b'':
                i += 1024
                self.send(byte_chunk)
                print('Calculated chunks: ', byte_chunk)
                byte_chunk = fibonnachi_number_bytes[i:i + 1024]
            self.close()


class FibonnachiServer(asyncore.dispatcher):

    def __init__(self, host, port, listener_number):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(listener_number)

    # When we get a client connection, handle it with a dispatcher
    def handle_accept(self):
        client = self.accept()
        if client is not None:
            socket, address = client
            print('Connection by ', address)
            Handler(socket)

server = FibonnachiServer('localhost', 8080, 5)
asyncore.loop()
