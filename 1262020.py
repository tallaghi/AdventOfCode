from collections import Counter 

with open(r"FlatFiles/1262020.txt","r") as my_file:
    allAnswers = my_file.read()
    chunked = allAnswers.split("\n\n")
    count = 0
    for chunk in chunked:
        #Part 1
        #count += len(set(chunk.replace("\n","").strip()))
        amountNeeded = chunk.count("\n") + 1
        charSet = set(chunk.replace("\n","").strip())
        for char in charSet:
            if chunk.count(char) == amountNeeded:
                count += 1
    print(count)