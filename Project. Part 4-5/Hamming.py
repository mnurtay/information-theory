class Hamming:
  def __init__(self, data):
    self.data = self.__checkInputData(data)
  
  def __checkInputData(self, data):
    length = len(data)
    if length%4!=0:
      temp = 4-length%4
      temp = '0'*temp
      data += temp
    return data

  def encode(self):
    length = len(self.data)
    result = ''
    i, j = 0, 4
    while j<=length:
      temp = self.data[i:j]
      r1 = str(int(temp[0]) ^ int(temp[1]) ^ int(temp[2]))
      r2 = str(int(temp[1]) ^ int(temp[2]) ^ int(temp[3]))
      r3 = str(int(temp[0]) ^ int(temp[1]) ^ int(temp[3]))
      result += temp+r1+r2+r3
      i = j
      j += 4
    return result