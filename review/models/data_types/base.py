from review.helpers.indexing import Indexer
class DataType:
    def __init__(self, index):
        self.is_index = index

    # default is raw string
    def process(self, value):
        return [str(value)]

    def index(self, field, value, doc_id, score):
        if not self.is_index:
            return False
        else:
            # implement default indexer
            #print("inside default indexer", field, value, doc_id)
            indexer = Indexer.put_index(field, value, doc_id, score)
            return True

