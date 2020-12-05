print(range(150,193))

yearRanges = {
    "byr": range(1920,2003),
    "iyr": range(2010,2021),
    "eyr": range(2020,2031)
}

eyeColors = ["amb","blu","brn","gry","grn","hzl","oth"]

def checkYear(field):
    if int(field[-4:]) in yearRanges.get(field[:3]):
        return True
    return False

def checkField(field):
    if "yr:" in field and len(field) == 8:        
        return checkYear(field)
    elif "hgt:" in field:
        if field.endswith("cm") and int(field.replace("hgt:","").replace("cm","")) in range(150,194):
            return True
        elif field.endswith("in") and int(field.replace("hgt:","").replace("in","")) in range(59,77):
            return True
    elif "hcl:" in field and field[4] == "#" and len(field) == 11:        
        return True
    elif "ecl:" in field and field[-3:] in eyeColors:        
        return True
    elif "pid:" in field and len(field) == 13 and field[-9:].isnumeric():
        return True
    return False


with open(r"FlatFiles/1242020.txt","r") as my_file:
    allPassports = my_file.read()
    chunked = allPassports.split("\n\n")
    passportCount = 0
    processedFieldsCount = 0
    for passport in chunked:        
        passportFlat = passport.replace("\n"," ")
        fieldCount = passportFlat.count(":")
        if (fieldCount == 7 and "cid:" not in passport) or fieldCount==8:
            processedFieldsCount += 1
            fields = passportFlat.split(" ")
            valid = True
            i = 0
            while valid and i < len(fields):   
                if "cid:" not in fields[i]:
                    valid = checkField(fields[i])
                i += 1
            if valid:
                passportCount += 1
    print(passportCount)  