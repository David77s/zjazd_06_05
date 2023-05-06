import csv

filename = 'username.csv'

with open(filename,encoding='utf-8',newline='') as csv_file:  #biblioteka csv impementuje new line, wiec nic nie wpisujemy

    #Sniffer
    sample = csv_file.read()
    file_dialect = csv.Sniffer().sniff(sample)
    #Wracaamy na początek
    csv_file.seek(0)
    csv_file.readline().strip('\n').split(file_dialect.delimiter)

    # przekazujemy dialekt który został znaleziony przez Sniffera
    reader = csv.reader(csv_file,quoting=csv.QUOTE_NONNUMERIC,dialect = file_dialect)

    for row in reader:
        print(row)

print(f"Delimeter: {file_dialect.delimiter}")
print(f"Escape: {file_dialect.escapechar}")
print(f"Linie terminator: {repr(file_dialect.lineterminator)}")