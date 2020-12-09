allInstructions = []

def runInstructionSet(instructions):
    indexSet = set()
    accum=0
    i=0
    while i < len(instructions):
        ins = instructions[i]
        instruction = ins[:3].strip()
        number = int(ins[4:])
        currentI = i

        if instruction == "nop":
            i += 1
        elif instruction == "acc":
            accum += number
            i += 1
        elif instruction == "jmp":
            i += number
            
        if i not in indexSet:
            indexSet.add(i)
        else:
            print(f"current I is: {currentI} | newI is: {i} | instruction is: {instruction} | number is: {number} | accum is: {accum}")
            print(indexSet)   
            return currentI, i, accum,instruction,number,False
    print(f"current I is: {currentI} | newI is: {i} | instruction is: {instruction} | number is: {number} | accum is: {accum}")
    return currentI, i, accum,instruction,number,True
    
def part1():
    indexSet = set()
    accum=0
    i=0
    while i < len(allInstructions):
        ins = allInstructions[i]
        instruction = ins[:3].strip()
        number = int(ins[4:])
        if instruction == "nop":
            i += 1
        elif instruction == "acc":
            accum += number
            i += 1
        elif instruction == "jmp":
            i += number
        
        if i not in indexSet:
            indexSet.add(i)
        else:
            print(accum)
            break

def part2():  
    currentI, i, accum,instruction,number,success = runInstructionSet(allInstructions)
    staticI = i
    while not success:
        modifiedInstructions = allInstructions.copy()
        index = 0
        for idx, ins in enumerate(modifiedInstructions[staticI:]):
            if ("jmp" in ins or "nop" in ins):
                index = idx+staticI
                staticI = idx+1+staticI
                break
        print(index)
        print(modifiedInstructions[index])
        print(allInstructions[index])
        if 'jmp' in modifiedInstructions[index]:
            modifiedInstructions[index] = modifiedInstructions[index].replace('jmp','nop')
        elif 'nop' in modifiedInstructions[index]:
            modifiedInstructions[index] = modifiedInstructions[index].replace('nop','jmp')
        print(modifiedInstructions[index])
        currentI, i, accum,instruction,number,success = runInstructionSet(modifiedInstructions)
    print("Success!")

with open(r"FlatFiles/1282020.txt","r") as my_file:
    allInstructions = my_file.readlines()

part2()