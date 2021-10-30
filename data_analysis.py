import sys

def seperate_data(data):
    file = open(data, "r")

    instructions = dict()
    datas = dict()
    counter = 0
    for line in file.readlines():
        line = line.split(",")
        access = line[1].strip()
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
                counter += 1
                datas[ref] = 1
    
    print("Instructions\n")
    for key in instructions.keys():
        print(str(key) + "," + str(instructions[key]) + "\n")
    print("\nData:\n")
    for key in datas.keys():
        print(str(key) + "," + str(datas[key]) + "\n")
    print(counter)

if __name__ == "__main__":
    # seperate_data("/Users/mingonsong/2021-2022/CSC369/lec8/tr-heaploop.ref")
    seperate_data("/Users/mingonsong/2021-2022/CSC369/lec8/tr-matmul.ref")