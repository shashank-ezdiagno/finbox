from .base_model import IndexElement
class Indexer:
    _indices = {}
    _reverse_indices = {}
    _max_len_index= 0
    @classmethod
    def get_index(cls, field, val):
        if field not in cls._indices:
            cls._indices[field] = {}
        return cls._indices[field].get(val,{})

    @classmethod
    def get_reverse_index(cls, doc_id, field):
        #print("inside reverse index", doc_id, field)
        if doc_id not in cls._reverse_indices:
            cls._reverse_indices[doc_id] = {}
        return cls._reverse_indices[doc_id].get(field,set())

    @classmethod
    def put_index(cls, field, val, doc_id, score):
        if field not in cls._indices:
            cls._indices[field] = {}
        if val not in cls._indices[field]:
            cls._indices[field][val]={IndexElement(doc_id,score)}
        else:
            cls._indices[field][val].add(IndexElement(doc_id,score))
        if doc_id not in cls._reverse_indices:
            cls._reverse_indices[doc_id] = {}
        if field not in cls._reverse_indices[doc_id]:
            cls._reverse_indices[doc_id][field] = {val}
        else:
            cls._reverse_indices[doc_id][field].add(val)
        if len(cls._indices[field][val]) > cls._max_len_index:
            cls._max_len_index = len(cls._indices[field][val])
            cls._max_val = val