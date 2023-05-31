import time
class Stoper():
    def __init__(self):
        self.startTime = 0.0
        self.measureTime = 0.0

    def start(self):
        self.startTime = time.time()
        self.measureTime = 0.0

    def read(self):
        self.measureTime = time.time() - self.startTime
        return self.measureTime

    def reset(self):
        self.measureTime = 0.0
        self.startTime = time.time()