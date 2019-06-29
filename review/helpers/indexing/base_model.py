class IndexElement:
    def __init__(self, doc_id, score):
        self.doc_id = doc_id
        self.score = score
    def __eq__(self, other):
        return self.doc_id==other.doc_id and self.score==other.score

    def __hash__(self):
        return hash(self.doc_id)

    def __cmp__(self, other):
        return cmp(other.score, self.score)

    def __repr__(self):
        return "({},{})".format(self.doc_id, self.score)