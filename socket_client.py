import socket
import asyncore
import time
import argparse

class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port, number):
        if (type(number) != int) or (number < 0):
            print(number, 'is not a unsigned, whole number. Please try again.')
            exit()

        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        # print('Sent the number: ', number)
        self.out_buffer = number.to_bytes(1024, byteorder='little', signed=False)

    def handle_read(self):
        fibonnachi_number_bytes = b''

        while True:
            buffer = self.recv(1024)
            if len(buffer):
                time.sleep(0.5)
                fibonnachi_number_bytes += buffer[0:]
                # print('Receiving response...')
            else:
                # print('Calculated Fibonnachi number bytes: ', fibonnachi_number_bytes)
                fibonnachi_number = int.from_bytes(fibonnachi_number_bytes, byteorder='little', signed=False)
                # print('Calculated Fibonnachi number : ', fibonnachi_number)
                print(fibonnachi_number)
                break

    def handle_close(self):
        self.close()


parser = argparse.ArgumentParser(description='Passes n to a server to computer the nth Fibonacci number.')
parser.add_argument('integer', nargs=1, type=int, help='The nth Fibonacci number to compute')
arguements = parser.parse_args()
command_line_number = (arguements.integer[0])


client = Client('localhost', 8080, command_line_number)
asyncore.loop()
