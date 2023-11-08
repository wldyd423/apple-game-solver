import os
count = dict()
if __name__ == "__main__":
    path = "./data"
    for file in os.listdir(path):
        # print(file)
        name = file.split(".")[0]
        label = name.split("_")[2]
        # print(name, label)
        if label not in count:
            count[label] = [file]
        else:
            count[label].append(file)
    
    for key in sorted(list(count)):
        print(key, len(count[key]))