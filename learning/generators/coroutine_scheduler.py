"""
Basic Concepts
Generator: It's a special type of iterator where you can pause the execution of the function and return a value using the yield keyword. The next time the generator's __next__() method is called (or when next() is called with the generator), it picks up right where it left off until it hits another yield.

Coroutine: At a high level, a coroutine is a generalization of generators. While a generator produces values (using yield), a coroutine can also consume values (using yield again but in a slightly different context). This means that a coroutine can both produce and consume values.

Coroutines have a send() method which is used to send values into the coroutine. When a value is sent into the coroutine, the function runs until it hits a yield, at which point the value of the expression to the right of the yield keyword is returned. The next time a value is sent into the coroutine, execution picks up right after the yield, and the value that was sent in can be captured with the yield expression.

Using Coroutines
Starting a Coroutine: Unlike generators which start execution immediately on the first call to next(), coroutines need to be 'primed' first. This means you have to always call next(coroutine) or coroutine.send(None) to start the coroutine.

Sending Values: After starting, you can send values into the coroutine using the send() method.

Closing Coroutines: You can manually close a coroutine by calling its close() method.

Real World Example: A Simple Coroutine-Based Task Scheduler
Imagine a situation where you have multiple tasks that need to be scheduled and run, but you want to give each task a chance to run for a bit before moving on to the next one, allowing tasks to yield control back to the scheduler. This can be done using coroutines.

"""
# Simple Coroutine Scheduler


def task1():
    while True:
        print("Task 1 running")
        yield


def task2():
    while True:
        print("Task 2 running")
        yield


def scheduler(tasks):
    while True:
        for task in tasks:
            next(task)

# Usage:


if __name__ == '__main__':
    tasks = [task1(), task2()]
    scheduler(tasks)
