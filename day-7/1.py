import sys
sys.setrecursionlimit(100000)

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

class Directory:
    def __init__(self) -> None:
        self.files = []
        self.subdirs = []

    def size(self):
        total = 0
        for file in self.files:
            total += file
            if total > 100000:
                return 0, False
        for subdir in self.subdirs:
            size, valid = subdir.size()
            if not valid:
                return 0, False
            total += size
            if total > 100000:
                return 0, False
        return total, True

    def to_array(self):
        output = [item for item in self.files]
        for subdir in self.subdirs:
            output.append(subdir.to_array())
        return output

directories = {}
directory_stack = ["/"]
for line in lines:
    print(directory_stack)
    if line.startswith("$"):
        command = line[2:].split(" ")
        if command[0] == "cd":
            if command[1] == "..":
                directory_stack.pop()
                if len(directory_stack) == 0:
                    directory_stack = ["/"]
            else:
                directory = command[1]
                directory_stack.append(directory)
                if directory == "/":
                    directory_stack = ["/"]
                if directory not in directories:
                    directories[directory] = Directory()
    else:
        directory = directory_stack[-1]
        if line.startswith("dir"):
            dirName = line.split(" ")[1]
            if dirName not in directories:
                directories[dirName] = Directory()           
            directories[directory].subdirs.append(directories[dirName]) 
            
        else:
            directories[directory].files.append(int(line.split(" ")[0]))

total = 0
print(directories["/"].subdirs)
for d in directories:
    directory = directories[d]
    size, valid = directory.size()
    if valid:
        total += size

print(total)