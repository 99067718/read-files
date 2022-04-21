import time
file = open('C:/Users/HP/Documents/Klas 1/SoftwareDevelopment/2022/Read-Write/read-files/README.md','r')
lineList = file.readlines()
for i in range(len(lineList)):
    time.sleep(1)
    print(lineList[i])