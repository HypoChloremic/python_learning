"""In Python 3.5 and later versions, yield from can be used to implement coroutines. 
Coroutines are functions that can be paused and resumed, allowing for asynchronous programming. 
Here's an example of a coroutine implemented using yield from.add()



In this example, coroutine is a generator function that loops indefinitely and yields control 
to the caller using yield. When the coroutine is resumed, it receives a value using the send method. 
The main function creates an instance of the coroutine using coroutine(), and then calls next(c) 
to advance the coroutine to its first yield statement. The send method is then used to send two messages to the coroutine.

When this code is run, the output will be:"""


def coroutine():
    while True:
        print("Starting the couroutine, meaning this is being run now")
        x = yield
        print('Received: ', x)


def main():
    c = coroutine()
    next(c)
    c.send(10)
    c.send(20)
    c.close()


if __name__ == '__main__':
    main()
