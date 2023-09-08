class InvalidPriceError(Exception):
    def __init__(self, price=0):
        self.price = price

    def __str__(self):
        return 'Invalid price'


class InvalidNameError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Invalid name'
