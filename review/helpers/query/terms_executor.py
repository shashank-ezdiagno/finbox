from ..indexing import Indexer
from .base_model import IndexQueryElement
from .heap_min import HeapMin

class TermsQueryExecutor:
    def __init__(self, max_count):
        self.max_count = max_count


    def execute(self, fields, vals):
        hp = HeapMin([])
        visited_docs = set()
        for val in vals:
            for field in fields:
                for doc in Indexer.get_index(field, val):
                    if doc.doc_id in visited_docs:
                        continue
                    query_element = IndexQueryElement(doc.doc_id, fields, vals, doc.score)
                    if hp.size < self.max_count:
                        hp.insert(query_element)
                    else:
                        if hp.peek() < query_element:
                            hp.pop_min()
                            hp.insert(query_element)
                    visited_docs.add(doc.doc_id)
        hp.arr.sort(reverse=True)
        for doc in hp.arr:
            yield doc.__dict__()