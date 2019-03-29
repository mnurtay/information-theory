class Huffman:
    def __init__(self):
        self.data = {}
        self.key = {}
  
    def __sort(self, dictionary):
        for key, value in dictionary.items():
            self.data[key] = value['probability']
        self.data = dict(sorted(self.data.items(), key=lambda x: x[1], reverse=True))

    def generateKey(self, dictionary):
        self.__sort(dictionary)
        