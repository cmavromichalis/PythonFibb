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

The algoirthm is:<br />
* a = 0       <br />
* b = 1       <br />
* loop        <br />
  * old_b = b <br />
  * b += a    <br />
  * a = old_b <br />
        
Using a 2.5Ghz Intel Core i7 with 16GB of ram here were my calculation times and digits:<br />

n digits     - time to compute (in seconds) <br />
1            - 0.000  <br />
10           - 3.099 * 10^-6 <br />
100          - 1.215 * 10^-5 <br />
1,000        - 1.268 * 10^-4 <br />
10,000       - 2.831 * 10^-3 <br />
100,000      - 1.1032 <br />
1,000,000    - 10.534 <br />
10,000,000   - 981.280 <br />

## Range of inputs client and server can handle

The max nth number you can request is limited to 2,468 digits long. The time it takes is dependent on how long you want to wait. With my timings from above, calculation time grows linearly with 10 million digits taking 16 minutes + time to transmit; about 20 minutes.

## Tests

To run tests test.sh is included which will test:<br />
1) Fibonacci numbers are correct using known good values<br />
2) Bad parameters are not accepted<br />
3) That the server responds asynchronously

## Desired optimizations

Some desired optimizations to have in this would be:<br />
1) A faster algorithm, I'm sure that there are better ones than this simple one <br />
2) Fast transmitting of data, when the numbers get huge it takes time to transfer them. Maybe this can be accomplished quicker.<br />
3) Memory thrashing, trying to compute 1,000,000,000 digits takes a really long time. It never finished for me. I think because the numebrs get so bug that memory thrashes.


## License

MIT
