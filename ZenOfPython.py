import time

with open("C:/Users/HP/Documents/Klas 1/SoftwareDevelopment/2022/Read-Write/read-files/README.md") as empty:
    content = empty.readlines()
    for i in range(len(content)):
        time.sleep(1)
        print(content[i])



# oude code

# file = open('C:/Users/HP/Documents/Klas 1/SoftwareDevelopment/2022/Read-Write/read-files/README.md','r')
# lineList = file.readlines()
# for i in range(len(lineList)):
#     time.sleep(1)
#     print(lineList[i])