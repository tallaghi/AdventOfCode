
with open(r"FlatFiles/1222020.txt","r") as my_file:
    passwords = my_file.readlines()
    pwCount = 0
    for pw in passwords:
        pwsplit = pw.split(":")
        password = pwsplit[1]
        char = pwsplit[0][len(pwsplit[0])-1]
        rnge = pwsplit[0][0 : len(pwsplit[0])-2]
        rngesplit = rnge.split("-")
        # count = password.count(char)
        # if password.count(char) >= int(rngesplit[0]) and password.count(char) <= int(rngesplit[1]):
        #     pwCount += 1
        if (password[int(rngesplit[0])] == char) != (password[int(rngesplit[1])] == char):
             pwCount += 1
    print(pwCount)
        