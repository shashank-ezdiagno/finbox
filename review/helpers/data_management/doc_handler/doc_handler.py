from .doc_parser import DocParser
from review.models import Doc
class DocHandler():
    def __init__(self, file_path):
        self.parser = DocParser(file_path)


    def parse_data(self, max_count, doc_line_limit, headers, readable_headers, data_types):
        docs = self.parser.yield_data(max_count, doc_line_limit, headers, readable_headers, data_types)
        for doc in docs:
            #print(doc)
            doc_model = Doc(doc)
            doc_model.save()