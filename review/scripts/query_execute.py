from ..helpers.indexing import Indexer
from ..helpers.query import TermsQueryExecutor

def run():
    print(Indexer._max_len_index)
    executor = TermsQueryExecutor(8000)
    doc_ids = executor.execute(["summary","text"], {"product","found", Indexer._max_val})
    print([doc for doc in doc_ids])