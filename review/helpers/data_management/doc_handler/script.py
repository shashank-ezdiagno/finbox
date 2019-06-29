from .doc_handler import DocHandler
import os

def read_file():
    doc_line_limit = 8
    headers = ["product/productId", "review/userId", "review/profileName",
                    "review/helpfulness", "review/score", "review/time",
                    "review/summary", "review/text"]
    readable_headers = ["productId", "userId", "profileName",
                    "helpfulness", "score", "time",
                    "summary", "text"]
    data_types = [str,str,str,str,float,int,str,str]
    max_count = 1000
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(BASE_DIR,"finefoods.txt")
    handler = DocHandler(path)
    handler.parse_data(max_count, doc_line_limit, headers, readable_headers, data_types)