import os.path as op
file_name = input()
event = input()
event = "'" + event + "'"

if(op.isfile(file_name)): # file exists
    with open(file_name, 'r', encoding="utf-8") as f:
        fulltext = f.read()
        if fulltext == []:  # empty file
            with open(file_name, 'w', encoding= "utf-8") as f:
                f.write("event" + " 1 " + "- " + event + '\n')
        else:
            text = []
            with open(file_name, 'r', encoding="utf-8") as f:
                text = f.readlines()
                index = 0
                for i in range(len(text)):
                    if text[i] == '\n':
                        continue
                    else:
                        index = i
                        break
                string = text[index].split()
                number = int(string[1])
                number += 1
                newstring = " ".join(["event", str(number), "-", event+'\n'])
                text.insert(0, newstring)
            with open(file_name, 'w', encoding="utf-8") as f:
                f.writelines(text)
else: # file does not exist
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write("event" + " 1" + " - " + event + '\n')
