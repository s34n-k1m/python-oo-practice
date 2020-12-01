class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Set the start number and generation number"""
        self.start = start
        self.prev_num = start - 1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} prev_num={self.prev_num}>"

    def generate(self):
        """Returns the next serial number: +1"""
        self.prev_num += 1
        return self.prev_num

    def reset(self):
        """Resets the serial number sequence to the initial starting number"""
        self.prev_num = self.start - 1
