import math
rowStartLoc = 0
rowEndLoc = 127
colStartLoc = 0
colEndLoc = 7

def findLocation(string,rnge,frontChar,backChar,length):
    location = 0
    for idx,val in enumerate(string):
        if idx < (length-1):
            if val == frontChar:
                rnge = rnge[:len(rnge)//2]
            elif val == backChar:
                rnge = rnge[len(rnge)//2:]
        else:
            if val == frontChar:
                location = rnge[0]
            elif val == backChar:
                location = rnge[1]
    return location

with open(r"FlatFiles/1252020.txt","r") as my_file:
    seatLocations = my_file.readlines()
    # For part 1
    #highestID = 0
    seatIDs = []
    for seatLocation in seatLocations:
        row = findLocation(seatLocation[0:7],range(rowStartLoc,rowEndLoc+1),'F','B',7)
        col = findLocation(seatLocation[7:].replace("\n","").strip(),range(colStartLoc,colEndLoc+1),'L','R',3)
        seatID = row * 8 + col
        # For part 1
        # if seatID > highestID:
        #     highestID = seatID
        seatIDs.append(seatID)
    seatIDs.sort()
    mySeat = [i for i in range(seatIDs[0],seatIDs[len(seatIDs)-1] + 1) if i not in seatIDs]
    print(mySeat)
    
