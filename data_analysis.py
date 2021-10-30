import sys

def seperate_data(data):
    file = open(data, "r")

    instructions = dict()
    datas = dict()

    for line in file.readlines():
        line = line.split(",")
        access = line[1]
        ref = line[0][:-3]

        if access == "I":
            if ref in instructions.keys():
                instructions[ref] += 1
            else:
                instructions[ref] = 1
        else:
            if ref in datas.keys():
                datas[ref] += 1
            else:
                datas[ref] = 1
    
    print("Instructions\n")
    for key in instructions.keys():
        print(key + "," + instructions[key] + "\n")
    print("\nData:\n")
    for key in datas.keys():
        print(key + "," + datas[key] + "\n")

if __name__ == "__main__":
    seperate_data(sys.argv[1])