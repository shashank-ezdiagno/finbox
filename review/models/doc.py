from ..helpers.indexing.analyzer import StandardAnalyzer
from ..helpers.indexing.filter import CaseInsensitiveFilter
from ..helpers.indexing.tokenizer import StandardTokenizer
from .data_types import Text, RawString, Float, Integer
from django.db import models
import uuid
from django.forms.models import model_to_dict

class ReviewModel(models.Model):
    class Meta:
        app_label = 'review'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    summary = models.TextField()
    productId = models.CharField(max_length=100)
    userId = models.CharField(max_length=100)
    profileName = models.CharField(max_length=100)
    helpfulness = models.CharField(max_length=10)
    score = models.FloatField(max_length=10)
    time = models.IntegerField()

class Doc():
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
        doc_model = ReviewModel(**self.raw)
        doc_model.save()
        score = tokens_dict["score"][0]
        for field,tokens in tokens_dict.items():
            data_type = self.__class__.get_type(field)
            for token in tokens:
                data_type.index(field, token, doc_id, score)

    def create_index_from_db(self):
        tokens_dict = {}
        doc_id = self.raw.pop("id")
        for field, value in self.raw.items():
            data_type = self.__class__.get_type(field)
            tokens = data_type.process(value)
            tokens_dict[field] = tokens

        score = tokens_dict["score"][0]
        for field,tokens in tokens_dict.items():
            data_type = self.__class__.get_type(field)
            for token in tokens:
                data_type.index(field, token, doc_id, score)


    @staticmethod
    def get(doc_id):
        return model_to_dict(ReviewModel.objects.get(id=doc_id))