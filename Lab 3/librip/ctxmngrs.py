import time

class timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.time = time.clock()

    def __exit__(self, type, value, traceback):
        print(time.clock() - self.time)