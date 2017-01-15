import socket
import asyncore
import time


class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        print('Sent the number: ', message)
        self.out_buffer = message.to_bytes(1024, byteorder='little', signed=False)

    def handle_read(self):
        fibonnachi_number_bytes = b''

        buffer = self.recv(1024)
        check = int.from_bytes(buffer, byteorder='little', signed=False)

        while True:
            buffer = self.recv(1024)
            if buffer:
                time.sleep(0.5)
                fibonnachi_number_bytes += buffer[0:]
                print('Receiving response...')
            else:
                print('Calculated Fibonnachi number bytes: ', fibonnachi_number_bytes)
                fibonnachi_number = int.from_bytes(fibonnachi_number_bytes, byteorder='little', signed=False)
                print('Calculated Fibonnachi number : ', fibonnachi_number)
                break

    def handle_close(self):
        self.close()

client = Client('localhost', 8080, 1000)
asyncore.loop()