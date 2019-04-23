class Huffman:
    def __init__(self, dictionary):
        self.key = {}
        self.combinates = self.__sort(dictionary)
        self.__generateKey(self.__sort(dictionary))

    # Sort list by probabilities
    def __sort(self, dictionary):
        arr = []
        dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1]['probability']))
        for key, value in dictionary.items():
            arr.append({ 'mark':key, 'probability':value['probability'] })
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]['probability'] == arr[j]['probability']:
                    first = ord(arr[i]['mark'])
                    second = ord(arr[j]['mark'])
                    if first < second:
                        temp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
        return arr

    # Sort the list alphabetically when the probabilities are equal
    def __sortList(self, arr):
        arr = sorted(arr, key=lambda x: x['probability'])
        return arr
    
    def __setCode(self, mark, code):
        for item in mark:
            if type(item)==list:
                self.__setCode(item, code)
            else:
                if item not in self.key:
                    self.key[item] = code
                else:
                    self.key[item] = code + self.key[item]

    def __createCode(self, arr):
        pass
                    

    def __generateKey(self, arr):
        length = len(arr)-1
        while length > 0:   
            first = arr.pop(0)
            second = arr.pop(0)

            if(first['probability'] <= second['probability']):
                self.__setCode(first['mark'], '0')
                self.__setCode(second['mark'], '1')
            else:
                self.__setCode(first['mark'], '1')
                self.__setCode(second['mark'], '0')
            
            temp = {
                'mark': [second['mark'], first['mark']],
                'probability': second['probability']+first['probability']
            }
            arr.append(temp)

            arr = self.__sortList(arr)
            length -= 1
        writeFile = open('txt_files/Keys.txt', 'w')
        for key, value in sorted(self.key.items()):
            if key == '\n':
                key = '\\n'
            string = key+"\t-\t"+value+"\n"
            writeFile.write(string)

    def encript(self, text):
        encripted = ''
        for item in text:
            encripted += self.key[item]
        return encripted

    def decript(self, text):
        decripted = ''
        code = ''
        for item in text:
            code += item
            if code in self.key.values():
                index = list(self.key.values()).index(code)
                decripted += list(self.key.keys())[index]
                code = ''
        return decripted
