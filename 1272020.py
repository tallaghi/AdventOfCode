import threading, queue

allRules = []
rules = []
rulesDict = {}
searchColor = "shiny gold"
colorSet = set()
colorQueue = queue.Queue()
def setRules(allRules):
    rules.clear()
    for rule in allRules:
        ruleSplit = rule.split("bags contain")
        ruleParent = ruleSplit[0].strip()
        ruleChildren = ruleSplit[1].split(",")
        children = []
        for child in ruleChildren:
            children.append(child)
        rules.append({"parentColor" : ruleParent,"children": children })

def setRulesp2(allRules):
    for rule in allRules:
        ruleSplit = rule.split("bags contain")
        ruleParent = ruleSplit[0].strip()
        ruleChildren = ruleSplit[1].split(",")  
        rulesDict[ruleParent] = {}      
        for child in ruleChildren:
            if child.replace("\n","").strip() != "no other bags.":
                kid = child.split()
                numOfBags = int(kid[0])
                bagColor = f"{kid[1]} {kid[2]}"
                rulesDict[ruleParent][bagColor] = int(numOfBags)

def searchForChildColor():
    while True:
        color = colorQueue.get()
        print(f'Working on {color}')
        for rule in rules:
            if any(color in r for r in rule["children"]):
                colorSet.add(rule["parentColor"])
                colorQueue.put(rule["parentColor"])
                print(f'Added {rule["parentColor"]} to queue')    
        print(f'Finished working on {color}')
        colorQueue.task_done()

def countBagsWithinColor(color):
    childBags = rulesDict[color]
    bagCount = 0
    if childBags == {}:
      return 0
    for child in childBags: 
        bagCount += childBags[child] + (childBags[child] * countBagsWithinColor(child))
    return bagCount

def part1():
    setRules(allRules)
    threading.Thread(target=searchForChildColor, daemon=True).start()
    colorQueue.put(searchColor)

    colorQueue.join()

    print(colorSet)
    print(len(colorSet))

def part2():
    setRulesp2(allRules)
    bagCount = countBagsWithinColor(searchColor)
    print(bagCount)

with open(r"FlatFiles/1272020.txt","r") as my_file:
    allRules = my_file.readlines()


part1()
part2()