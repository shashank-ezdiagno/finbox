from .doc_parser import DocParser
from review.models import Doc
from django.forms.models import model_to_dict
class DocHandler():
    def __init__(self, file_path):
        self.parser = DocParser(file_path)


    def parse_data(self, max_count, doc_line_limit, headers, readable_headers, data_types):
        docs = self.parser.yield_data(max_count, doc_line_limit, headers, readable_headers, data_types)
        for doc in docs:
            #print(doc)
            doc_model = Doc(doc)
            doc_model.save()

    @staticmethod
    def create_index_from_db():
        from review.models import ReviewModel
        docs = ReviewModel.objects.all()
        for i,doc in enumerate(docs):
            doc_dict = model_to_dict(doc)
            doc_dict["id"] = doc.id
            print(i)
            doc_model = Doc(doc_dict)
            doc_model.create_index_from_db()
