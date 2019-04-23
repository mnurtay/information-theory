from ReadFile import ReadFile
from Huffman import Huffman
from Hamming import Hamming
from random import randint

def writeToFile(fileName, string):
  writeFile = open('txt_files/'+fileName+'.txt', 'w')
  writeFile.write(string)

def setErrors(data):
  length = len(data)
  i, j = 0, 7
  while j<=length:
    randIndex = randint(i, j-1)
    temp = data[randIndex]
    temp = '1' if int(temp)==0 else '0'
    data = data[:randIndex] + temp + data[randIndex+1:]
    i=j; j+=7
  return data


file = ReadFile('txt_files/Text.txt', analize=True)
source = Huffman(file.data)
encripted = source.encript(file.file_text)
channel = Hamming()
encripted = channel.encode(encripted)

#set errors
errorData = setErrors(encripted)
writeToFile('Encripted Text', errorData)

#fix errors
channel = Hamming()
trueData = channel.decode(errorData)
decripted = source.decript(trueData)
writeToFile('Decripted Text', decripted)
