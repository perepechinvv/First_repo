record = "Drake Mikelsson,19"
path = "test.txt" 

def add_employee_to_file(record, path):

    fh = open(path, 'a')
    fh.write('\n')
    fh.write(record)
    fh.close()

    fh = open(path, 'r')
    text = fh.read()
    print(text)
    fh.close()



add_employee_to_file(record, path)