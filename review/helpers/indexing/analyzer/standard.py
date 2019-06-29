import re
import string

class StandardAnalyzer:
    def __init__(self, tokenizer, min_token_length, filter):
        self.tokenizer = tokenizer(min_token_length)
        self.filter = filter

    def pre_process(self, text):
        text = re.sub("[{}]".format(string.punctuation), " ",text)
        text = re.sub(r"\s+", " ",text)
        return text

    def tokenize(self, data):
        return self.tokenizer.get_tokens(data)

    def try_filter(self, token):
        return self.filter.satisfy_filter(token)

    def process(self, text):
        text = self.pre_process(text)
        tokens = self.tokenize(text)
        for token in tokens:
            yield self.try_filter(token)