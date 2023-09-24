

# In order to use the with statement
# we have to define __enter__ and __exit__
# It is important to note that we have to catch
# type, value and traceback

class something:

    # This is pretty easy
    def __enter__(self):
        print("entering")

    # And this is even more interesting
    def __exit__(self, type_, value, traceback):
        print("Exiting")
        print(type_, value, traceback)


if __name__ == '__main__':
    with something():
        print("eh")

    with open("with_stat_1.py", "r") as f:
        print(f.read())
