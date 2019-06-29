from ..helpers.indexing.analyzer import StandardAnalyzer
from ..helpers.indexing.filter import CaseInsensitiveFilter
from ..helpers.indexing.tokenizer import StandardTokenizer
from .data_types import Text, RawString, Float, Integer
import uuid

class Doc():
    data = {}
    text = Text(StandardAnalyzer, StandardTokenizer, 2, CaseInsensitiveFilter)
    summary = Text(StandardAnalyzer, StandardTokenizer, 2, CaseInsensitiveFilter)
    productId = RawString()
    userId = RawString()
    profileName = RawString()
    helpfulness = RawString()
    score = Float(index=True)
    time = Integer(index=False)

    def __init__(self, raw_doc):
        self.raw = raw_doc

    @classmethod
    def get_type(cls, field):
        return getattr(cls, field)

    def save(self):
        tokens_dict = {}
        for field, value in self.raw.items():
            data_type = self.__class__.get_type(field)
            tokens = data_type.process(value)
            tokens_dict[field] = tokens
        doc_id = uuid.uuid4()
        self.raw["id"] = doc_id
        self.data[doc_id] = self.raw
        score = tokens_dict["score"][0]
        for field,tokens in tokens_dict.items():
            data_type = self.__class__.get_type(field)
            for token in tokens:
                data_type.index(field, token, doc_id, score)

    @staticmethod
    def get(doc_id):
        return Doc.data[doc_id]