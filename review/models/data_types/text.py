from .base import DataType
from review.helpers.data_management import TextProcessor

class Text(DataType):
    def __init__(self, analyzer, tokenizer, min_token_length, filter):
        super().__init__(index=True)
        self.processor = TextProcessor(analyzer, tokenizer, min_token_length, filter)

    def process(self, value):
        tokens = self.processor.parse(value)
        for token in tokens:
            yield token