
with open(r"FlatFiles/1212020.txt","r") as my_file:
    numbers = my_file.readlines()
    for idx,num in enumerate(numbers):
        for i in range((idx+1),len(numbers)):
            for j in range((i+1),len(numbers)):
                if int(num) + int(numbers[i]) + int(numbers[j]) == 2020:
                    print(int(num)+int(numbers[i])+int(numbers[j]))
                    print(int(num)*int(numbers[i])*int(numbers[j]))

