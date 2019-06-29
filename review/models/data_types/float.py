from .base import DataType

class Float(DataType):
    def process(self, value):
        return [float(value)]