from ReadFile import ReadFile
from Huffman import Huffman


file = ReadFile('txt_files/Text.txt')
huffman = Huffman()
huffman.generateKey(file.data)