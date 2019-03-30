class ReadFile:
  def __init__(self, file_name, analize):
    self.file_name = file_name
    self.analize = analize
    self.file_text = None
    self.count = 0
    self.data = {}
    self.__read()
  
  def __read(self):
    try:
      read = open(self.file_name, 'r')
      if self.analize:
        self.__analize(read)
        self.__writeToFile()
    except:
      print("File Not Found!")
  
  def __analize(self, read):
    for text in read:
      self.file_text = text
      for item in text:
        if item in self.data:
          self.data[item]['count'] += 1
        else:
          self.data[item] = {'count':1, 'probability':0}
        self.count += 1
  
  def __writeToFile(self):
    writeFile = open('txt_files/Probability.txt', 'w')
    for key, value in sorted(self.data.items()):
      value['probability'] = round(value['count']/self.count, 10)
      if key == '\n':
        key = '\\n'
      string = key+"  -  Probability: "+str(value['probability'])+'\n'
      writeFile.write(string)
