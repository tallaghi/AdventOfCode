from itertools import permutations  

allNums = []
preambleNum = 25

def something(startIndex,total):
    tempTotal = 0
    for idx, val in enumerate(allNums[startIndex:]):
        tempTotal += val
        if total == tempTotal and val != total:
            correctSlice = allNums[startIndex:(startIndex+idx)]
            print(f"{max(correctSlice) + min(correctSlice)} equals {tempTotal} which equals {total}")
            return True
        elif tempTotal > total:
            return False

def part1():
    for idx, val in enumerate(allNums[preambleNum:],start=preambleNum):
        perm = permutations(allNums[(idx-preambleNum):(idx)],2)
        #print(f"{val.strip()} {idx}")
        numSet = set()
        for i in list(perm):  
            numSet.add(i[0] + i[1])
        if val not in numSet:
            # print(f"{val}")
            # break
            return val
    return 0

def part2():
    targetVal = part1()
    for idx, val in enumerate(allNums):
        success = something(idx,targetVal)
        if success:
            print("yay")
            break        


with open(r"FlatFiles/1292020.txt","r") as my_file:
    allNums = [int(i.strip()) for i in my_file.readlines()] 

part2()