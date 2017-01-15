import socket
from optparse import OptionParser
from fibonnachi_compute import fibonacci_generator


parser = OptionParser()
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=False,
                  help="don't output debug statements")

(options, args) = parser.parse_args()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5) # become a server socket, maximum 5 connections

while True:
    print('Waiting for a connection...')
    connection, address = server_socket.accept()
    buffer = connection.recv(32)
    if len(buffer) > 0:
        received_number = int.from_bytes(buffer, byteorder='little', signed=False)
        print('Received number: ', received_number)
        number = fibonacci_generator(received_number)
        print('Calculated Fibonnachi number: ', number)
        fibonnachi_number_bytes = number.to_bytes(((number.bit_length() + 7) // 8), byteorder='little', signed=False)
        print('Calculated Fibonnachi number: ', fibonnachi_number_bytes)

        byte_length = len(fibonnachi_number_bytes)

        i = 0
        byte_chunk = fibonnachi_number_bytes[i:i + 1024]
        # Grab chunks of bytes and transmit them until there are no more to grab
        while byte_chunk != b'':
            i += 1024
            connection.send(byte_chunk)
            print('Calculated chunks: ', byte_chunk)
            byte_chunk = fibonnachi_number_bytes[i:i+1024]
        connection.close()
