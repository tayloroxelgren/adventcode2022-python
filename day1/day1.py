with open("day1-puzzelin.txt","r") as f:
    data=f.readlines()


for i in range(len(data)):
    try:
        data[i]=int(data[i].split("\n")[0])
    except:
        data[i]="SEPARATOR"


def gatherElfCalz(data):
    elves=[]
    result=0

    for d in data:
        if type(d) is int:
            result+=d
        else:
            elves.append(result)
            result=0
    
    return elves


elves=gatherElfCalz(data)

maxElf=max(elves)
print("Answer for part 1: ",maxElf)

elves.sort(reverse=True)
print("Answer for part 2: ",sum(elves[:3]))
