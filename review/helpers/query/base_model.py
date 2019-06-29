from ..indexing import Indexer
from review.models import Doc
class IndexQueryElement():
    def __init__(self, doc_id, fields, vals, score):
        length = float(len(vals))
        doc_vals = set()
        for field in fields:
            doc_vals = doc_vals.union(Indexer.get_reverse_index(doc_id, field))
        self.query_score = round(float(len(vals.intersection(doc_vals)))/length,2)
        self.doc_id = doc_id
        self.score = score

    def __gt__(self, other):
        if self.query_score != other.query_score:
            return self.query_score > other.query_score
        else:
            return self.score > other.score

    def __cmp__(self, other):
        if self.query_score != other.query_score:
            return cmp(self.query_score, other.query_score)
        else:
            return cmp(self.score, other.score)

    def __repr__(self):
        return "{},{},{}".format(self.doc_id, self.query_score, self.score)


    def __dict__(self):
        doc = Doc.get(self.doc_id)
        return dict(doc=doc, score=self.query_score, _id=self.doc_id)