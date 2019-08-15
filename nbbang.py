fileSelect = int(input("Use existing file? 1. yes / 2. no "))
fileName = input("type the name of the file : ")

def readFile(fN) :
    f = open("events/" + fN + ".txt")
    data = f.read().splitlines()
    stats = { }
    for info in data :
        temp = info.split()
        if temp[0] in stats:
            stats[temp[0]] += float(temp[1])
        else :
            stats[temp[0]] = float(temp[1])
    print(stats)
    f.close()

def writeFile(fN) :
    g = open("events/" + fileName + ".txt", "at")
    name = input('누가 돈을썼습니까? ')
    while name!='':
        money = input("돈을 얼마나 썼나요? ")
        g.write(name + " " + money + "\n")
        name = input('누가 돈을썼습니까? ')
    g.close()


if fileSelect == 1 :
    readFile(fileName)
    writeFile(fileName)
    readFile(fileName)
else :
    writeFile(fileName)
    readFile(fileName)





# a = input('얼마?')
# print(a)
#
# list1=[]
# list1.append
