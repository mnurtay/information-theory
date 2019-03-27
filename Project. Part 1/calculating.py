reading = open('Text.txt', 'r')
prob = {}
count = 0

for line in reading:
    for item in line:
        if item == ' ':
            item = '_'
        if item in prob:
            prob[item]['count'] += 1
        else:
            prob[item] = {'count':1, 'probability':0}
        count += 1

writeFile = open('output.txt', 'w')
for key, value in sorted(prob.items()):
    value['probability'] = value['count']/count
    string = key+"  -  Count: "+str(value['count'])+"   \tProbability: "+str(value['probability'])+'\n'
    writeFile.write(string)