from ReadFile import ReadFile
from Huffman import Huffman


file = ReadFile('txt_files/Text.txt', analize=True)
huffman = Huffman(file.data)
encripted = huffman.encript(file.file_text)
decripted = huffman.decript(encripted)
