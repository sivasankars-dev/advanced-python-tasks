class FileWriter:
    def write(self, data):
        pass
    
class ReadOnly:
    def read(self, data):
        pass

class TextFileWriter(FileWriter):
    def write(self, data):
        print(f"Writing text: {data}")

class ReadOnlyFileWriter(ReadOnly):
    def read(self, data):
        print('Read only: ', data)

def writeFile(file, data):
    file.write(data)

def readFile(file, data):
    file.read(data)
    
writeFile(TextFileWriter(), "hello siva")
readFile(ReadOnlyFileWriter(), "Hello kowsi")