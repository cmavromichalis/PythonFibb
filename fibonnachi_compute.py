import time

# Hold the numbers we calculated already; has our seeds to start
FIBONACCI_NUMBERS = [0, 1]


# Function that will calculate and return the n'th Fibonacci number.
def fibonacci_generator(number):
    # Validate input
    if number <= 0:
        return 'Please enter a number greater than 0'

    # If we have already calculated this, return it
    if len(FIBONACCI_NUMBERS) > number:
        print("Length:", len(FIBONACCI_NUMBERS))
        return FIBONACCI_NUMBERS[number]

    # Else calculate it where we left off
    number_computed = len(FIBONACCI_NUMBERS)
    a = FIBONACCI_NUMBERS[number_computed - 2]
    b = FIBONACCI_NUMBERS[number_computed - 1]
    counter = number_computed - 1

    # Calculation loop
    start_time = time.time()
    while counter < number:
        # One liner:
        a, b = b, a + b
        # old_b = b
        # b += a
        # a = old_b
        counter += 1
        FIBONACCI_NUMBERS.append(b)
    end_time = time.time()
    print("Total time taken to calculate loop: ", end_time - start_time)
    return b


print("Precalculating 10000", fibonacci_generator(10000))  # Error
#print("Precalculating 10000", fibonacci_generator(11))  # Error
#print("1st num should be. ", fibonacci_generator(10))  # 0
#print("10 num should be. ", fibonacci_generator(10))  # 0
#print("20 num should be. ", fibonacci_generator(20))  # 0
#print("10 num should be. ", fibonacci_generator(10))  # 0
# print("42 num should be. ", fibonacci_generator(ct.value))  # 0
#print("500000 num should be.", fibonacci_generator(1000001))
