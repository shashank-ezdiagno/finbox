from .base import DataType


class RawString(DataType):
    def __init__(self):
        super().__init__(index=False)