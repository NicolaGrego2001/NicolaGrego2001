import gzip

file_gz_path = "test.csv.gz"
file_path = "test.csv"

def load_gzip_into_python(path):
    with gzip.open(path, 'rb') as in_gzip:
        content = in_gzip.read()
        content_text = content.decode()
        print(content_text.split('\r\n'))
        #content_list = content.split(b'\r\n')
        #print(content_list)


def decompress_gzip_into_file(path):
    with gzip.open(path, 'rb') as in_gzip:
        with open(path.replace('.gz', ''), 'wb') as out_file:
            out_file.write(in_gzip.read())


def compress_file_into_gzip(path):
    with open(path, 'rb') as in_file:
        with gzip.open(path + '.gz', 'wb') as out_gzip:
            out_gzip.write(in_file.read())

#load_gzip_into_python(file_gz_path)
#decompress_gzip_into_file(file_gz_path)
#compress_file_into_gzip(file_path.replace('.gz', ''))