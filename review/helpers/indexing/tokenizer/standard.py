class StandardTokenizer():
    def __init__(self, min_token_length):
        self.min_token_length = min_token_length
    def get_tokens(self, text):
        words = text.split(" ")
        #print(text)
        for word in words:
            if len(word)>self.min_token_length:
                yield word