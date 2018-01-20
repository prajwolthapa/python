file_name='directory.txt'
access_mode = 'r'
def directory():
    with open(file_name,access_mode) as dirpath:
        return dirpath.readline()
