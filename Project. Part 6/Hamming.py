class Hamming:
  def __init__(self):
    self.errors = {
      '000': None,
      '001': 6,
      '010': 5,
      '011': 3,
      '100': 4,
      '101': 0,
      '110': 2,
      '111': 1
    }
  
  def __checkInputData(self, data):
    length = len(data)
    if length%4!=0:
      temp = 4-length%4
      temp = '0'*temp
      data += temp
    return data
  
  def __xor(self, temp):
    r1 = str(int(temp[0]) ^ int(temp[1]) ^ int(temp[2]))
    r2 = str(int(temp[1]) ^ int(temp[2]) ^ int(temp[3]))
    r3 = str(int(temp[0]) ^ int(temp[1]) ^ int(temp[3]))
    return r1, r2, r3

    
  def encode(self, data):
    data = self.__checkInputData(data)
    length = len(data)
    result = ''
    i, j = 0, 4
    while j<=length:
      temp = data[i:j]
      r1, r2, r3 = self.__xor(temp)
      result += temp+r1+r2+r3
      i, j = j, j+4
    return result
  
  def decode(self, data):
    length = len(data)
    result = ''
    i, j = 0, 7
    while j<=length:
      temp = data[i:j]
      rg1, rg2, rg3 = self.__xor(temp)
      rc1, rc2, rc3 = temp[4], temp[5], temp[6]
      s1 = str(int(rc1)^int(rg1))
      s2 = str(int(rc2)^int(rg2))
      s3 = str(int(rc3)^int(rg3))
      error = self.errors[s1+s2+s3]
      fix = str(int(not int(temp[error])))
      temp = temp[:error]+fix+temp[error+1:]
      result += temp[:4]
      i, j = j, j+7
    return result