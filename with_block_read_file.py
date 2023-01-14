# with block
# context manager
# its popular beacuse we dont have to close the file in this manner

with open("temp_file.txt", "r") as f:
    data=f.read()
    print(data)
print(f.closed)