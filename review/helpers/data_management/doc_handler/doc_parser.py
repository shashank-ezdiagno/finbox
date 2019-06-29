
class DocParser():
    def __init__(self, file_path):
        self.file_p = open(file_path, "rb")


    def yield_data(self, max_count, doc_line_limit, headers, readable_headers, data_types):
        j=0
        while(j<max_count):
            doc = {}
            flag = True
            for i in range(8):
                line = self.file_p.readline()
                doc_header = headers[i]
                readable = readable_headers[i]
                data_type = data_types[i]
                try:
                    line = line.decode()
                except Exception as e:
                    print(e)
                    flag = False
                    print(line)
                    continue
                line =line[len(doc_header)+1:].strip()
                doc[readable] = data_type(line)
            j+=1
            if flag:
                yield doc
            # skip empty lines
            empty_line = self.file_p.readline()
            while(not empty_line):
                empty_line = self.file_p.readline()