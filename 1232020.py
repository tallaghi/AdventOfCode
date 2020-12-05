def countTrees(down, right, slopes):
    horizLoc = 0
    treeCount = 0
    i = down
    while i < len(slopes):
        slope = slopes[i].strip()
        horizLoc += right
        while len(slope) <= horizLoc:
            slope += slope
        char = slope[horizLoc]
        if char == "#":
            treeCount += 1
        i += down
    return treeCount

    
with open(r"FlatFiles/1232020.txt","r") as my_file:
    slopes = my_file.readlines()
    print(countTrees(1, 3, slopes) * countTrees(1, 1, slopes) *
     countTrees(1, 5, slopes) * countTrees(1, 7, slopes) * 
     countTrees(2, 1, slopes))