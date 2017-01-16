## Synopsis

This is a Python 3.6.0 client and server. The client will pass a number n to the server and the server will then compute the nth Fibonacci number and return it to the client.

## Code Example
$ ./runserver.sh &<br />
$ python3 socket_client.py 10 <br />
55<br />
$ python3 socket_client.py 100 <br />
354224848179261915075<br />

## Motivation

This is a coding exercise for a pretty cool job :)

## Installation

This is built with Python 3.6.0 and uses only standard modules from it.

1) First, make sure Python 3.6.0 is downloaded and installed.<br />
2) Check git is also installed<br />
3) git clone https://github.com/cmavromichalis/PythonFibb.git<br />
4) cd PythonFibb/<br />
5) ./runserver.sh &<br />
6) python3 socket_client.py 10000

## Description

If there is an issue computing the nth Fibonacci, the server will return the value 0<br />
The server will listen for connections on port 8080 and expects to receive in bytes an unsigned integer

## Tests

Describe and show how to run the tests with code examples.

## License

MIT
