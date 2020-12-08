# PART 1 ONLY
import threading, queue

allRules = []
rules = []
searchColor = "shiny gold"
colorSet = set()
colorQueue = queue.Queue()
def setRules(allRules):
    for rule in allRules:
        ruleSplit = rule.split("bags contain")
        ruleParent = ruleSplit[0].strip()
        ruleChildren = ruleSplit[1].split(",")
        children = []
        for child in ruleChildren:
            tSplit = child.split()            
            #childNum = tSplit[0]
            childColor = f"{tSplit[1]} {tSplit[2]}"
            #children.append({"amount":childNum,"color":childColor})
            children.append(childColor)
        rules.append({"parentColor" : ruleParent,"children": children })

def searchForChildColor():
    while True:
        color = colorQueue.get()
        print(f'Working on {color}')
        for rule in rules:
            if color in rule["children"]:
                colorSet.add(rule["parentColor"])
                colorQueue.put(rule["parentColor"])                    
                print(f'Added {rule["parentColor"]} to queue')    
        print(f'Finished working on {color}')
        colorQueue.task_done()

with open(r"FlatFiles/1272020.txt","r") as my_file:
    allRules = my_file.readlines()

setRules(allRules)
threading.Thread(target=searchForChildColor, daemon=True).start()
colorQueue.put(searchColor)

colorQueue.join()

print(colorSet)
print(len(colorSet))