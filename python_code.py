class python_code:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_code(self, text):
        f = open(self.file_name, 'w+')
        f.write("text")
    
    def read_code(self):
        f = open(self.file_name, 'r')
        lines = f.readlines()
        print(lines)

code = python_code("file1.txt")
code.read_code()

        




