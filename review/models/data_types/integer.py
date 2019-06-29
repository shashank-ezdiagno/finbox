from .base import DataType
class Integer(DataType):
    def __init__(self, index):
        self.is_index = index
    def process(self, value):
        return [int(value)]