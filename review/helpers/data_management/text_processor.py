from .base_processor import DataProcessor

class TextProcessor(DataProcessor):
    def __init__(self, analyzer, tokenizer, min_token_length, filter):
        self.analyzer = analyzer(tokenizer, min_token_length, filter)

    def parse(self, data):
        tokens = self.analyzer.process(data)
        for token in tokens:
            yield token